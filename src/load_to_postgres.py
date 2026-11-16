import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Read database credentials from .env
load_dotenv()

# 2. Build database connection
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

engine = create_engine(connection_url)

# 3. Read cleaned CSV file
csv_file = "data/processed/production_vegetale_clean.csv"
df = pd.read_csv(csv_file)

print("Rows to load:", len(df))

# 4. Load data into PostgreSQL
df.to_sql(
    name="stg_crop_indicators",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")

# 5. Verify loaded rows
with engine.connect() as connection:
    result = connection.exec_driver_sql(
        "SELECT COUNT(*) FROM stg_crop_indicators"
    )
    print("Rows in PostgreSQL:", result.scalar())

engine.dispose()
