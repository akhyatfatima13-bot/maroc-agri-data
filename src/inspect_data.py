from pathlib import Path
import pandas as pd

# 1. تحديد مكان ملف Excel
data_folder = Path("data/raw")

# 2. البحث عن ملف Excel
excel_files = list(data_folder.glob("*.xlsx"))

# 3. التأكد من وجود الملف
if not excel_files:
    print("No Excel file found!")
else:
    file_path = excel_files[0]

    # 4. قراءة أسماء Sheets
    excel = pd.ExcelFile(file_path)

    print("Excel file:", file_path.name)
    print("Sheets:", excel.sheet_names)

    # 5. عرض أول 5 أسطر من كل Sheet
    for sheet in excel.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet)

        print("\nSheet:", sheet)
        print("Columns:", df.columns.tolist())
        print(df.head())
        print("\n--- DATA INFORMATION ---")
        df.info()

        print("\n--- MISSING VALUES ---")
        print(df.isna().sum())

        print("\n--- UNIQUE PERIODS ---")
        print(df["Occurrence"].unique())

        print("\n--- UNIQUE INDICATORS ---")
        print(df["Indicateur"].unique())

        print("\n--- UNIQUE CATEGORIES ---")
        print(df["Filière"].unique())

        print("\n--- NUMBER OF PRODUCTS ---")
        print(df["Produit"].nunique()) 
        print("\n--- DUPLICATE ROWS ---")
        print("Exact duplicates:", df.duplicated().sum())

        print("\n--- DUPLICATE RECORDS ---")
        print(
            df.duplicated(
                subset=["Occurrence", "Filière", "Produit", "Indicateur"]
            ).sum()
        )

        print("\n--- VALUE STATISTICS ---")
        print(df[" Valeur"].describe())

        print("\n--- NEGATIVE VALUES ---")
        print((df[" Valeur"] < 0).sum())

        print("\n--- INDICATOR COUNTS ---")
        print(df["Indicateur"].value_counts())
  
        # Define the columns that identify a record
        key_columns = [
            "Occurrence",
            "Filière",
            "Produit",
            "Indicateur"
        ]

        # Find all records with repeated keys
        duplicates = df[
            df.duplicated(subset=key_columns, keep=False)
        ]

        print("\n--- REPEATED RECORDS EXAMPLES ---")
        print(
            duplicates.sort_values(key_columns)
            .head(20)
            .to_string(index=False)
        )

        # Count how many groups have repeated keys
        print("\n--- REPEATED GROUPS ---")
        print(
            duplicates.groupby(key_columns).ngroups
        )

        # Check if repeated records have different values
        print("\n--- DIFFERENT VALUES IN REPEATED RECORDS ---")
        print(
            duplicates.groupby(key_columns)[" Valeur"]
            .nunique()
            .value_counts()
        )

        # Show the most repeated records
        print("\n--- MOST REPEATED RECORDS ---")
        print(
            duplicates.groupby(key_columns)
            .size()
            .sort_values(ascending=False)
            .head(10)
        )
        # Inspect one repeated product and period
        example = df[
            (df["Occurrence"] == "2020/2021") &
            (df["Filière"] == "Agrumes") &
            (df["Produit"] == "Autres agrumes")
        ]

        print("\n--- AUTRES AGRUMES: 2020/2021 ---")
        print(example.to_string(index=True))
        # Inspect exact duplicate rows
        exact_duplicates = df[
            df.duplicated(keep=False)
        ]

        print("\n--- EXACT DUPLICATES EXAMPLES ---")
        print(exact_duplicates.head(20).to_string(index=True))

        print("\nTotal exact duplicate rows:", len(exact_duplicates))
        # Select one row to investigate
        sample_row = df.loc[2192]

        # Find all rows identical to this row
        matching_rows = df[
            df.eq(sample_row).all(axis=1)
        ]

        print("\n--- INVESTIGATING ONE DUPLICATE ---")
        print(matching_rows.to_string(index=True))

        print("Number of identical rows:", len(matching_rows))
# Inspect original Excel workbook structure
import openpyxl

workbook = openpyxl.load_workbook(
    file_path,
    data_only=False
)

print("\n--- WORKBOOK STRUCTURE ---")

