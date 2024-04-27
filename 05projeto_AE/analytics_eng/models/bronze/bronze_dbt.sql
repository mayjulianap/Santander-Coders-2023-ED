{{ config(materialized='table') }}

select *
from public.raw_metadata