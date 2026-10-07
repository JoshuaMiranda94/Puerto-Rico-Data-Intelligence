-- Puerto Rico Data Intelligence
-- Municipality-level analytics queries

-- 1. Top municipalities by population
SELECT
    municipality,
    population,
    population_rank
FROM municipality_indicators
ORDER BY population DESC
LIMIT 10;


-- 2. Highest median household income
SELECT
    municipality,
    median_household_income,
    income_rank
FROM municipality_indicators
WHERE median_household_income IS NOT NULL
ORDER BY median_household_income DESC
LIMIT 10;


-- 3. Highest unemployment rate
SELECT
    municipality,
    civilian_labor_force,
    unemployed,
    unemployment_rate,
    unemployment_rank
FROM municipality_indicators
WHERE unemployment_rate IS NOT NULL
ORDER BY unemployment_rate DESC
LIMIT 10;


-- 4. Puerto Rico-wide municipality averages
SELECT
    ROUND(AVG(population), 0) AS avg_municipality_population,
    ROUND(AVG(median_household_income), 2) AS avg_median_household_income,
    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment_rate
FROM municipality_indicators;


-- 5. Large municipalities with above-average unemployment
WITH averages AS (
    SELECT
        AVG(population) AS avg_population,
        AVG(unemployment_rate) AS avg_unemployment_rate
    FROM municipality_indicators
)
SELECT
    m.municipality,
    m.population,
    m.unemployment_rate
FROM municipality_indicators AS m
CROSS JOIN averages AS a
WHERE m.population > a.avg_population
  AND m.unemployment_rate > a.avg_unemployment_rate
ORDER BY m.population DESC;


-- 6. Compare each municipality with the dataset average
WITH averages AS (
    SELECT
        AVG(median_household_income) AS avg_income,
        AVG(unemployment_rate) AS avg_unemployment
    FROM municipality_indicators
)
SELECT
    m.municipality,
    m.median_household_income,
    ROUND(m.median_household_income - a.avg_income, 2) AS income_vs_average,
    m.unemployment_rate,
    ROUND(m.unemployment_rate - a.avg_unemployment, 2) AS unemployment_vs_average
FROM municipality_indicators AS m
CROSS JOIN averages AS a
ORDER BY income_vs_average DESC;
