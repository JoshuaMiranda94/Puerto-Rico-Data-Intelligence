from __future__ import annotations

import pandas as pd


NUMERIC_COLUMNS = [
    "population",
    "median_household_income",
    "civilian_labor_force",
    "unemployed",
]


def clean_municipality_name(value: str) -> str:
    text = str(value)
    text = text.replace(" Municipio, Puerto Rico", "")
    text = text.replace(", Puerto Rico", "")
    return text.strip()


def transform_municipality_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    for column in NUMERIC_COLUMNS:
        result[column] = pd.to_numeric(result[column], errors="coerce")

    result["municipality"] = result["municipality_name"].map(clean_municipality_name)

    denominator = result["civilian_labor_force"].replace(0, pd.NA)
    result["unemployment_rate"] = (
        result["unemployed"] / denominator * 100
    ).round(2)

    result["population_rank"] = (
        result["population"].rank(method="min", ascending=False).astype("Int64")
    )
    result["income_rank"] = (
        result["median_household_income"]
        .rank(method="min", ascending=False)
        .astype("Int64")
    )
    result["unemployment_rank"] = (
        result["unemployment_rate"]
        .rank(method="min", ascending=False)
        .astype("Int64")
    )

    result["geoid"] = (
        result["state_fips"].astype(str).str.zfill(2)
        + result["municipality_fips"].astype(str).str.zfill(3)
    )

    keep = [
        "geoid",
        "state_fips",
        "municipality_fips",
        "municipality",
        "population",
        "median_household_income",
        "civilian_labor_force",
        "unemployed",
        "unemployment_rate",
        "population_rank",
        "income_rank",
        "unemployment_rank",
        "source_year",
        "source_name",
    ]

    result = result[keep].sort_values("municipality").reset_index(drop=True)
    return result


def build_rankings(df: pd.DataFrame) -> pd.DataFrame:
    rankings = df[
        [
            "municipality",
            "population",
            "median_household_income",
            "unemployment_rate",
            "population_rank",
            "income_rank",
            "unemployment_rank",
        ]
    ].copy()
    return rankings.sort_values("population_rank").reset_index(drop=True)
