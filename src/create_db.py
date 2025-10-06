# src/create_db.py
import sqlite3
from pathlib import Path

# Define the base folder (the parent folder of /src)
BASE = Path(__file__).resolve().parents[1]

# Paths for the database and schema file
DB_PATH = BASE / "clinic_simple.db"
SCHEMA_PATH = BASE / "sql" / "schema.sql"

def main():
    # Read the SQL commands from schema.sql
    sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Connect to (or create) the SQLite database file
    with sqlite3.connect(DB_PATH) as conn:
        # Execute the SQL script to create the table
        conn.executescript(sql)

    print(f"✅ Created {DB_PATH.name} using {SCHEMA_PATH}")

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
