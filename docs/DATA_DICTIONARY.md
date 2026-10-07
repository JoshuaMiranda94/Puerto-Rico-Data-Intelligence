# Data Dictionary

| Field | Type | Description |
|---|---|---|
| `geoid` | text | Census geographic identifier formed from state + municipality FIPS |
| `state_fips` | text | Puerto Rico state FIPS (`72`) |
| `municipality_fips` | text | Census county-equivalent code for the municipality |
| `municipality` | text | Clean municipality name |
| `population` | integer | ACS estimate of total population |
| `median_household_income` | numeric | ACS median household income estimate |
| `civilian_labor_force` | integer | Civilian labor force estimate |
| `unemployed` | integer | Unemployed population estimate |
| `unemployment_rate` | numeric | `unemployed / civilian_labor_force * 100` |
| `population_rank` | integer | Rank by population, descending |
| `income_rank` | integer | Rank by median household income, descending |
| `unemployment_rank` | integer | Rank by unemployment rate, descending |
| `source_year` | integer | ACS dataset year |
| `source_name` | text | Data source label |

## Important interpretation note

ACS values are survey estimates. They should not be interpreted as exact administrative counts. A production extension should also bring in margins of error where decision-making requires uncertainty analysis.
