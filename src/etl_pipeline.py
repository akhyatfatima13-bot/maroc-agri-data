
from pathlib import Path
import pandas as pd


def extract_data():
    """Read the original Excel dataset."""

    data_folder = Path("data/raw")
    excel_files = list(data_folder.glob("*.xlsx"))

    if not excel_files:
        raise FileNotFoundError("No Excel file found")

    df = pd.read_excel(excel_files[0])

    print("EXTRACT completed")
    print("Rows extracted:", len(df))

    return df


def transform_data(df):
    """Clean and validate the dataset."""

    df = df.copy()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean text values
    text_columns = df.select_dtypes(
        include=["object", "str"]
    ).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Convert Valeur to numeric
    df["Valeur"] = pd.to_numeric(
        df["Valeur"],
        errors="coerce"
    )

    # Remove rows with invalid numeric values
    df = df.dropna(subset=["Valeur"])

    # Remove exact duplicates
    df = df.drop_duplicates()

    print("TRANSFORM completed")
    print("Rows after transformation:", len(df))

    return df


def load_data(df):
    """Save the transformed dataset as CSV."""

    output_folder = Path("data/processed")
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "production_vegetale_clean.csv"

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print("LOAD completed")
    print("File saved:", output_file)


def main():
    df = extract_data()
    df_clean = transform_data(df)
    load_data(df_clean)

    print("\nETL PIPELINE FINISHED SUCCESSFULLY")


if __name__ == "__main__":
    main()
