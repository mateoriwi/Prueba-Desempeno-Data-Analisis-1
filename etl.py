import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

df2009 = pd.read_csv("data/Retail 2009-10.csv")
df2010 = pd.read_csv("data/Retail 2010-11.csv")

df = pd.concat([df2009, df2010], ignore_index=True)

clean_df = df.copy()
raw_df = df.copy()

print("Nulos en el dataset")

print("Duplicados en el dataset")
print(clean_df.duplicated().sum())

print(df.shape)

clean_df["Description"] = clean_df["Description"].fillna("Unknown")

print(clean_df.dtypes)

clean_df["InvoiceDate"] = pd.to_datetime(
    clean_df["InvoiceDate"],
    format="mixed",
    errors="coerce"
)

clean_df['Customer ID'] = pd.to_numeric(clean_df['Customer ID'], errors='coerce').astype('Int64')

print(clean_df.dtypes)
print(clean_df.isnull().sum())
print(clean_df["InvoiceDate"])

print(clean_df[clean_df["Description"].isnull()])
print(clean_df[clean_df["Customer ID"] == "<NA>"])

## Se decide eliminar TODAS las filas con "Description" = NaN y "Customer ID" = <NA> ya que estas, tampoco tienen precio ni valor monetario


print(clean_df[(clean_df["Price"] > 0.0) & (clean_df["Description"].isna())])

clean_df = clean_df.dropna(subset=["Description"])

print(clean_df[(clean_df["Customer ID"].isna()) & (clean_df["Price"] == 0.0)])

clean_df = clean_df.dropna(subset=["Customer ID"])

clean_df = clean_df.drop_duplicates()

print(clean_df[clean_df["Price"] < 0])

print(clean_df[clean_df["Quantity"] < 0])

clean_df["Revenue"] = (clean_df["Quantity"]) * (clean_df["Price"])

print(clean_df)

clean_df['Year'] = clean_df['InvoiceDate'].dt.year

customer = clean_df[["Customer ID", "Country"]].drop_duplicates()

products = clean_df[["StockCode", "Description"]].drop_duplicates()

invoices = clean_df[["Invoice", "InvoiceDate", "Customer ID"]].drop_duplicates()

transactions = clean_df[["Invoice", "StockCode", "Quantity", "Price", "Revenue"]] 

transactions.insert(
    0,
    "TransactionID",
    range(1, len(transactions) + 1))

print(customer["Customer ID"].duplicated().sum())


print(
    products.groupby("StockCode")["Description"]
    .nunique()
    .sort_values(ascending=False)
    .head(20)
)


print(
    invoices.groupby("Invoice")["Customer ID"]
    .nunique()
    .sort_values(ascending=False)
    .head()
)


print(
    invoices.groupby("Invoice")["InvoiceDate"]
    .nunique()
    .sort_values(ascending=False)
    .head()
)


print(( transactions["Quantity"] * transactions["Price"] == transactions["Revenue"] ).all())

