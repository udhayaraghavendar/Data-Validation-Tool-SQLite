# Data-Validation-Tool-SQLite
## A lightweight and beginner-friendly data quality validation tool built using Python + SQLite. It automatically checks a database for common data issues like missing values, duplicates, invalid relationships, and timestamp errors — and logs the results neatly.

## 🚀 Features

-✔️ Validate data inside SQLite database
-✔️ Detect missing or null values
-✔️ Detect duplicate order IDs
-✔️ Identify timestamp mismatches (order_date > delivery_date)
-✔️ Validate foreign key relationships between customers and orders
-✔️ Auto-generated log files with detailed results
-✔️ Simple run_validation.py script to execute all checks

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

🛠️ How It Works

The main validation logic is implemented in validator.py:


Key Features:

Creates log directory automatically

Runs each SQL check and prints results

Logs every message to a timestamped log file

▶️ Running the Tool

Use the driver script run_validation.py:


Run:
python run_validation.py

Output:

Console output with pass/fail for each check

A log file created inside logs/ such as:

logs/validation_2025-12-08_17-30.log



