import pandas as pd

from pr_data_intelligence.transform import transform_municipality_data


def test_transform_calculates_unemployment_and_geoid():
    raw = pd.DataFrame(
        {
            "municipality_name": ["Example Municipio, Puerto Rico"],
            "population": ["1000"],
            "median_household_income": ["25000"],
            "civilian_labor_force": ["500"],
            "unemployed": ["50"],
            "municipality_fips": ["001"],
            "state_fips": ["72"],
            "source_year": [2024],
            "source_name": ["US Census Bureau ACS 5-Year"],
        }
    )

    result = transform_municipality_data(raw)

    assert result.loc[0, "municipality"] == "Example"
    assert result.loc[0, "unemployment_rate"] == 10.0
    assert result.loc[0, "geoid"] == "72001"
