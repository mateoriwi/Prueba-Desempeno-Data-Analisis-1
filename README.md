
# Proyecto de Data Analytics — Online Retail II

## Descripción

Proyecto de análisis y procesamiento de datos desarrollado para el análisis de información comercial del dataset Online Retail II.

El proyecto utiliza información de ventas de los archivos `Retail 2009-10.csv` y `Retail 2010-11.csv`, correspondientes a transacciones comerciales realizadas durante los períodos 2009-2010 y 2010-2011.

El flujo del proyecto consiste en extraer los datos desde archivos CSV, realizar limpieza y transformación mediante Python y Pandas, estructurar la información en diferentes tablas y cargar los datos procesados en PostgreSQL para su posterior análisis en Power BI.

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- PostgreSQL
- SQLAlchemy
- Psycopg2
- python-dotenv
- Power BI
- Git / GitHub

---

## Flujo del proyecto

```text
Retail 2009-10.csv ──┐
                     │
Retail 2010-11.csv ──┤
                     ▼
                  Pandas
                     │
                     ▼
          Limpieza y transformación
                     │
                     ▼
               Normalización
                     │
                     ▼
                PostgreSQL
                     │
                     ▼
                 Power BI
                     │
                     ▼
             Análisis de datos
```

---

## Dataset

El proyecto utiliza el dataset **Online Retail II**, dividido en dos archivos:

- `Retail 2009-10.csv`
- `Retail 2010-11.csv`

Ambos archivos son cargados mediante Pandas y posteriormente concatenados en un único DataFrame.

```python
df2009 = pd.read_csv("data/Retail 2009-10.csv")
df2010 = pd.read_csv("data/Retail 2010-11.csv")

df = pd.concat([df2009, df2010], ignore_index=True)
```

El dataset contiene información relacionada con:

- Facturas
- Productos
- Cantidades
- Precios
- Fechas de facturación
- Clientes
- Países

---

# Proceso ETL

## 1. Extract

Los dos archivos CSV son cargados utilizando `pandas.read_csv()` y posteriormente combinados en un único DataFrame.

También se conserva una copia de los datos originales mediante `raw_df` para mantener una referencia de los datos antes de la transformación.

---

## 2. Transform

### Tratamiento de valores nulos

Se realizó una revisión inicial de los valores nulos y tipos de datos.

Las columnas `Description` y `Customer ID` fueron analizadas durante el proceso de limpieza.

Se decidió eliminar:

- Registros sin `Description`.
- Registros sin `Customer ID`.

Esto permite trabajar posteriormente con información de productos y clientes identificables.

### Conversión de tipos

La columna `InvoiceDate` fue convertida a tipo fecha mediante `pandas.to_datetime()`.

La columna `Customer ID` fue convertida a formato numérico utilizando el tipo nullable `Int64`.

### Duplicados

Se identificaron y eliminaron registros duplicados mediante:

```python
clean_df = clean_df.drop_duplicates()
```

También se realizaron validaciones posteriores para comprobar posibles duplicados en clientes, productos y facturas.

### Revenue

Se creó una nueva columna denominada `Revenue`:

```text
Revenue = Quantity × Price
```

Esta columna representa el ingreso asociado a cada registro de transacción.

### Año

Se creó la columna `Year` a partir de `InvoiceDate`:

```python
clean_df["Year"] = clean_df["InvoiceDate"].dt.year
```

Esta columna permite realizar análisis agrupados por año.

---

# Modelo de datos

Después de la limpieza, la información se dividió en cuatro tablas principales.

## Customer

Contiene información de los clientes:

- `Customer ID`
- `Country`

Se eliminan duplicados utilizando `Customer ID` como identificador.

## Products

Contiene información de los productos:

- `StockCode`
- `Description`

Los productos se deduplican utilizando `StockCode`.

## Invoices

Contiene información de las facturas:

- `Invoice`
- `InvoiceDate`
- `Customer ID`

Cada factura se conserva de forma única utilizando `Invoice`.

## Transactions

Contiene la información principal de las transacciones:

- `Transaction ID`
- `Invoice`
- `StockCode`
- `Quantity`
- `Price`
- `Revenue`

El `Transaction ID` se genera durante el proceso de transformación.

---

## Estructura de relaciones

El modelo puede representarse conceptualmente de la siguiente manera:

```text
        Customer
           │
           │ Customer ID
           ▼
        Invoices
           │
           │ Invoice
           ▼
      Transactions
           │
           │ StockCode
           ▼
        Products
```

---

# Validaciones

Durante el proceso se realizaron diferentes validaciones de calidad de datos.

Se verificaron:

- Cantidad de valores nulos.
- Cantidad de registros duplicados.
- Duplicados en clientes.
- Duplicados en productos.
- Duplicados en facturas.
- Descripciones diferentes asociadas a un mismo `StockCode`.
- Clientes diferentes asociados a una misma factura.
- Fechas diferentes asociadas a una misma factura.
- Consistencia entre `Quantity × Price` y `Revenue`.

La consistencia del cálculo de revenue se comprobó mediante:

```python
(
    transactions["Quantity"] * transactions["Price"]
    == transactions["Revenue"]
).all()
```

---

# PostgreSQL

Los datos transformados fueron cargados en una base de datos PostgreSQL denominada:

```text
Prueba
```

La conexión se realiza mediante SQLAlchemy y las credenciales se obtienen mediante variables de entorno.

```python
password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/Prueba"
)
```

Las tablas cargadas son:

- `customer`
- `products`
- `invoices`
- `transactions`

---

# Seguridad

La contraseña de PostgreSQL no se encuentra escrita directamente en el código.

Se utiliza un archivo `.env` para almacenar la variable:

```text
DB_PASSWORD
```

El archivo `.env` permanece fuera del repositorio mediante `.gitignore`.

Esto evita publicar credenciales sensibles en GitHub.

---

# Power BI

La información almacenada en PostgreSQL puede utilizarse como fuente para Power BI.

El análisis permite visualizar aspectos como:

- Evolución de ingresos.
- Productos con mayor desempeño.
- Distribución de ingresos.
- Comportamiento por país.
- Comportamiento de clientes.
- Relación entre cantidad, precio e ingresos.

---

# Resultados del proceso

Después de realizar la limpieza y transformación, los datos son estructurados en tablas relacionadas y cargados en PostgreSQL.

El proceso permite pasar de los archivos originales de ventas a una estructura organizada para análisis y Business Intelligence.

---

# Estructura del proyecto

```text
DataAnalytics/
│
├── data/
│   ├── Retail 2009-10.csv
│   └── Retail 2010-11.csv
│
├── .gitignore
├── main.py
├── etl.py
└── requirements.txt
```

> El archivo `.env` y el entorno virtual `.venv` no deben incluirse en el repositorio.

---

# Ejecución

## 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 2. Configurar las variables de entorno

Crear un archivo `.env` con las credenciales necesarias para PostgreSQL.

## 3. Ejecutar el proceso

```bash
python main.py
```

El programa:

1. Carga los dos archivos CSV.
2. Combina los datasets.
3. Limpia y transforma los datos.
4. Crea las tablas de clientes, productos, facturas y transacciones.
5. Realiza validaciones.
6. Se conecta a PostgreSQL.
7. Carga las tablas en la base de datos.

---

## Autor

**Mateo Hernandez Mendoza**
Cohorte 5 — Análisis de Datos
