# Proyecto de Data Analytics — Online Retail II

## Descripción

Proyecto de análisis y procesamiento de datos desarrollado para el análisis de información comercial del dataset **Online Retail II**.

La solución utiliza los archivos de ventas correspondientes a los períodos 2009-2010 y 2010-2011. Los datos son procesados mediante Python y Pandas, almacenados en PostgreSQL y posteriormente utilizados en Power BI para realizar análisis y visualizaciones.

---

## Objetivo

Procesar y organizar información de ventas para obtener una estructura de datos adecuada para su almacenamiento y análisis.

El flujo principal de la solución es:

```text
Archivos CSV
↓
Python / Pandas
↓
Limpieza y transformación
↓
Organización de los datos
↓
PostgreSQL
↓
Power BI
↓
Análisis y visualización
```

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

## Estructura del proyecto

```text
Prueba-Desempeno-Data-Analisis-1/
│
├── data/
│   ├── Retail 2009-10.csv
│   └── Retail 2010-11.csv
│
├── sql/
│   └── DML.sql
│
├── captures/
│
├── main.py
├── etl.py
└── README.md
```

## Archivos principales

### `main.py`

Archivo principal utilizado para ejecutar el proceso ETL.

### `etl.py`

Contiene el proceso ETL utilizado para cargar, limpiar, transformar y almacenar los datos.

### `sql/DML.sql`

Contiene las instrucciones SQL utilizadas para crear las tablas de PostgreSQL.

### `data/`

Contiene los archivos CSV utilizados como fuente de información.

---

## Dataset

El proyecto utiliza el dataset **Online Retail II**, dividido en dos archivos:

- `Retail 2009-10.csv`
- `Retail 2010-11.csv`

Los archivos son cargados mediante Pandas y posteriormente combinados para realizar el procesamiento.

---

## Proceso ETL

### Extract

Los archivos CSV son cargados mediante Pandas:

```python
df2009 = pd.read_csv("data/Retail 2009-10.csv")
df2010 = pd.read_csv("data/Retail 2010-11.csv")

df = pd.concat([df2009, df2010], ignore_index=True)
```

### Transform

Durante el proceso se realizan diferentes operaciones:

- Tratamiento de valores nulos.
- Conversión de `InvoiceDate` a formato de fecha.
- Conversión de `Customer ID` a formato numérico.
- Eliminación de registros incompletos.
- Eliminación de registros duplicados.
- Creación de la columna `Revenue`.

El ingreso de cada registro se calcula mediante:

```text
Revenue = Quantity × Price
```

También se genera una columna `Year` a partir de la fecha de factura.

### Load

Los datos procesados se organizan en cuatro tablas y posteriormente se cargan en PostgreSQL:

- `customer`
- `products`
- `invoices`
- `transactions`

---

## Modelo de datos

La información se organiza de la siguiente manera:

### Customer

Contiene:

- `Customer ID`
- `Country`

### Products

Contiene:

- `StockCode`
- `Description`

### Invoices

Contiene:

- `Invoice`
- `InvoiceDate`
- `Customer ID`

### Transactions

Contiene:

- `Transaction ID`
- `Invoice`
- `StockCode`
- `Quantity`
- `Price`
- `Revenue`

Las tablas se relacionan mediante claves primarias y foráneas.

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

## PostgreSQL

Los datos procesados se almacenan en una base de datos PostgreSQL llamada:

```text
Prueba
```

El archivo `sql/DML.sql` contiene la estructura de las tablas utilizadas por la solución.

Las tablas creadas son:

- `customer`
- `products`
- `invoices`
- `transactions`

---

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/mateoriwi/Prueba-Desempeno-Data-Analisis-1.git
```

Ingresar a la carpeta:

```bash
cd Prueba-Desempeno-Data-Analisis-1
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install pandas numpy psycopg2 sqlalchemy python-dotenv
```

### 4. Configurar PostgreSQL

Crear una base de datos llamada:

```text
Prueba
```

Después ejecutar el archivo:

```text
sql/DML.sql
```

Esto crea las tablas necesarias para almacenar la información.

### 5. Configurar las credenciales

Crear un archivo `.env` en la raíz del proyecto:

```text
.env
```

Agregar:

```env
DB_PASSWORD=TU_CONTRASEÑA
```

Reemplazar `TU_CONTRASEÑA` por la contraseña del usuario de PostgreSQL.

El archivo `.env` no debe publicarse en el repositorio.

---

## Ejecución

Con PostgreSQL configurado y el entorno virtual activado, ejecutar:

```bash
python main.py
```

El proceso realiza automáticamente:

- Carga de los archivos CSV.
- Unión de los datasets.
- Limpieza de los datos.
- Transformación de los datos.
- Organización de la información.
- Conexión con PostgreSQL.
- Carga de las tablas en la base de datos.

Cuando la ejecución termina correctamente se muestra:

```text
¡Conexión exitosa con PostgreSQL!
Proceso ETL completado correctamente.
```

---

## Power BI

Los datos almacenados en PostgreSQL pueden utilizarse en Power BI para realizar el análisis y visualización de la información.

El análisis permite consultar aspectos como:

- Ingresos.
- Transacciones.
- Productos.
- Clientes.
- Países.
- Cantidades vendidas.
- Evolución de las ventas.

El modelo de datos utilizado en Power BI está compuesto por las tablas:

- `Customer`
- `Invoices`
- `Transactions`
- `Products`

---

## Funcionalidades

La solución permite:

- Procesar archivos de ventas.
- Limpiar datos.
- Transformar tipos de datos.
- Eliminar registros duplicados e incompletos.
- Calcular ingresos.
- Organizar los datos en tablas relacionadas.
- Almacenar la información en PostgreSQL.
- Utilizar los datos en Power BI.
- Analizar los resultados mediante indicadores y visualizaciones.

---

## Buenas prácticas aplicadas

Durante el desarrollo se aplicaron algunas prácticas para mantener organizada y segura la solución:

- Separación de los datos fuente y los datos procesados.
- Uso de variables de entorno para las credenciales de PostgreSQL.
- Organización del proyecto mediante carpetas.
- Uso de nombres descriptivos para variables y tablas.
- Eliminación de registros duplicados.
- Validación y transformación de los tipos de datos.
- Separación del proceso principal y del proceso ETL.

---

## Resultado esperado

Al finalizar correctamente el proceso se obtiene:

```text
CSV
↓
ETL
↓
PostgreSQL
↓
Power BI
↓
Dashboard
```

La información de ventas queda procesada, organizada y disponible para realizar análisis mediante Power BI.
