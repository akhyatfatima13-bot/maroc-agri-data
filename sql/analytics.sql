-- 1. Total agricultural production by season
-- Excluding seasons with unclear data granularity

SELECT
    s.season_name,
    ROUND(SUM(f.value), 2) AS total_production_tonnes
FROM fact_crop_observation f
JOIN dim_season s
    ON f.season_id = s.season_id
JOIN dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_name = 'Production-T (Tonnes)'
  AND s.season_name NOT IN ('2020/2021', '2021/2022')
GROUP BY s.season_name
ORDER BY s.season_name;
-- 2. Total production by agricultural category
-- Excluding seasons with unclear data granularity

SELECT
    c.category_name,
    ROUND(SUM(f.value), 2) AS total_production_tonnes
FROM fact_crop_observation f
JOIN dim_category c
    ON f.category_id = c.category_id
JOIN dim_indicator i
    ON f.indicator_id = i.indicator_id
JOIN dim_season s
    ON f.season_id = s.season_id
WHERE i.indicator_name = 'Production-T (Tonnes)'
  AND s.season_name NOT IN ('2020/2021', '2021/2022')
GROUP BY c.category_name
ORDER BY total_production_tonnes DESC;
