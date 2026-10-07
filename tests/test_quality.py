import pandas as pd

from pr_data_intelligence.quality import run_quality_checks


def test_quality_passes_clean_data():
    raw = pd.DataFrame(
        {
            "municipality_name": ["Example Municipio, Puerto Rico"],
            "population": ["1000"],
            "median_household_income": ["25000"],
            "civilian_labor_force": ["500"],
            "unemployed": ["50"],
            "municipality_fips": ["001"],
            "state_fips": ["72"],
        }
    )

    result = run_quality_checks(raw)

    assert result.passed is True
    assert result.row_count == 1
    assert result.duplicate_fips == 0
