# Puerto Rico Data Intelligence

A portfolio-ready data analytics project that turns official Puerto Rico municipality data into a reproducible analytics pipeline, SQLite database, dashboard-ready exports, and executive insights.

## Why this project

Puerto Rico data is often spread across multiple public sources and is not always presented in a way that is easy to compare municipality by municipality. This project creates a clean analytical layer for exploring population, household income, employment, unemployment, and related indicators.

The project is designed to demonstrate practical skills in:

- Python data extraction and transformation
- API integration
- data quality validation
- SQL analytics
- reproducible ETL pipelines
- dashboard-ready data modeling
- business-style reporting
- testing and documentation

## Data source

The starter pipeline uses the **U.S. Census Bureau American Community Survey (ACS) 5-Year API** for Puerto Rico municipality-level data.

Puerto Rico uses state FIPS code `72`, and municipalities are represented as county-equivalent geographies in Census data.

Default dataset:

`2024 ACS 5-Year`

Core variables used:

| Variable | Meaning |
|---|---|
| `B01003_001E` | Total population |
| `B19013_001E` | Median household income |
| `B23025_003E` | Civilian labor force |
| `B23025_005E` | Unemployed population |

The pipeline calculates unemployment rate from the labor-force fields instead of storing it as a hard-coded value.

## Architecture

```text
Census ACS API
      |
      v
Extract raw municipality data
      |
      v
Data quality checks
      |
      v
Transform + KPI calculations
      |
      +----------------------+
      |                      |
      v                      v
Processed CSV           SQLite database
      |                      |
      +----------+-----------+
                 |
                 v
        Dashboard-ready exports
                 |
                 v
       SQL / Power BI / analysis
```

## Repository structure

```text
Puerto-Rico-Data-Intelligence/
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── POWERBI_GUIDE.md
│   └── PROJECT_STORY.md
├── reports/
│   └── EXECUTIVE_SUMMARY_TEMPLATE.md
├── scripts/
│   └── run_pipeline.py
├── sql/
│   └── analysis_queries.sql
├── src/
│   └── pr_data_intelligence/
│       ├── __init__.py
│       ├── extract.py
│       ├── quality.py
│       ├── transform.py
│       └── load.py
├── tests/
│   ├── test_quality.py
│   └── test_transform.py
├── ATTRIBUTION.md
├── requirements.txt
└── README.md
```

## Quick start

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python scripts/run_pipeline.py
```

Expected outputs:

```text
data/raw/acs_pr_municipalities_raw.csv
data/processed/pr_municipality_indicators.csv
data/exports/pr_dashboard_dataset.csv
data/exports/municipality_rankings.csv
data/pr_data_intelligence.sqlite
reports/data_quality_report.json
```

Run tests:

```bash
pytest -q
```

## KPIs

The processed dataset includes:

- population
- median household income
- civilian labor force
- unemployed population
- unemployment rate
- population rank
- income rank
- unemployment rank

## Example SQL questions

The included SQL file answers questions such as:

- Which municipalities have the highest population?
- Which municipalities have the highest median household income?
- Which municipalities have the highest unemployment rate?
- Which municipalities combine large population with above-average unemployment?
- How do municipalities compare with Puerto Rico-wide averages?

## Power BI

`docs/POWERBI_GUIDE.md` explains a suggested dashboard with:

1. Executive overview
2. Municipality comparison
3. Income and labor-market analysis
4. Map view
5. Detail table with rankings

The export in `data/exports/pr_dashboard_dataset.csv` is designed to be loaded directly into Power BI.

## Portfolio direction

This repository is intentionally structured as a professional analytics project rather than as a course lab. Future versions can add additional official sources for tourism, housing, energy, education, and economic activity while preserving the same quality-gated pipeline.

## Author

Joshua Miranda  
Data Analytics | Artificial Intelligence | Python | SQL | Power BI
