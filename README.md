# Data-Validation-Tool-SQLite
## A lightweight and beginner-friendly data quality validation tool built using Python + SQLite. It automatically checks a database for common data issues like missing values, duplicates, invalid relationships, and timestamp errors — and logs the results neatly.

## 🚀 Features

- ✔️ Validate data inside SQLite database
- ✔️ Detect missing or null values
- ✔️ Detect duplicate order IDs
- ✔️ Identify timestamp mismatches (order_date > delivery_date)
- ✔️ Validate foreign key relationships between customers and orders
- ✔️ Auto-generated log files with detailed results
- ✔️ Simple run_validation.py script to execute all checks

## 📁 Project Structure

```
data_quality_tool/
│── config.py
│── sql_queries.py
│── validator.py
│── run_validation.py
│── sample_data.db
│── logs/
    └── validation_YYYY-MM-DD_HH-MM.log
```

## ⚙️ Configuration

### The database path and log directory are stored in config.py
```bash
DB_PATH = "sample_data.db"
LOG_DIR = "logs"
```

## 🧪 Validation Checks

### All SQL queries are stored in sql_queries.py

1️⃣ Missing Values

Finds orders with NULL customer_id or NULL order_date.

2️⃣ Duplicate Orders

Detects multiple records with the same order_id.

3️⃣ Timestamp Mismatch

Finds rows where order_date is greater than delivery_date.

4️⃣ Invalid Relationships

Checks if an order links to a non-existent customer.


## 🛠️ How It Works

The main validation logic is implemented in validator.py:

### Key Features:

- Creates log directory automatically
- Runs each SQL check and prints results
- Logs every message to a timestamped log file


## ▶️ Running the Tool

- Use the driver script run_validation.py:

Run:
``` bash
python run_validation.py
```

### Output:

- Console output with pass/fail for each check
- A log file created inside logs/ such as:
``` bash
logs/validation_2025-12-08_17-30.log
```

## 🗄️ Sample Database Schema
```bash
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name TEXT
);

CREATE TABLE orders (
    order_id INT ,
    customer_id INT,
    order_date TEXT,
    delivery_date TEXT,
    amount REAL
);
```
## 📌 Example Use Cases

- Data validation before analytics
- Checking data consistency in ETL pipelines
- Automated quality checks for SQLite-based systems
- Student projects / learning SQL + Python

## Validation Scenarios
### Scenario 1 — Output When Issues Are Found

<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/5f48cb9c-26e7-4bbd-9cdd-7cdb13c2def8" />

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/b864e5d9-380d-43eb-acbc-b378a8f71ed0" />

## Log File Folder:
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/3dcd3399-a3f9-4b80-8563-1a007f9f85fc" />

## Log File Generated:
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/4aeda28d-a3f6-40c9-82d9-e7c5f1486fd6" />

## Log File:
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/3af602a8-5720-4424-94da-da2b931ea674" />

### Scenario 2 — Output When Issues Are Not Found
```bash
===== DATA VALIDATION STARTED =====

---- Running Check: missing_values ----
[PASSED] No issues found.

---- Running Check: duplicate_orders ----
[PASSED] No issues found.

---- Running Check: timestamp_mismatch ----
[PASSED] No issues found.

---- Running Check: invalid_relationships ----
[PASSED] No issues found.

===== VALIDATION COMPLETED =====
```



