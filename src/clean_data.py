
from pathlib import Path
import pandas as pd

# ==========================================
# 1. LOCATE THE ORIGINAL EXCEL FILE
# ==========================================

data_folder = Path("data/raw")
excel_files = list(data_folder.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError("No Excel file found in data/raw")

excel_file = excel_files[0]

print("Excel file:", excel_file)


# ==========================================
# 2. READ THE ORIGINAL DATA
# ==========================================

df = pd.read_excel(excel_file)

print("\n--- ORIGINAL DATA ---")
print("Original rows:", len(df))
print("Original columns:", df.columns.tolist())


# ==========================================
# 3. CHECK EXTRA SPACES IN TEXT VALUES
# ==========================================

print("\n--- WHITESPACE CHECK ---")

text_columns = df.select_dtypes(include=["object", "str"]).columns

for column in text_columns:
    extra_spaces = df[column].ne(
        df[column].str.strip()
    ).sum()

    print(column, ":", extra_spaces)


# ==========================================
# 4. CLEAN COLUMN NAMES AND TEXT VALUES
# ==========================================

df.columns = df.columns.str.strip()

for column in text_columns:
    df[column] = df[column].str.strip()

print("\n--- CLEANED COLUMN NAMES ---")
print(df.columns.tolist())


# ==========================================
# 5. CHECK NUMERIC DATA
# ==========================================

print("\n--- NUMERIC DATA CHECK ---")

df["Valeur"] = pd.to_numeric(
    df["Valeur"],
    errors="coerce"
)

print("Data type:", df["Valeur"].dtype)

print(
    "Non-numeric values:",
    df["Valeur"].isna().sum()
)

print(
    "Negative values:",
    (df["Valeur"] < 0).sum()
)

print(
    "Zero values:",
    (df["Valeur"] == 0).sum()
)


# ==========================================
# 6. REMOVE EXACT DUPLICATES
# ==========================================

print("\n--- DUPLICATES CHECK ---")

duplicates_count = df.duplicated().sum()

print("Exact duplicates found:", duplicates_count)

df_clean = df.drop_duplicates().copy()

print("Rows after cleaning:", len(df_clean))
print("Removed rows:", len(df) - len(df_clean))


# ==========================================
# 7. SAVE CLEANED DATA
# ==========================================

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "production_vegetale_clean.csv"

df_clean.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("\nCleaned file saved:", output_file)


# ==========================================
# 8. VALIDATE THE PROCESSED DATA
# ==========================================

print("\n--- FINAL DATA VALIDATION ---")

check_df = pd.read_csv(output_file)

print("Processed rows:", len(check_df))
print("Processed columns:", check_df.columns.tolist())

print(
    "Remaining exact duplicates:",
    check_df.duplicated().sum()
)

print("\nMissing values:")
print(check_df.isna().sum())

print("\nData types:")
print(check_df.dtypes)

print("\n--- CLEANING COMPLETED ---")

