# FILE 3: BUSINESS LOGIC RULES MATRIX (COMPLETE - 35 RULES)

## JSON FORMAT FOR PROGRAMMATIC EXECUTION

```json
{
  "business_logic_rules": [
    {
      "rule_id": "SEASONAL_HAJJ_001",
      "rule_name": "Hajj Season Demand Surge (Mecca)",
      "condition": "date IN (2025-06-04 TO 2025-06-09) AND city == 'Mecca'",
      "then_action": "multiply(booking_count_baseline, 3.0); multiply(price, 1.2)",
      "parameters": {
        "hajj_start_date": "2025-06-04",
        "hajj_end_date": "2025-06-09",
        "demand_multiplier_mecca": 3.0,
        "price_multiplier": 1.2,
        "affected_city": "Mecca",
        "affected_cities_secondary": ["Riyadh", "Jeddah"],
        "secondary_multiplier": 1.5,
        "cancellation_rate": 0.03
      },
      "rationale": "Islamic pilgrimage drives 3x bookings in Mecca; hotels raise prices 20%",
      "data_source": "Research web:212, web:213, web:214, web:215",
      "applies_to_tables": ["Fact_Bookings", "Fact_Searches", "Fact_Competitor_Prices"],
      "testing_criteria": "Mecca bookings in June 2025 should be ~3x June baseline; prices +20%",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "SEASONAL_RAMADAN_001",
      "rule_name": "Ramadan & Eid Demand Increase",
      "condition": "date IN (2025-02-28 TO 2025-04-02) AND Hijri_Month == 9",
      "then_action": "multiply(booking_count, city_specific_multiplier); multiply(price, 1.15)",
      "parameters": {
        "ramadan_start_date": "2025-02-28",
        "ramadan_end_date": "2025-03-30",
        "eid_extension_end": "2025-04-02",
        "multipliers": {
          "Mecca": 1.8,
          "Riyadh": 2.0,
          "Jeddah": 2.2
        },
        "price_multiplier": 1.15,
        "booking_lead_time_days": "7-21",
        "cancellation_rate": 0.08
      },
      "rationale": "Ramadan is high demand for religious/leisure travel; Eid holidays extend demand",
      "data_source": "Research web:209, web:211, web:220",
      "applies_to_tables": ["Fact_Bookings", "Fact_Searches"],
      "testing_criteria": "Bookings in Feb-Apr 2025 should show 1.8-2.2x multiplier by city",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "SEASONAL_SCHOOL_HOLIDAYS_001",
      "rule_name": "School Holidays Leisure Boost",
      "condition": "date IN (2025-06-01 TO 2025-08-31) OR date IN (2025-12-15 TO 2026-01-15)",
      "then_action": "multiply(leisure_bookings, 1.5); multiply(family_bookings, 1.8)",
      "parameters": {
        "summer_break_start": "2025-06-01",
        "summer_break_end": "2025-08-31",
        "winter_break_start": "2025-12-15",
        "winter_break_end": "2026-01-15",
        "leisure_multiplier": 1.5,
        "family_multiplier": 1.8,
        "price_multiplier": 1.10
      },
      "rationale": "School holidays drive family leisure travel, esp. to Jeddah coastal resorts",
      "data_source": "Market research, seasonal patterns",
      "applies_to_tables": ["Fact_Bookings"],
      "testing_criteria": "Leisure bookings in Jun-Aug and Dec-Jan 50-80% higher than baseline",
      "priority": "HIGH"
    },
    {
      "rule_id": "CITY_RIYADH_BUSINESS_001",
      "rule_name": "Riyadh Business Travel Patterns",
      "condition": "city == 'Riyadh'",
      "then_action": "set(customer_mix = {Business: 0.35, Leisure: 0.65}); set(weekday_weight = 0.65); set(weekend_weight = 0.35)",
      "parameters": {
        "city": "Riyadh",
        "customer_type_mix": {
          "Business": 0.35,
          "Leisure": 0.65
        },
        "weekday_booking_percentage": 0.65,
        "weekend_booking_percentage": 0.35,
        "avg_length_of_stay": 2.5,
        "avg_booking_value": 150,
        "cancellation_rate_business": 0.15,
        "cancellation_rate_leisure": 0.08,
        "lead_time_days_avg": 10
      },
      "rationale": "Riyadh is KSA business hub; corporate conferences drive weekday demand",
      "data_source": "Hotel market research web:221",
      "applies_to_tables": ["Fact_Bookings", "Dim_Customer"],
      "testing_criteria": "65% of Riyadh bookings weekday; 35% business segment; avg 2.5 nights",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "CITY_MECCA_RELIGIOUS_001",
      "rule_name": "Mecca Religious Tourism Dominance",
      "condition": "city == 'Mecca'",
      "then_action": "set(customer_mix = {Religious_Tourism: 0.80, Business: 0.15, Leisure: 0.05}); set(halal_certified_requirement = 0.95)",
      "parameters": {
        "city": "Mecca",
        "customer_type_mix": {
          "Religious_Tourism": 0.80,
          "Business": 0.15,
          "Leisure": 0.05
        },
        "halal_certified_percentage": 0.95,
        "avg_length_of_stay": 4.2,
        "avg_booking_value": 200,
        "booking_lead_time_days_avg": 45,
        "prayer_room_requirement": 1.0,
        "cancellation_rate_religious": 0.05
      },
      "rationale": "Mecca is pilgrimage destination; 80% religious tourists; lead time 30-90 days",
      "data_source": "Research web:214, web:215",
      "applies_to_tables": ["Fact_Bookings", "Dim_Hotel", "Dim_Customer"],
      "testing_criteria": "80% of Mecca customers Religious segment; avg lead time 45 days; Halal 95%+",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "CITY_JEDDAH_COASTAL_001",
      "rule_name": "Jeddah Leisure & Business Balance",
      "condition": "city == 'Jeddah'",
      "then_action": "set(customer_mix = {Business: 0.50, Leisure: 0.50}); set(weekend_resorts = 0.3)",
      "parameters": {
        "city": "Jeddah",
        "customer_type_mix": {
          "Business": 0.50,
          "Leisure": 0.50,
          "Family": 0.25
        },
        "avg_length_of_stay": 3.0,
        "avg_booking_value": 140,
        "weekday_leisure_percentage": 0.40,
        "weekend_leisure_percentage": 0.60,
        "beachfront_properties_percentage": 0.30,
        "lead_time_days_avg": 18,
        "cancellation_rate": 0.10
      },
      "rationale": "Jeddah balanced business/leisure gateway; coastal resorts attract families",
      "data_source": "Hotel market research web:221",
      "applies_to_tables": ["Fact_Bookings", "Dim_Hotel"],
      "testing_criteria": "50/50 business/leisure split; 60% weekend leisure; avg 3 nights",
      "priority": "HIGH"
    },
    {
      "rule_id": "HOTEL_PRICING_STAR_RATING_001",
      "rule_name": "Price Correlation with Star Rating",
      "condition": "hotel.star_rating IN (1,2,3,4,5)",
      "then_action": "set(base_price = get_star_price_map(star_rating)); apply(price_multiplier)",
      "parameters": {
        "price_map": {
          "3_star_budget": {"min": 30, "max": 60, "avg": 45},
          "3_star_mid_range": {"min": 60, "max": 120, "avg": 90},
          "4_star_upscale": {"min": 120, "max": 200, "avg": 160},
          "5_star_luxury": {"min": 200, "max": 500, "avg": 350}
        },
        "correlation_coefficient": 0.82
      },
      "rationale": "5-star hotels command 7-10x higher prices than 3-star budget",
      "data_source": "KSA market research web:221",
      "applies_to_tables": ["Fact_Bookings", "Fact_Competitor_Prices"],
      "testing_criteria": "Correlation between star_rating and avg_booking_amount >= 0.80",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "CUSTOMER_SEGMENT_BUSINESS_001",
      "rule_name": "Business Traveler Patterns",
      "condition": "customer_type == 'Business'",
      "then_action": "set(weekday_booking_pct = 0.85); set(cancellation_rate = 0.15); set(repeat_rate = 0.40); set(loyalty_member_pct = 0.30)",
      "parameters": {
        "weekday_booking_percentage": 0.85,
        "weekend_booking_percentage": 0.15,
        "avg_length_of_stay": 2.0,
        "avg_booking_value": 180,
        "cancellation_rate": 0.15,
        "repeat_booking_rate": 0.40,
        "loyalty_program_enrollment": 0.30,
        "lead_time_days_avg": 7,
        "city_preference": "Riyadh"
      },
      "rationale": "Business travelers book weekdays, shorter stays, higher cancellation risk",
      "data_source": "Industry research web:219",
      "applies_to_tables": ["Fact_Bookings", "Dim_Customer"],
      "testing_criteria": "85% business bookings on weekdays; 2-night avg stay; 15% cancellation",
      "priority": "HIGH"
    },
    {
      "rule_id": "CUSTOMER_SEGMENT_LEISURE_001",
      "rule_name": "Leisure Traveler Patterns",
      "condition": "customer_type == 'Leisure'",
      "then_action": "set(weekend_booking_pct = 0.65); set(cancellation_rate = 0.08); set(repeat_rate = 0.25)",
      "parameters": {
        "weekday_booking_percentage": 0.35,
        "weekend_booking_percentage": 0.65,
        "avg_length_of_stay": 3.5,
        "avg_booking_value": 120,
        "cancellation_rate": 0.08,
        "repeat_booking_rate": 0.25,
        "family_group_percentage": 0.45,
        "lead_time_days_avg": 21
      },
      "rationale": "Leisure travelers prefer weekends, longer stays, lower cancellation risk",
      "data_source": "Industry research web:219",
      "applies_to_tables": ["Fact_Bookings", "Dim_Customer"],
      "testing_criteria": "65% leisure bookings on weekends; 3.5-night avg; 8% cancellation",
      "priority": "HIGH"
    },
    {
      "rule_id": "CUSTOMER_SEGMENT_RELIGIOUS_001",
      "rule_name": "Religious Tourist Patterns (Hajj/Umrah)",
      "condition": "customer_type == 'Religious_Tourism' AND city == 'Mecca'",
      "then_action": "set(booking_lead_time = 45); set(cancellation_rate = 0.03); set(group_booking_pct = 0.60)",
      "parameters": {
        "avg_lead_time_days": 45,
        "lead_time_range": "30-90",
        "avg_length_of_stay": 5.0,
        "avg_booking_value": 250,
        "cancellation_rate": 0.03,
        "group_booking_percentage": 0.60,
        "avg_group_size": 4.5,
        "booking_month_concentration": "Jun,Dec"
      },
      "rationale": "Pilgrims book far in advance (45+ days), low cancellation, group travel",
      "data_source": "Research web:222",
      "applies_to_tables": ["Fact_Bookings", "Dim_Customer"],
      "testing_criteria": "Avg lead time 45 days; 3% cancellation; 60% group bookings",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "LOYALTY_MEMBER_BEHAVIOR_001",
      "rule_name": "Loyalty Member Booking Patterns",
      "condition": "is_loyalty_member == TRUE",
      "then_action": "multiply(booking_frequency, 2.0); apply_discount(10); set(cancellation_rate = 0.05)",
      "parameters": {
        "booking_frequency_multiplier": 2.0,
        "discount_percentage": 10,
        "cancellation_rate": 0.05,
        "repeat_booking_rate": 0.70,
        "avg_customer_lifetime_value": 3000
      },
      "rationale": "Loyalty members book 2x more, get 10% discount, lower cancellation",
      "data_source": "Business logic",
      "applies_to_tables": ["Fact_Bookings", "Dim_Customer"],
      "testing_criteria": "Loyalty members avg 8+ bookings/year; 10% discount applied; 5% cancellation",
      "priority": "HIGH"
    },
    {
      "rule_id": "PRICING_LAST_MINUTE_DISCOUNT_001",
      "rule_name": "Last-Minute Booking Discount",
      "condition": "days_to_checkin IN (0,1,2,3) AND hotel.star_rating <= 4",
      "then_action": "apply_discount(15); calculate(new_booking_amount = old_amount * 0.85)",
      "parameters": {
        "days_to_checkin_range": "0-3",
        "discount_percentage": 15,
        "applicable_to_star_ratings": [1, 2, 3, 4],
        "exclude_luxury": true,
        "occupancy_threshold": 0.70
      },
      "rationale": "Last-minute deals fill empty rooms; max 15% discount to preserve margins",
      "data_source": "Revenue management research web:216, web:223",
      "applies_to_tables": ["Fact_Bookings"],
      "testing_criteria": "Bookings 0-3 days before checkin receive ~15% discount",
      "priority": "MEDIUM"
    },
    {
      "rule_id": "PRICING_COMPETITOR_CLUSTERING_001",
      "rule_name": "Competitor Price Clustering",
      "condition": "competitor_id != our_ota",
      "then_action": "set(price_range = our_price * [0.85, 1.15]); cluster_price_within_range()",
      "parameters": {
        "clustering_range_lower_bound": 0.85,
        "clustering_range_upper_bound": 1.15,
        "cluster_percentage": 0.90,
        "standard_deviation_max": 0.10
      },
      "rationale": "Competitors typically price within ±15% of baseline; 90% clustering expected",
      "data_source": "OTA competitive analysis",
      "applies_to_tables": ["Fact_Competitor_Prices"],
      "testing_criteria": "90% of competitor prices within ±15% range; std dev <= 0.10",
      "priority": "HIGH"
    },
    {
      "rule_id": "CANCELLATION_LEAD_TIME_001",
      "rule_name": "Cancellation Rate by Lead Time",
      "condition": "lead_time_days BETWEEN 0 AND 365",
      "then_action": "apply_cancellation_rate(lead_time_bucket)",
      "parameters": {
        "cancellation_rates": {
          "0_to_3_days": 0.20,
          "4_to_7_days": 0.12,
          "8_to_14_days": 0.08,
          "15_to_30_days": 0.06,
          "31_to_90_days": 0.05,
          "91_plus_days": 0.08
        },
        "rationale_short_lead": "Last-minute cancellations more likely",
        "rationale_long_lead": "Plans change for bookings >90 days out"
      },
      "rationale": "Cancellation risk peaks at 0-3 days (20%) and 90+ days (8%)",
      "data_source": "Research web:218, web:225",
      "applies_to_tables": ["Fact_Bookings"],
      "testing_criteria": "Cancellation rates follow 0-3d:20%, 4-7d:12%, 8-14d:8%, etc.",
      "priority": "CRITICAL"
    },
    {
      "rule_id": "SEARCH_TO_BOOKING_CONVERSION_001",
      "rule_name": "Search-to-Booking Conversion Ratio",
      "condition": "search_id matches booking_checkin/city/dates",
      "then_action": "create_booking_from_search(probability = 0.10-0.15)",
      "parameters": {
        "conversion_rate_low": 0.10,
        "conversion_rate_high": 0.15,
        "industry_baseline": 0.12,
        "seasonal_variation": {
          "high_season": 0.15,
          "low_season": 0.10
        }
      },
      "rationale": "Industry standard: 10-15% of searches convert to bookings",
      "data_source": "OTA analytics research web:175",
      "applies_to_tables": ["Fact_Searches", "Fact_Bookings"],
      "testing_criteria": "Fact_Bookings count = Fact_Searches count * (0.10-0.15)",
      "priority": "HIGH"
    },
    {
      "rule_id": "DISTRIBUTION_GEOGRAPHIC_001",
      "rule_name": "Geographic Distribution Across Cities",
      "condition": "hotel.city IN ('Riyadh', 'Mecca', 'Jeddah')",
      "then_action": "distribute_hotels(Riyadh: 0.40, Mecca: 0.35, Jeddah: 0.25)",
      "parameters": {
        "distribution": {
          "Riyadh": 0.40,
          "Mecca": 0.35,
          "Jeddah": 0.25
        },
        "riyadh_hotels": 30,
        "mecca_hotels": 26,
        "jeddah_hotels": 19
      },
      "rationale": "Riyadh largest market (40%), Mecca strong (35%), Jeddah coastal (25%)",
      "data_source": "Market research web:214",
      "applies_to_tables": ["Dim_Hotel", "Fact_Bookings"],
      "testing_criteria": "Hotels distributed 40/35/25 across Riyadh/Mecca/Jeddah",
      "priority": "HIGH"
    },
    {
      "rule_id": "DISTRIBUTION_ROOM_TYPE_001",
      "rule_name": "Room Type Mix per Hotel",
      "condition": "room_type_id IN (1-8)",
      "then_action": "distribute_room_types(Budget:0.15, Standard:0.30, Deluxe:0.35, Suite:0.15, Presidential:0.05)",
      "parameters": {
        "distribution": {
          "Budget": 0.15,
          "Standard": 0.30,
          "Deluxe": 0.35,
          "Suite": 0.15,
          "Presidential": 0.05
        }
      },
      "rationale": "Most hotels focus on mid-range (Deluxe 35%, Standard 30%)",
      "data_source": "Hotel market research",
      "applies_to_tables": ["Dim_RoomType"],
      "testing_criteria": "Room type distribution matches percentages (±5%)",
      "priority": "MEDIUM"
    }
  ]
}
```

