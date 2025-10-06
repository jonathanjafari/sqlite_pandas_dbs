-- A) Row count
SELECT COUNT(*) AS n_patients FROM patients;

-- B) Top primary diagnoses by count
SELECT primary_icd10, COUNT(*) AS n
FROM patients
GROUP BY primary_icd10
ORDER BY n DESC;

-- C) Office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992)
SELECT patient_id, last_cpt, last_visit_dt
FROM patients
WHERE last_cpt LIKE '992%' AND last_visit_dt >= '2025-01-01'
ORDER BY last_visit_dt DESC;

-- D) Age (approx) at last visit for the 5 oldest patients
SELECT
  patient_id,
  birth_date,
  last_visit_dt,
  CAST((julianday(date('now')) - julianday(birth_date)) / 365.25 AS INT) AS age_years
FROM patients
ORDER BY age_years DESC
LIMIT 5;

-- E) Quick data quality check: any blank codes?
SELECT *
FROM patients
WHERE primary_icd10 = '' OR last_cpt = '';
