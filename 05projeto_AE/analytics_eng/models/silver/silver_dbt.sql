-- models/silver_dbt.sql

SELECT
    adult,
    budget,
    id,
    imdb_id,
    original_language,
    original_title,
    overview,
    popularity,
    release_date,
    revenue,
    runtime,
    status,
    title,
    video,
    vote_average,
    vote_count
FROM public.bronze_dbt
WHERE release_date IS NOT NULL
AND vote_count IS NOT NULL
AND vote_average IS NOT NULL
AND popularity IS NOT NULL