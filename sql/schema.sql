DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
  patient_id     TEXT PRIMARY KEY,         -- e.g., P0001
  birth_date     DATE NOT NULL,            -- ISO: YYYY-MM-DD
  primary_icd10  TEXT NOT NULL,            -- e.g., E11.9
  last_cpt       TEXT NOT NULL,            -- e.g., 99213
  last_visit_dt  DATE NOT NULL             -- ISO date
);
