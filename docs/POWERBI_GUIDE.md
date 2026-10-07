# Power BI Dashboard Guide

Use:

`data/exports/pr_dashboard_dataset.csv`

as the main Power BI table.

## Page 1 — Executive Overview

Recommended cards:

- Total population represented
- Average municipality median household income
- Average municipality unemployment rate
- Number of municipalities

Recommended visuals:

- Top 10 municipalities by population
- Highest / lowest median household income
- Highest unemployment rate
- Puerto Rico municipality map

## Page 2 — Municipality Comparison

Use a slicer for municipality.

Suggested visuals:

- Population
- Median household income
- Unemployment rate
- Population rank
- Income rank
- Unemployment rank

## Page 3 — Income & Labor Market

Suggested visuals:

- Scatter: median household income vs unemployment rate
- Bubble size: population
- Bar chart: unemployment rate by municipality
- Table with conditional formatting

## Page 4 — Geographic View

Use `geoid` or municipality name with Puerto Rico context.

For a future geospatial upgrade, add official municipality boundary GeoJSON and use Shape Map or Azure Maps.

## Suggested visual design

Keep it professional and recruiter-friendly:

- one clear title per page
- limited number of KPIs
- consistent number formatting
- explain data source and ACS year
- include a small methodology note
