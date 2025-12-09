import sqlite3
import os
from datetime import datetime
from config import DB_PATH, LOG_DIR
from sql_queries import SQL_CHECKS

class DataValidator:

    def __init__(self):
        os.makedirs(LOG_DIR, exist_ok=True)
        self.log_file = f"{LOG_DIR}/validation_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.log"

    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")
        print(message)

    def run_check(self, conn, check_name, query):
        self.log(f"\n---- Running Check: {check_name} ----")
        cursor = conn.execute(query)
        results = cursor.fetchall()

        if results:
            self.log(f"[FAILED] Found {len(results)} issue(s).")
            for row in results:
                self.log(f"  -> {row}")
        else:
            self.log("[PASSED] No issues found.")

    def run_all_checks(self):
        conn = sqlite3.connect(DB_PATH)
        self.log("\n===== DATA VALIDATION STARTED =====")

        for check_name, query in SQL_CHECKS.items():
            self.run_check(conn, check_name, query)

        self.log("\n===== VALIDATION COMPLETED =====")
        conn.close()
