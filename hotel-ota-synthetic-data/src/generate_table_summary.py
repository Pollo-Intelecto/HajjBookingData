
# Create complete Data Dictionary summary (fixing Python syntax - use None instead of null)

data_dictionary_summary = {
    "Fact_Bookings": {
        "type": "Fact Table",
        "granularity": "One row per booking transaction",
        "record_count": "10,000-20,000",
        "column_count": 20,
        "key_columns": ["Booking_ID (PK)", "Hotel_ID (FK)", "Customer_ID (FK)", "Booking_Date_ID (FK)"]
    },
    "Fact_Searches": {
        "type": "Fact Table",
        "granularity": "One row per search query",
        "record_count": "50,000-100,000",
        "column_count": 13,
        "key_columns": ["Search_ID (PK)", "Customer_ID (FK)", "Search_Date_ID (FK)"]
    },
    "Fact_Competitor_Prices": {
        "type": "Fact Table",
        "granularity": "One row per hotel-competitor-date price snapshot",
        "record_count": "500,000+",
        "column_count": 8,
        "key_columns": ["Competitor_Price_ID (PK)", "Hotel_ID (FK)", "Competitor_ID (FK)"]
    },
    "Dim_Date": {
        "type": "Dimension Table",
        "granularity": "One row per calendar day",
        "record_count": "~550 days (18 months)",
        "column_count": 22,
        "key_columns": ["Date_ID (PK)", "Hijri_Date", "Is_Ramadan", "Is_Hajj_Season"]
    },
    "Dim_Hotel": {
        "type": "Dimension Table",
        "granularity": "One row per hotel property",
        "record_count": "50-100 hotels",
        "column_count": 19,
        "key_columns": ["Hotel_ID (PK)", "City", "Star_Rating", "Chain_Name"]
    },
    "Dim_Customer": {
        "type": "Dimension Table",
        "granularity": "One row per customer",
        "record_count": "5,000-15,000",
        "column_count": 16,
        "key_columns": ["Customer_ID (PK)", "Email", "Customer_Type", "Is_Loyalty_Member"]
    },
    "Dim_Location": {
        "type": "Dimension Table",
        "granularity": "One row per city/district",
        "record_count": "9-15 locations",
        "column_count": 7,
        "key_columns": ["Location_ID (PK)", "City", "District", "City_Type"]
    },
    "Dim_RoomType": {
        "type": "Dimension Table",
        "granularity": "One row per room category",
        "record_count": "~15-20 types",
        "column_count": 5,
        "key_columns": ["Room_Type_ID (PK)", "Room_Category", "Max_Occupancy"]
    },
    "Dim_Competitor": {
        "type": "Dimension Table",
        "granularity": "One row per OTA competitor",
        "record_count": "7 competitors",
        "column_count": 5,
        "key_columns": ["Competitor_ID (PK)", "Competitor_Name", "Market_Position"]
    },
    "Dim_Channel": {
        "type": "Dimension Table",
        "granularity": "One row per booking channel",
        "record_count": "~5-10 channels",
        "column_count": 4,
        "key_columns": ["Channel_ID (PK)", "Channel_Name", "Channel_Type"]
    },
    "Dim_LoyaltyTier": {
        "type": "Dimension Table",
        "granularity": "One row per loyalty tier",
        "record_count": "~4-5 tiers",
        "column_count": 6,
        "key_columns": ["Loyalty_Tier_ID (PK)", "Tier_Name", "Min_Bookings"]
    },
    "Dim_MarketEvent": {
        "type": "Dimension Table",
        "granularity": "One row per seasonal/market event",
        "record_count": "~15-20 events",
        "column_count": 7,
        "key_columns": ["Event_ID (PK)", "Event_Name", "Event_Type", "Demand_Multiplier"]
    }
}

# Create DataFrame
import pandas as pd

summary_rows = []
for table_name, details in data_dictionary_summary.items():
    summary_rows.append({
        'Table Name': table_name,
        'Type': details['type'],
        'Granularity': details['granularity'],
        'Record Count': details['record_count'],
        'Columns': details['column_count'],
        'Key Columns': ', '.join(details['key_columns'])
    })

summary_df = pd.DataFrame(summary_rows)

print("✅ COMPLETE DATA DICTIONARY - ALL 12 TABLES\n")
print(summary_df.to_string(index=False))
print(f"\n📊 SUMMARY STATISTICS:")
print(f"   Total Tables: {len(data_dictionary_summary)}")
print(f"   Fact Tables: 3")
print(f"   Dimension Tables: 9")
total_cols = sum([details['column_count'] for details in data_dictionary_summary.values()])
print(f"   Total Columns: {total_cols}")

summary_df.to_csv('hotel_ota_tables_summary.csv', index=False)
print("\n✅ Exported: hotel_ota_tables_summary.csv")
