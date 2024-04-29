-- models/gold_dbt.sql

WITH revenue_budget AS (
    SELECT
        EXTRACT(YEAR FROM CAST(release_date AS DATE)) AS year,
        AVG(CAST(budget AS NUMERIC)) AS avg_budget,  -- Cast budget to numeric before averaging
        AVG(CAST(revenue AS NUMERIC)) AS avg_revenue,  -- Cast revenue to numeric if needed
        (AVG(CAST(revenue AS NUMERIC)) - AVG(CAST(budget AS NUMERIC))) AS avg_profit  -- Calculate profit
    FROM public.silver_dbt
    GROUP BY 1
)

SELECT
    year,
    avg_revenue,
    avg_budget,
    avg_revenue - avg_budget AS avg_profit
FROM revenue_budget
ORDER BY year