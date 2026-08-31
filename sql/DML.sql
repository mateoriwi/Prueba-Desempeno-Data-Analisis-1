CREATE TABLE customer (
    "Customer ID" INT PRIMARY KEY,
    "Country" VARCHAR(100)
);

CREATE TABLE products (
    "StockCode" VARCHAR(20) PRIMARY KEY,
    "Description" VARCHAR(255)
);

CREATE TABLE invoices (
    "Invoice" VARCHAR(20) PRIMARY KEY,
    "InvoiceDate" TIMESTAMP,
    "Customer ID" INT,

    FOREIGN KEY ("Customer ID")
        REFERENCES customer("Customer ID")
);

CREATE TABLE transactions (
    "Transaction ID" INT PRIMARY KEY,
    "Invoice" VARCHAR(20),
    "StockCode" VARCHAR(20),
    "Quantity" INT,
    "Price" FLOAT NOT NULL,
	"Revenue" FLOAT NOT NULL,

    FOREIGN KEY ("Invoice")
        REFERENCES invoices("Invoice"),

    FOREIGN KEY ("StockCode")
        REFERENCES products("StockCode")
);