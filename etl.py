import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

df = pd.read_csv("data/Retail 2009-10.csv")

print(df)

df2 = pd.read_csv("data/Retail 2010-11.csv")

print(df2)