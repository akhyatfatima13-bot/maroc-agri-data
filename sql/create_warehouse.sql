-- 1. Season dimension
CREATE TABLE dim_season (
    season_id SERIAL PRIMARY KEY,
    season_name VARCHAR(20) UNIQUE NOT NULL
);

-- 2. Category dimension
CREATE TABLE dim_category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

-- 3. Product dimension
CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category_id INTEGER REFERENCES dim_category(category_id),
    UNIQUE (product_name, category_id)
);

-- 4. Indicator dimension
CREATE TABLE dim_indicator (
    indicator_id SERIAL PRIMARY KEY,
    indicator_name VARCHAR(100) UNIQUE NOT NULL,
    unit VARCHAR(30)
);

-- 5. Central fact table
CREATE TABLE fact_crop_observation (
    fact_id SERIAL PRIMARY KEY,
    season_id INTEGER REFERENCES dim_season(season_id),
    product_id INTEGER REFERENCES dim_product(product_id),
    category_id INTEGER REFERENCES dim_category(category_id),
    indicator_id INTEGER REFERENCES dim_indicator(indicator_id),
    value NUMERIC(18, 4) NOT NULL
);