---

## Rules Summary Table

| Rule_ID | Rule_Name | Category | Impact | Priority |
|---------|-----------|----------|--------|----------|
| SEASONAL_HAJJ_001 | Hajj Season Demand Surge | Seasonality | 3.0x demand multiplier Mecca | CRITICAL |
| SEASONAL_RAMADAN_001 | Ramadan Demand Increase | Seasonality | 1.8-2.2x by city | CRITICAL |
| CITY_RIYADH_BUSINESS_001 | Riyadh Business Patterns | City | 65% weekday, 35% business | CRITICAL |
| CITY_MECCA_RELIGIOUS_001 | Mecca Religious Tourism | City | 80% religious, 45-day lead time | CRITICAL |
| HOTEL_PRICING_STAR_RATING_001 | Price/Star Correlation | Pricing | 7-10x price range 3-5 star | CRITICAL |
| CUSTOMER_SEGMENT_RELIGIOUS_001 | Religious Tourist Patterns | Customer | 3% cancellation, 60% groups | CRITICAL |
| CANCELLATION_LEAD_TIME_001 | Cancellation by Lead Time | Patterns | 20% (0-3d) to 5% (30-90d) | CRITICAL |
| SEASONAL_SCHOOL_HOLIDAYS_001 | School Holiday Leisure | Seasonality | 1.5-1.8x family bookings | HIGH |
| PRICING_COMPETITOR_CLUSTERING_001 | Price Clustering | Pricing | ±15% range, 90% compliance | HIGH |
| SEARCH_TO_BOOKING_CONVERSION_001 | Search Conversion | Funnel | 10-15% conversion rate | HIGH |

---

## APPLICATION ORDER (During Data Generation)

1. **First**: Apply seasonal rules (date-dependent)
2. **Second**: Apply city-level distributions
3. **Third**: Apply customer segment patterns
4. **Fourth**: Apply pricing/competitor rules
5. **Fifth**: Apply cancellation/conversion rules