for sheet in workbook.worksheets:
    print("Sheet:", sheet.title)
    print("Dimensions:", sheet.max_row, "rows x", sheet.max_column, "columns")
    print("Hidden sheet:", sheet.sheet_state)
    print("Hidden rows:", [
        i for i, row in sheet.row_dimensions.items()
        if row.hidden
    ][:20])
    print("Hidden columns:", [
        col for col, dimension in sheet.column_dimensions.items()
        if dimension.hidden
    ])
    print("Merged cells:", list(sheet.merged_cells.ranges)[:20])
# Inspect rows around repeated records
print("\n--- ORIGINAL ROWS AROUND DUPLICATE ---")

print(
    df.loc[2185:2200].to_string(index=True)
)

print("\n--- ORIGINAL ROWS AROUND SECOND OCCURRENCE ---")

print(
    df.loc[5245:5260].to_string(index=True)
)
print("\n--- EXACT DUPLICATES BY YEAR ---")

exact_duplicates = df[df.duplicated(keep=False)]

print(
    exact_duplicates.groupby("Occurrence")
    .size()
    .sort_index()
)

print("\n--- DUPLICATE GROUPS BY YEAR ---")

duplicate_groups = (
    df[df.duplicated(
        subset=["Occurrence", "Filière", "Produit", "Indicateur"],
        keep=False
    )]
    .groupby("Occurrence")
    .size()
)

print(duplicate_groups.sort_index())
print("\n--- ROW COUNT BY YEAR ---")

print(
    df.groupby("Occurrence")
    .size()
    .sort_index()
)

print("\n--- UNIQUE PRODUCTS BY YEAR ---")

print(
    df.groupby("Occurrence")["Produit"]
    .nunique()
    .sort_index()
)

print("\n--- UNIQUE CATEGORIES BY YEAR ---")

print(
    df.groupby("Occurrence")["Filière"]
    .nunique()
    .sort_index()
)
print("\n--- OLIVIER PRODUCTION 2020/2021 ---")

olivier = df[
    (df["Occurrence"] == "2020/2021") &
    (df["Produit"] == "Olivier") &
    (df["Indicateur"] == "Production-T (Tonnes)")
]

print("Number of records:", len(olivier))
print(olivier.head(20).to_string(index=True))

print("\n--- OLIVIER PRODUCTION VALUE COUNTS ---")

print(
    olivier[" Valeur"]
    .value_counts()
    .head(10)
)
print("\n--- OLIVIER RECORDS BY YEAR ---")

olivier_all = df[
    (df["Produit"] == "Olivier") &
    (df["Indicateur"] == "Production-T (Tonnes)")
]

print(
    olivier_all.groupby("Occurrence")
    .agg(
        number_of_records=(" Valeur", "size"),
        different_values=(" Valeur", "nunique"),
        total_value=(" Valeur", "sum")
    )
    .to_string()
)
print("\n--- RECORD COUNTS BY PRODUCT AND YEAR ---")

selected_products = [
    "Olivier",
    "Blé tendre",
    "Figuier",
    "Orange",
]

for product in selected_products:

    product_data = df[
        (df["Produit"] == product) &
        (df["Indicateur"] == "Production-T (Tonnes)")
    ]

    print(f"\nProduct: {product}")

    print(
        product_data.groupby("Occurrence")
        .size()
        .to_string()
    )
print("\n--- PRODUCTS CONTAINING ORANG ---")

print(
    df[
        df["Produit"].str.contains(
            "orang",
            case=False,
            na=False
        )
    ]["Produit"]
    .drop_duplicates()
    .to_list()
)
print("\n--- ALL EXCEL HEADERS ---")

print(df.columns.tolist())
print("\n--- BLE TENDRE: 2019/2020 ---")

print(
    df[
        (df["Occurrence"] == "2019/2020") &
        (df["Produit"] == "Blé tendre")
    ].to_string(index=True)
)

print("\n--- BLE TENDRE: 2020/2021 ---")

print(
    df[
        (df["Occurrence"] == "2020/2021") &
        (df["Produit"] == "Blé tendre")
    ].head(15).to_string(index=True)
)
print("\n--- BLE TENDRE: YEAR COMPARISON ---")

ble = df[
    df["Produit"] == "Blé tendre"
]

comparison = (
    ble.groupby(["Occurrence", "Indicateur"])
    .agg(
        number_of_records=(" Valeur", "size"),
        unique_values=(" Valeur", "nunique"),
        total_value=(" Valeur", "sum"),
        minimum=(" Valeur", "min"),
        maximum=(" Valeur", "max")
    )
)

print(comparison.to_string())
