import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

df2009 = pd.read_csv("data/Retail 2009-10.csv")
df2010 = pd.read_csv("data/Retail 2010-11.csv")

df = pd.concat([df2009, df2010], ignore_index=True)

clean_df = df.copy()
raw_df = df.copy()

clean_df["Description"] = clean_df["Description"].fillna("Unknown")

clean_df["InvoiceDate"] = pd.to_datetime(
    clean_df["InvoiceDate"],
    format="mixed",
    errors="coerce"
)

clean_df["Customer ID"] = pd.to_numeric(
    clean_df["Customer ID"],
    errors="coerce"
).astype("Int64")

clean_df = clean_df.dropna(subset=["Description"])
clean_df = clean_df.dropna(subset=["Customer ID"])

clean_df = clean_df.drop_duplicates()

clean_df["Revenue"] = clean_df["Quantity"] * clean_df["Price"]

clean_df["Year"] = clean_df["InvoiceDate"].dt.year

customer = (
    clean_df[["Customer ID", "Country"]]
    .drop_duplicates(subset=["Customer ID"])
)

products = (
    clean_df[["StockCode", "Description"]]
    .drop_duplicates(subset=["StockCode"])
)

invoices = (
    clean_df[["Invoice", "InvoiceDate", "Customer ID"]]
    .drop_duplicates(subset=["Invoice"])
)

transactions = clean_df[
    ["Invoice", "StockCode", "Quantity", "Price", "Revenue"]
].copy()

transactions.insert(
    0,
    "Transaction ID",
    range(1, len(transactions) + 1)
)

password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/Prueba"
)

with engine.connect() as conexion:
    print("¡Conexión exitosa con PostgreSQL!")

customer.to_sql(
    "customer",
    con=engine,
    if_exists="append",
    index=False
)

products.to_sql(
    "products",
    con=engine,
    if_exists="append",
    index=False
)

invoices.to_sql(
    "invoices",
    con=engine,
    if_exists="append",
    index=False
)

transactions.to_sql(
    "transactions",
    con=engine,
    if_exists="append",
    index=False
)

print("Proceso ETL completado correctamente.")
