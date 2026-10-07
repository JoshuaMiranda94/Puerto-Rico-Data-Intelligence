from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from pr_data_intelligence.extract import CensusConfig, fetch_acs_municipalities, save_raw
from pr_data_intelligence.quality import run_quality_checks, write_quality_report
from pr_data_intelligence.transform import transform_municipality_data, build_rankings
from pr_data_intelligence.load import save_processed_csv, load_sqlite


def main() -> None:
    raw_path = PROJECT_ROOT / "data" / "raw" / "acs_pr_municipalities_raw.csv"
    processed_path = PROJECT_ROOT / "data" / "processed" / "pr_municipality_indicators.csv"
    dashboard_path = PROJECT_ROOT / "data" / "exports" / "pr_dashboard_dataset.csv"
    rankings_path = PROJECT_ROOT / "data" / "exports" / "municipality_rankings.csv"
    db_path = PROJECT_ROOT / "data" / "pr_data_intelligence.sqlite"
    quality_path = PROJECT_ROOT / "reports" / "data_quality_report.json"

    print("Puerto Rico Data Intelligence")
    print("-----------------------------")
    print("1/5 Extracting Census ACS municipality data...")

    raw = fetch_acs_municipalities(CensusConfig())
    save_raw(raw, raw_path)

    print(f"   Raw rows: {len(raw)}")
    print("2/5 Running data quality checks...")

    quality = run_quality_checks(raw)
    write_quality_report(quality, quality_path)

    if not quality.passed:
        raise SystemExit(
            f"Quality gate FAILED. See: {quality_path}"
        )

    print("   Quality gate: PASS")
    print("3/5 Transforming data...")

    processed = transform_municipality_data(raw)
    rankings = build_rankings(processed)

    print("4/5 Saving analytics outputs...")
    save_processed_csv(processed, processed_path)
    save_processed_csv(processed, dashboard_path)
    save_processed_csv(rankings, rankings_path)
    load_sqlite(processed, db_path)

    print("5/5 Complete")
    print("")
    print(f"Processed dataset: {processed_path}")
    print(f"Dashboard export:  {dashboard_path}")
    print(f"SQLite database:   {db_path}")
    print(f"Quality report:    {quality_path}")


if __name__ == "__main__":
    main()
