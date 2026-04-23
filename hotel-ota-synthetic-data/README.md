# Hotel-OTA Synthetic Data Generator
**Saudi Arabia Market Entry — Data Analytics Project**

A synthetic hotel booking dataset built to support Power BI dashboard development for an OTA entering the Saudi market. All 590,000+ records were engineered from scratch — no real customer data involved.

---

## What's in the Dataset

| | |
|---|---|
| Tables | 12 (3 fact + 9 dimension) |
| Total records | 590,000+ |
| Date range | Jan 2024 – Jun 2025 |
| Cities | Riyadh, Mecca, Jeddah |
| KPIs supported | 25 (with DAX formulas) |

---

## Why Engineered, Not Random

Random generation produces flat, unrealistic data. Instead, we encoded 31 business rules directly into the generation logic — Saudi seasonal events, city traveler profiles, pricing tiers, and cancellation behavior — so the output mirrors how the market actually behaves.

Key patterns encoded:

- **Hajj (Jun 4–9):** Mecca bookings spike 3x
- **Ramadan (Feb 28–Mar 30):** All cities 2x demand
- **Riyadh:** Business-heavy, weekday-focused
- **Mecca:** 80% religious travelers, long lead times
- **Cancellations:** 5% early bookers → 20% last-minute

---

## Data Quality

48 automated tests were run against the generated data. All passed.

| Test Category | Result |
|---|---|
| Referential integrity (13 FK checks) | ✅ 100% |
| Date logic (booking ≤ check-in < check-out) | ✅ 100% |
| Seasonal multipliers (Hajj 3x, Ramadan 2x) | ✅ Confirmed |
| Search-to-book conversion | ✅ 12% (target: 10–15%) |
| Price vs. star rating correlation | ✅ r = 0.976 |

Full results in `validation/validation_results.csv`.

---

## Repository Structure

```
hotel-ota-synthetic-data/
│
├── spec/                           # Blueprints (rules, relationships, calendar)
│   ├── FILE1_Data_Dictionary_Complete.csv
│   ├── FILE2_Referential_Integrity.json
│   ├── FILE3_Business_Logic_Rules.json
│   └── FILE6_Market_Calendar_2025.json
│
├── src/                            # Generation scripts
│   ├── script_complete.py          # Generates all 12 CSVs
│   ├── generate_data_dictionary.py
│   ├── generate_kpi_catalogue.py
│   └── generate_table_summary.py
│
├── data/                           # Output — ready for Power BI import
│   ├── hotel_ota_tables_summary.csv
│   ├── hotel_ota_kpi_catalog.csv   # 25 KPIs with DAX formulas
│   └── ... (12 generated CSVs)
│
└── validation/
    └── validation_results.csv
```

---

## Running the Project

```bash
pip install pandas numpy
python src/script_complete.py       # generates all 12 CSVs into data/
```

> Uses `random_seed=42` — output is identical on every run.

---

## Tech Stack

Python · pandas · JSON · Power BI

---

## Authors

Ahmed Atef Mohran & Mu'min Ahmed
