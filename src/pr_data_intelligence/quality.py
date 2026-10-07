from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable
import json
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "municipality_name",
    "population",
    "median_household_income",
    "civilian_labor_force",
    "unemployed",
    "municipality_fips",
    "state_fips",
]


@dataclass
class QualityResult:
    passed: bool
    row_count: int
    duplicate_fips: int
    missing_required_values: int
    negative_numeric_values: int
    invalid_state_fips: int

    def to_dict(self) -> dict:
        return asdict(self)


def validate_schema(df: pd.DataFrame) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def run_quality_checks(df: pd.DataFrame) -> QualityResult:
    validate_schema(df)

    numeric_columns = [
        "population",
        "median_household_income",
        "civilian_labor_force",
        "unemployed",
    ]

    numeric = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    missing_required_values = int(df[REQUIRED_COLUMNS].isna().sum().sum())
    duplicate_fips = int(df["municipality_fips"].duplicated().sum())
    negative_numeric_values = int((numeric < 0).sum().sum())
    invalid_state_fips = int((df["state_fips"].astype(str) != "72").sum())

    passed = all(
        value == 0
        for value in [
            duplicate_fips,
            missing_required_values,
            negative_numeric_values,
            invalid_state_fips,
        ]
    )

    return QualityResult(
        passed=passed,
        row_count=len(df),
        duplicate_fips=duplicate_fips,
        missing_required_values=missing_required_values,
        negative_numeric_values=negative_numeric_values,
        invalid_state_fips=invalid_state_fips,
    )


def write_quality_report(result: QualityResult, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")
    return path
