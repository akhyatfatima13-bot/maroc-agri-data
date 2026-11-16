# Morocco Agricultural Production Data Warehouse

## Project Overview

This project focuses on building a Data Warehouse and
analytical platform for agricultural production data in Morocco.

The project uses historical agricultural data covering
12 agricultural seasons, from 2010/2011 to 2021/2022.

The main objective is to transform raw agricultural data
into structured and reliable information that can support
data analysis and business intelligence.

The solution follows a data engineering workflow:
- Data Extraction
- Data Cleaning and Transformation
- Data Loading
- Data Warehouse Modeling
- SQL Analytics
- Data Visualization

## Project Objectives

- Build an end-to-end ETL pipeline using Python and Pandas.
- Design a relational Data Warehouse using PostgreSQL.
- Organize agricultural data using a dimensional model.
- Perform analytical queries using SQL.
- Develop an interactive dashboard using Power BI.
## Dataset Description

The dataset is provided by the Moroccan Open Data Portal.

**Source:** [Production végétale 2010–2022](https://data.gov.ma/data/dataset/production-vegetale-2010-2022)

The original Excel dataset contains:
- 14,690 rows.
- 5 columns.
- 14 agricultural categories.
- 115 distinct product names.
- 12 agricultural seasons (2010/2011–2021/2022).

### Main Data Fields

| Column | Description |
|---|---|
| Occurrence | Agricultural season |
| Filière | Agricultural category |
| Produit | Agricultural product |
| Indicateur | Production or cultivated area |
| Valeur | Numerical observation |

## Technologies Used

- **Python:** Data processing and ETL development.
- **Pandas:** Data cleaning and transformation.
- **PostgreSQL:** Data Warehouse storage.
- **SQL:** Data analysis and querying.
- **Power BI:** Data visualization (planned).
- **Git & GitHub:** Version control and project documentation.

## Data Engineering Architecture

The project follows an end-to-end data engineering architecture:

```text
Excel Source
     |
     v
Python / Pandas ETL
     |
     v
Data Cleaning & Transformation
     |
     v
Processed CSV
     |
     v
PostgreSQL Staging Table
     |
     v
Data Warehouse
     |
     v
SQL Analytics
     |
     v
Power BI Dashboard
```

## ETL Pipeline

The ETL pipeline was developed using Python and Pandas.

### 1. Extract
- Read the original Excel dataset.
- Extract data from the `Feuil1` worksheet.
- Load 14,690 original records.

### 2. Transform
- Clean column names.
- Remove unnecessary spaces.
- Convert numerical values into numeric format.
- Identify and remove exact duplicate records.
- Preserve zero values for further investigation.

### 3. Load
- Export the cleaned dataset into CSV format.
- Load the processed data into PostgreSQL.
- Store the records in the staging table.
- Populate the Data Warehouse dimension and fact tables.

### ETL Results

| Metric | Result |
|---|---:|
| Original records | 14,690 |
| Clean records | 13,542 |
| Removed duplicates | 1,148 |
| Missing values | 0 |
| Negative values | 0 |
| Zero values preserved | 14 |

## Data Warehouse Design

The Data Warehouse uses a dimensional modeling approach.

It contains four dimension tables and one fact table.

### Dimension Tables

- `dim_season`: Stores agricultural seasons.
- `dim_category`: Stores agricultural categories.
- `dim_product`: Stores agricultural products and their categories.
- `dim_indicator`: Stores indicators and their measurement units.

### Fact Table

- `fact_crop_observation`: Stores agricultural observations and foreign keys referencing the dimensions.

### Database Structure

| Table | Number of Records |
|---|---:|
| dim_season | 12 |
| dim_category | 14 |
| dim_product | 116 |
| dim_indicator | 2 |
| fact_crop_observation | 13,542 |
| stg_crop_indicators | 13,542 |

The product dimension contains 116 product-category combinations because the product `Féverole` belongs to two different categories.

## SQL Analytics

SQL was used to perform analytical queries on the agricultural data.

The analyses include:

- Total agricultural production by season.
- Total production by agricultural category.
- Top 10 agricultural products by production.
- Total cultivated area by category.
- Number of distinct products by season.
- Distribution of observations by indicator.

### Key Analytical Findings

Based on the previously performed analysis:

- Fourragères is the category with the highest total production.
- Maraîchage and Céréales are among the leading production categories.
- Luzerne is the leading product in the previously calculated Top 10 ranking.
- Céréales has the highest accumulated cultivated area.

## Data Quality Limitations

A significant data granularity issue was identified in the last two agricultural seasons:

- 2020/2021
- 2021/2022

These seasons contain multiple records for the same product and indicator, unlike previous seasons.

The original dataset does not provide additional geographical or other dimensions explaining these observations.

Therefore:

- Non-identical observations are preserved.
- No geographical information is assumed.
- No arbitrary aggregation is performed.
- Yield calculations are avoided for these seasons.
- Direct comparisons involving these seasons require further investigation.

For the current season-based and category-based comparison, the analysis excludes 2020/2021 and 2021/2022.

Additional details are available in:

`docs/data_quality_report.md`

## Project Structure

```text
maroc-agri-data/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── clean_data.py
│   ├── etl_pipeline.py
│   └── load_to_postgres.py
│
├── sql/
│   ├── create_warehouse.sql
│   └── analytics.sql
│
├── notebooks/
│
├── docs/
│   └── data_quality_report.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Future Improvements

The following improvements are planned:

- Develop an interactive Power BI dashboard.
- Improve data documentation and analytical reporting.
- Publish the project on GitHub.
- Containerize the application using Docker.
- Improve the reproducibility of the ETL pipeline.

## Project Status

| Component | Status |
|---|---|
| Data extraction | Completed |
| Data cleaning | Completed |
| ETL pipeline | Completed |
| PostgreSQL staging | Completed |
| Data Warehouse modeling | Completed |
| Data loading | Completed |
| SQL Analytics | In progress |
| Power BI Dashboard | Planned |
| GitHub publication | Planned |
| Docker integration | Planned |
