# src/import_csv.py
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Define the base directory (the parent of src)
BASE = Path(__file__).resolve().parents[1]

# Paths for the database and CSV file
DB_PATH = BASE / "clinic_simple.db"
CSV_PATH = BASE / "data" / "patients.csv"

def main():
    # Create a connection engine to the SQLite database
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Read the CSV into a Pandas DataFrame
    df = pd.read_csv(CSV_PATH, dtype=str)

    # Clean up dates to make sure they're in ISO format
    for col in ["birth_date", "last_visit_dt"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")

    # Load the data into the 'patients' table
    df.to_sql("patients", con=engine, if_exists="append", index=False)

    print(f"✅ Imported {len(df)} rows into 'patients' table.")

# Run main() only if this file is executed directly
if __name__ == "__main__":
    main()
