
# Data Quality Report
## Morocco Agricultural Production Dataset (2010–2022)

### 1. Dataset Overview
- Original rows: 14,690
- Columns: 5
- Source format: Excel
- Indicators:
  - Production-T (Tonnes)
  - Superficie (Ha)

### 2. Data Quality Checks

| Check | Result |
|---|---:|
| Missing values | 0 |
| Extra spaces | 0 |
| Non-numeric values | 0 |
| Negative values | 0 |
| Zero values | 14 |
| Exact duplicate rows | 1,148 |

### 3. Cleaning Operations
- Cleaned column names.
- Removed extra spaces from text values.
- Converted Valeur to numeric.
- Removed exact duplicate rows.
- Preserved zero values for further investigation.

### 4. Final Dataset
- Original rows: 14,690
- Final rows: 13,542
- Removed exact duplicates: 1,148
- Remaining exact duplicates: 0
- Missing values after cleaning: 0

### 5. Notes
Zero values were preserved because they may represent valid
observations. Their meaning should be confirmed with the data source.

The dataset also requires further investigation of its data
granularity across different years before aggregation or analysis.

### 6. Data Granularity Limitation

A significant difference in data granularity was identified
in the 2020/2021 and 2021/2022 agricultural seasons.

Unlike previous seasons, these two seasons contain multiple
records for the same product and indicator.

Key observations:
- 2019/2020 generally contains one record per product and indicator.
- 2020/2021 and 2021/2022 contain multiple records for the
  same product and indicator.
- The source dataset does not provide additional dimensions
  explaining these records.
- No evidence confirms that these records represent regional
  or provincial data.

Data handling decisions:
- All non-exact-duplicate observations are preserved.
- No arbitrary aggregation is applied.
- No geographical dimension is assumed.
- Yield calculations and direct comparisons involving these
  two seasons are avoided until the data granularity is clarified.

This limitation must be considered when interpreting analytical
results and designing visualizations.
