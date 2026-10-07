from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests


DEFAULT_YEAR = 2024
STATE_FIPS_PR = "72"

ACS_VARIABLES = {
    "NAME": "municipality_name",
    "B01003_001E": "population",
    "B19013_001E": "median_household_income",
    "B23025_003E": "civilian_labor_force",
    "B23025_005E": "unemployed",
}


@dataclass(frozen=True)
class CensusConfig:
    year: int = DEFAULT_YEAR
    state_fips: str = STATE_FIPS_PR
    timeout_seconds: int = 30

    @property
    def endpoint(self) -> str:
        return f"https://api.census.gov/data/{self.year}/acs/acs5"


def build_params(config: CensusConfig) -> dict[str, str]:
    return {
        "get": ",".join(ACS_VARIABLES.keys()),
        "for": "county:*",
        "in": f"state:{config.state_fips}",
    }


def fetch_acs_municipalities(
    config: CensusConfig | None = None,
    session: requests.Session | None = None,
) -> pd.DataFrame:
    config = config or CensusConfig()
    client = session or requests.Session()

    response = client.get(
        config.endpoint,
        params=build_params(config),
        timeout=config.timeout_seconds,
    )
    response.raise_for_status()
    payload = response.json()

    if not payload or len(payload) < 2:
        raise ValueError("Census API returned no municipality rows.")

    header, *rows = payload
    df = pd.DataFrame(rows, columns=header)

    rename_map = {k: v for k, v in ACS_VARIABLES.items() if k in df.columns}
    df = df.rename(columns=rename_map)

    if "county" in df.columns:
        df = df.rename(columns={"county": "municipality_fips"})
    if "state" in df.columns:
        df = df.rename(columns={"state": "state_fips"})

    df["source_year"] = config.year
    df["source_name"] = "US Census Bureau ACS 5-Year"
    return df


def save_raw(df: pd.DataFrame, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
