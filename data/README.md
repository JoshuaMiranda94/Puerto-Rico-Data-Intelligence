# Data Folders

This repository does not commit generated Census extracts by default.

Run:

```bash
python scripts/run_pipeline.py
```

to create:

- `raw/acs_pr_municipalities_raw.csv`
- `processed/pr_municipality_indicators.csv`
- `exports/pr_dashboard_dataset.csv`
- `exports/municipality_rankings.csv`
- `pr_data_intelligence.sqlite`

This keeps the project reproducible and avoids presenting stale generated data as current.
