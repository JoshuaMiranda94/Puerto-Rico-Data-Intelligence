from __future__ import annotations

from pathlib import Path
import sqlite3

import pandas as pd


TABLE_NAME = "municipality_indicators"


def save_processed_csv(df: pd.DataFrame, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def load_sqlite(
    df: pd.DataFrame,
    database_path: str | Path,
    table_name: str = TABLE_NAME,
) -> Path:
    database_path = Path(database_path)
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(database_path) as connection:
        df.to_sql(table_name, connection, if_exists="replace", index=False)
        connection.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{table_name}_municipality "
            f"ON {table_name}(municipality)"
        )
        connection.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{table_name}_geoid "
            f"ON {table_name}(geoid)"
        )

    return database_path
