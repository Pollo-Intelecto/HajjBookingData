
# Create detailed 120-hour project timeline (Day-by-day breakdown)

timeline_data = {
    "Week 1 - Onboarding & Understanding Phase (18 hours total: focused on review & preparation)": {
        "Day 1 - Monday": [
            {
                "hour_range": "Hours 1-2 (Student A)",
                "task": "Project Kickoff & Scope Review",
                "description": "Read through complete Phase 1 deliverables (Scope, Problem Statement, Competitor Analysis). Understand project context: Saudi Arabia market, Riyadh/Mecca/Jeddah focus, 7 key competitors.",
                "output": "Scope Document reviewed; questions noted for clarification",
                "tools": "PDF reader, Phase 1 deliverables"
            },
            {
                "hour_range": "Hours 3-4 (Student A)",
                "task": "Star Schema & Data Model Deep Dive",
                "description": "Study the star schema design. Understand: Fact_Bookings grain (one row per booking), all dimension tables, foreign key relationships. Sketch relationships on paper.",
                "output": "Hand-drawn or digital schema diagram with labeled relationships",
                "tools": "Draw.io or pencil/paper"
            },
            {
                "hour_range": "Hours 5-6 (Student B)",
                "task": "KPI Catalog Review & Glossary Creation",
                "description": "Read all 25 KPIs. For each, write a 1-sentence 'why it matters' note in simple language. Create a personal glossary (e.g., 'RevPAR = revenue per available room = total $$ / total rooms').",
                "output": "Handwritten KPI glossary (25 entries); 1-2 pages",
                "tools": "KPI CSV, notebook"
            },
            {
                "handoff": "Student A's schema understanding + Student B's KPI glossary → needed for Week 2 data generation",
                "notes": "Students should feel comfortable explaining what data they'll generate and why each KPI matters."
            }
        ],
        "Day 2 - Tuesday": [
            {
                "hour_range": "Hours 7-8 (Student A)",
                "task": "Data Dictionary Study & Column Mapping",
                "description": "Review all 12 tables' columns (132 total). Map columns to KPIs: e.g., 'Revenue Per Available Room' needs Booking_Amount + Rooms_Available. Create a mapping document.",
                "output": "Excel/CSV: KPI → Required Columns mapping (25 KPIs × relevant columns)",
                "tools": "Excel, Data Dictionary CSV"
            },
            {
                "hour_range": "Hours 9-10 (Student A)",
                "task": "Dashboard Wireframe Analysis",
                "description": "Review 4 dashboard wireframes (Executive, Market, Customer, Operational). Understand which KPIs appear on which dashboard. Sketch data flow: Data → Model → Dashboard.",
                "output": "Dashboard requirements document: listing KPIs, visuals, filters per dashboard",
                "tools": "Dashboard wireframes, PowerPoint/Word"
            },
            {
                "hour_range": "Hours 11-12 (Student B)",
                "task": "Power BI Environment Setup",
                "description": "Download & install Microsoft Power BI Desktop (free). Open program. Practice: import a simple CSV. Create basic report. Get comfortable with interface.",
                "output": "Power BI Desktop operational; screenshot of sample report",
                "tools": "Power BI Desktop, sample CSV"
            },
            {
                "handoff": "Student A's column mapping → needed for synthetic data generation logic; Student B's BI readiness → can start data import in Week 2"
            }
        ],
        "Day 3 - Wednesday": [
            {
                "hour_range": "Hours 13-14 (Student A)",
                "task": "Islamic Calendar & Date Dimension Exploration",
                "description": "Understand Hijri calendar attributes crucial for Dim_Date. Research: when is Ramadan 2025? When is Hajj 2025? Map Gregorian to Hijri dates. Understand seasonal demand multipliers.",
                "output": "Islamic Calendar reference sheet: key dates for 12-18 month period (Ramadan, Hajj, Eid dates)",
                "tools": "Online Islamic calendar converter, research docs"
            },
            {
                "hour_range": "Hours 15-16 (Student A)",
                "task": "Hotel Market Data Gathering",
                "description": "Research: actual hotel prices in Riyadh, Mecca, Jeddah. Hotel star ratings distribution. Budget ($30-60), mid ($60-150), luxury ($150-500+) ranges. Document realistic pricing bands.",
                "output": "Market pricing reference document: 3 cities × 3 price tiers × sample rates",
                "tools": "Booking.com, Agoda, market research docs"
            },
            {
                "hour_range": "Hours 17-18 (Student B)",
                "task": "Data Generation Tools Preparation",
                "description": "Install Python (Anaconda). Install libraries: Faker, SDV, NumPy, Pandas. Run test scripts from documentation. Understand Faker locale for Arabic names ('ar_SA').",
                "output": "Python environment set up; sample Faker script runs successfully (generates 5 fake names)",
                "tools": "Anaconda, Python 3.9+, pip"
            },
            {
                "handoff": "Student A's market data + calendar → inputs for synthetic data generation; Student B's Python setup → ready for Week 2 data generation"
            }
        ]
    },
    "Week 2 - Synthetic Data Generation & Power BI Setup (30 hours: focused on data creation & BI model)": {
        "Day 4 - Thursday": [
            {
                "hour_range": "Hours 19-22 (Student A - 4 hours)",
                "task": "Dimension Table Generation (Dim_Date, Dim_Hotel, Dim_Location)",
                "description": "Write Python scripts to generate:\n- Dim_Date: 18-month calendar with Gregorian + Hijri dates, Ramadan/Hajj flags, seasons\n- Dim_Hotel: 75 hotels across 3 cities, star ratings 3-5, prices, commission rates\n- Dim_Location: 3 cities × 3 districts = 9 locations\nExport as CSV files.",
                "output": "3 CSV files: dim_date.csv, dim_hotel.csv, dim_location.csv",
                "tools": "Python, Faker, script file"
            },
            {
                "hour_range": "Hours 23-24 (Student B - 2 hours)",
                "task": "Additional Dimension Tables (Dim_Customer, Dim_RoomType, Others)",
                "description": "Generate remaining dimensions:\n- Dim_Customer: 8,000 customers with demographics, bookings, spend, segments\n- Dim_RoomType: 16 room categories (Standard, Deluxe, Suite, etc.)\n- Dim_Channel, Dim_Competitor, Dim_LoyaltyTier, Dim_MarketEvent\nExport all as CSV.",
                "output": "7 CSV files: all remaining dimensions",
                "tools": "Python, Faker script"
            },
            {
                "handoff": "All dimension tables ready for fact table generation and Power BI import"
            }
        ],
        "Day 5 - Friday": [
            {
                "hour_range": "Hours 25-28 (Student A - 4 hours)",
                "task": "Fact_Bookings Generation with Business Rules",
                "description": "Generate 15,000 booking records with logic:\n- Booking dates from 18-month range\n- Hotel references to valid Hotel_IDs\n- Customer references to valid Customer_IDs\n- Ramadan/Hajj seasons: 3x normal booking volume in Mecca\n- Pricing: correlate star rating to room rate\n- Cancellation rate: 10% randomly marked as cancelled\nExport as CSV.",
                "output": "fact_bookings.csv (15,000 rows, 20 columns)",
                "tools": "Python script, SDV for relationships"
            },
            {
                "hour_range": "Hours 29-30 (Student B - 2 hours)",
                "task": "Fact_Searches & Fact_Competitor_Prices Generation",
                "description": "Generate:\n- Fact_Searches: 75,000 search queries (related to bookings, seasonal patterns)\n- Fact_Competitor_Prices: 5 × 75 hotels × 7 competitors × 550 days = 287,500 price snapshots (daily prices for each hotel per competitor)\nApply seasonality multipliers.",
                "output": "fact_searches.csv, fact_competitor_prices.csv",
                "tools": "Python script, NumPy for distributions"
            },
            {
                "handoff": "All 3 fact tables ready for Power BI import"
            }
        ],
        "Day 6 - Monday (Week 2)": [
            {
                "hour_range": "Hours 31-34 (Student A - 4 hours)",
                "task": "Data Quality Validation & Cleansing",
                "description": "Run validation checks on all 12 CSVs:\n- Referential integrity: every Hotel_ID in fact tables exists in Dim_Hotel\n- Date consistency: Checkout_Date > Checkin_Date for all bookings\n- Numeric validation: prices >0, occupancy 0-100%, commission 15-25%\n- No negative values, duplicates in primary keys\nDocumented validation report.",
                "output": "Data Quality Validation Report (Word/PDF): pass/fail per table, issues found & fixed",
                "tools": "Python Pandas, validation script"
            },
            {
                "hour_range": "Hours 35-36 (Student B - 2 hours)",
                "task": "Power BI Data Import - Initial Setup",
                "description": "Open Power BI Desktop. Import all 12 CSV files. Review data preview for each. Check data types (Int, Decimal, Text, Date). Make minor type corrections in Power Query if needed.",
                "output": "Power BI file (.pbix) with all 12 tables imported (unrelated yet)",
                "tools": "Power BI Desktop, Power Query"
            },
            {
                "handoff": "Clean validated data + Power BI import → ready for data model building"
            }
        ],
        "Day 7 - Tuesday (Week 2)": [
            {
                "hour_range": "Hours 37-40 (Student A - 4 hours)",
                "task": "Star Schema Implementation in Power BI (Relationships)",
                "description": "In Power BI Desktop, create relationships (foreign keys):\n- Fact_Bookings → Dim_Hotel (Hotel_ID)\n- Fact_Bookings → Dim_Customer (Customer_ID)\n- Fact_Bookings → Dim_Date (Booking_Date_ID, CheckIn_Date_ID, CheckOut_Date_ID) [role-playing dates]\n- Similar for Fact_Searches, Fact_Competitor_Prices\nSet cardinality (1:Many) correctly. Hide foreign key columns from end users.",
                "output": "Power BI model with all relationships configured; Model view showing star schema",
                "tools": "Power BI Desktop, Data Model view"
            },
            {
                "hour_range": "Hours 41-42 (Student B - 2 hours)",
                "task": "Power BI Calculated Columns - Prepare Data for KPIs",
                "description": "Create calculated columns (derived data):\n- Booking_Duration = CheckOut_Date - CheckIn_Date\n- Commission_Amount = Booking_Amount × Commission_Rate\n- Days_to_Checkin = CheckIn_Date - Booking_Date\n- Season_Label = LOOKUPVALUE from Dim_Date's Season_Type\nFormat columns for calculations.",
                "output": "Power BI file with 4-6 calculated columns added to Fact_Bookings",
                "tools": "Power BI Desktop, DAX formulas"
            },
            {
                "handoff": "Schema implemented + calculated columns ready for KPI measure creation in Week 3"
            }
        ]
    },
    "Week 3 - DAX Measures & KPI Development (30 hours: focused on Power BI calculations)": {
        "Day 8 - Wednesday (Week 2)": [
            {
                "hour_range": "Hours 43-46 (Student A - 4 hours)",
                "task": "Revenue Performance KPIs (7 measures)",
                "description": "Create DAX measures for:\n1. [RevPAR] = SUM([Booking_Amount]) / DISTINCTCOUNT([Hotel_ID])\n2. [Total Commission Revenue] = SUMPRODUCT([Booking_Amount], [Commission %])\n3. [Average Booking Value] = DIVIDE([Total Booking Revenue], COUNTA([Booking_ID]))\n4. [Revenue Per Booking] = [Commission Revenue] / COUNTA([Booking_ID])\n5. [Revenue Per Customer] = [Commission Revenue] / DISTINCTCOUNT([Customer_ID])\n6. [Gross Booking Value] = SUM([Booking_Amount])\n7. [ADR] = [Total Room Revenue] / SUM([Booking_Duration_Nights])\nTest each formula with sample data.",
                "output": "Power BI file with 7 DAX measures (Revenue category)",
                "tools": "Power BI DAX editor"
            },
            {
                "hour_range": "Hours 47-48 (Student B - 2 hours)",
                "task": "Customer Behavior KPIs (6 measures) - Part 1",
                "description": "Create first 3 measures:\n1. [Conversion Rate %] = DIVIDE([Booking Count], [Search Count], 0) * 100\n2. [Booking Lead Time Days] = AVERAGEX([Bookings], [Checkin_Date] - [Booking_Date])\n3. [Customer Lifetime Value] = [Revenue Per Customer] * [Years_as_Customer] - [Acquisition_Cost]\nTest formulas against sample customer data.",
                "output": "Power BI file with 3 DAX measures (Customer Behavior category)",
                "tools": "Power BI DAX editor"
            },
            {
                "handoff": "Revenue KPIs + first Customer KPIs → used in dashboards starting Week 4"
            }
        ],
        "Day 9 - Thursday (Week 2)": [
            {
                "hour_range": "Hours 49-52 (Student A - 4 hours)",
                "task": "Customer Behavior KPIs (Part 2) + Operational Efficiency KPIs",
                "description": "Complete 3 remaining Customer KPIs:\n4. [Repeat Customer Rate %] = DIVIDE(COUNTIF([Bookings >= 2]), DISTINCTCOUNT([Customer_ID])) * 100\n5. [Cart Abandonment Rate %] = DIVIDE([Searches] - [Bookings], [Searches]) * 100\n6. [Search-to-Book Ratio] = [Booking Count] / [Search Count]\n\nStart Operational Efficiency (6 measures):\n1. [Cancellation Rate %] = DIVIDE(COUNTIF([Status] = 'Cancelled'), [Booking Count]) * 100\n2. [Payment Success Rate %] = DIVIDE(COUNTIF([Payment_Status] = 'Success'), [Payment Attempts]) * 100",
                "output": "Power BI file with additional 8 measures",
                "tools": "Power BI DAX editor"
            },
            {
                "hour_range": "Hours 53-54 (Student B - 2 hours)",
                "task": "Operational Efficiency KPIs (Part 2) + Competitive Position KPIs",
                "description": "Complete 4 remaining Operational measures:\n3. [Inventory Utilization %] = DIVIDE([Rooms Booked], [Rooms Available]) * 100\n4. [Avg Response Time Hours] = AVERAGE([Support_Response_Time])\n5. [Error Rate %] = DIVIDE([Failed Bookings], [Booking Attempts]) * 100\n6. [Support Tickets per 1000 Bookings] = DIVIDE([Ticket Count], [Booking Count]) * 1000\n\nStart 6 Competitive KPIs.",
                "output": "Power BI file with 10+ additional measures across all categories",
                "tools": "Power BI DAX editor"
            },
            {
                "handoff": "Nearly all 25 KPIs defined and tested → ready for dashboard visualization"
            }
        ],
        "Day 10 - Friday (Week 2)": [
            {
                "hour_range": "Hours 55-58 (Student A - 4 hours)",
                "task": "Complete Competitive Position KPIs (6 measures)",
                "description": "Create final 6 measures:\n1. [Price Competitiveness Index] = DIVIDE([Our ADR], [Competitor Avg ADR]) * 100\n2. [Market Share by City %] = DIVIDE([Our Bookings], [Total Market Bookings]) * 100\n3. [Inventory Overlap %] = DIVIDE([Hotels Listed on Competitor], [Our Total Hotels]) * 100\n4. [Feature Parity Score %] = DIVIDE([Our Features], [Max Competitor Features]) * 100\n5. [Review Score Delta] = [Our Avg Review] - [Competitor Avg Review]\n6. [Commission Competitiveness Index] = DIVIDE([Our Rate %], [Industry Avg Rate %]) * 100\n\nTest all measures.",
                "output": "Power BI file with ALL 25 KPIs complete",
                "tools": "Power BI DAX editor"
            },
            {
                "hour_range": "Hours 59-60 (Student B - 2 hours)",
                "task": "KPI Testing & Documentation",
                "description": "For each KPI: test with sample slicers (by City, by Month, by Hotel Star Rating). Verify results make sense (e.g., RevPAR increases in Mecca during Hajj). Document expected vs. actual values.",
                "output": "KPI Test Results document: 25 KPIs × 3 scenarios = 75 test cases (pass/fail)",
                "tools": "Power BI, Word/Excel"
            },
            {
                "handoff": "All 25 KPIs tested and ready for dashboard build. Clean Power BI file with proven measures → Week 4 dashboard development"
            }
        ]
    },
    "Week 4 - Dashboard Development & Project Completion (32 hours)": {
        "Day 11 - Monday (Week 3)": [
            {
                "hour_range": "Hours 61-64 (Student A - 4 hours)",
                "task": "Executive Overview Dashboard - Part 1 (KPIs + Trend Analysis)",
                "description": "Build Executive Dashboard Page 1:\n- Top row: 5 KPI cards (Total Revenue, Booking Count, Avg Value, Occupancy, Market Share) with sparklines\n- Center: Line chart (Revenue trend by Month, with forecast)\n- Add slicers: Date Range (Month/Quarter), City (Riyadh/Mecca/Jeddah), Star Rating\nStyle: professional blue/orange, white background, sans-serif font.",
                "output": "Power BI report page: Executive Overview Dashboard (upper section)",
                "tools": "Power BI report designer"
            },
            {
                "hour_range": "Hours 65-66 (Student B - 2 hours)",
                "task": "Executive Overview Dashboard - Part 2 (Competitive Positioning)",
                "description": "Add to same dashboard:\n- Competitive Position Matrix: scatter plot (Our ADR vs. Market ADR, bubble size = market share)\n- Competitor Pricing Table: show top 5 competitors' avg rates vs. ours by city\n- Geographic map: bookings by location (heat map)\nConfigure cross-filtering: clicking a city updates all visuals.",
                "output": "Power BI Executive Dashboard (complete, all visuals + interactivity)",
                "tools": "Power BI"
            },
            {
                "handoff": "Executive dashboard finished → used by leadership for strategic decisions"
            }
        ],
        "Day 12 - Tuesday (Week 3)": [
            {
                "hour_range": "Hours 67-70 (Student A - 4 hours)",
                "task": "Market Analysis Dashboard",
                "description": "Create new report page - Market Analysis:\n- Market share by city (pie/bar chart, %; drill-through to district level)\n- Competitor pricing comparison heatmap (hotel × competitor × ADR)\n- Seasonal demand line chart: Hajj/Ramadan/Eid highlighted\n- Inventory overlap matrix: which hotels listed on which competitors\nSlicers: Date, Competitor, Star Rating",
                "output": "Power BI Market Analysis Dashboard page (all 4 visuals)",
                "tools": "Power BI"
            },
            {
                "hour_range": "Hours 71-72 (Student B - 2 hours)",
                "task": "Customer Insights Dashboard",
                "description": "Create new report page - Customer Insights:\n- Customer segmentation (Business, Leisure, Religious, Family) - bar/donut chart with counts & revenue\n- Loyalty tier distribution & CLV by tier\n- Booking behavior histograms: lead time distribution, length of stay distribution\n- Repeat customer trends (% repeat over time - line chart)\nSlicers: Date Range, City, Customer Segment",
                "output": "Power BI Customer Insights Dashboard page (all 4 visuals)",
                "tools": "Power BI"
            },
            {
                "handoff": "Two more dashboards complete → marketing & customer teams ready to use"
            }
        ],
        "Day 13 - Wednesday (Week 3)": [
            {
                "hour_range": "Hours 73-76 (Student A - 4 hours)",
                "task": "Operational Performance Dashboard",
                "description": "Create new report page - Operational Performance:\n- Search-to-book funnel (waterfall or steps chart): searches → results viewed → cart created → checkout started → booked\n- Inventory utilization by hotel type (Standard/Deluxe/Suite) - clustered bar\n- Cancellation rate trends by month & reason\n- Error/failure tracking (payment failed, system errors) - KPI card + line trend\nSlicers: Date, Hotel Star Rating, Channel",
                "output": "Power BI Operational Performance Dashboard page (all 4 visuals)",
                "tools": "Power BI"
            },
            {
                "hour_range": "Hours 77-78 (Student B - 2 hours)",
                "task": "Dashboard Refinement & Polish",
                "description": "Cross all 4 dashboards:\n- Standardize colors (corporate blue #003366, accent orange #FF6600, gray text)\n- Add report title/date footer on each page\n- Add 'Last Updated' timestamp\n- Configure tooltips (hover details)\n- Test responsive design (mobile view) for Executive dashboard\n- Add hyperlinks between dashboards (e.g., Executive → drill into Market dashboard)",
                "output": "Polished 4-dashboard Power BI report (.pbix file)",
                "tools": "Power BI"
            },
            {
                "handoff": "All 4 dashboards complete, styled, and interactive → ready for demo & documentation"
            }
        ],
        "Day 14 - Thursday (Week 3)": [
            {
                "hour_range": "Hours 79-82 (Student A - 4 hours)",
                "task": "Documentation - Data Dictionary & Model Guide",
                "description": "Create comprehensive documentation:\n1. Data Dictionary (Word/PDF): All 12 tables, all 132 columns, definitions, sample values, business rules\n2. Star Schema Diagram: visual + textual explanation of relationships\n3. DAX Measure Catalog: all 25 KPIs with formulas, expected ranges, refresh frequency\n4. Assumption document: synthetic data specifics (hotels 75, customers 8k, bookings 15k, etc.)",
                "output": "3-4 Word/PDF documents totaling 30-40 pages",
                "tools": "Word, screenshots from Power BI"
            },
            {
                "hour_range": "Hours 83-84 (Student B - 2 hours)",
                "task": "User Guide & Dashboard Training Document",
                "description": "Create end-user guide:\n1. Dashboard User Guide (Word): How to use each dashboard, what each KPI means, how to filter/drill\n2. Power BI 101 for Stakeholders: basic BI concepts explained simply\n3. Troubleshooting guide: common issues & fixes\n4. Data refresh schedule & support contact info",
                "output": "User Guide (10-15 pages), easily understood by non-technical users",
                "tools": "Word"
            },
            {
                "handoff": "Documentation complete → stakeholders can understand and use dashboards independently"
            }
        ],
        "Day 15 - Friday (Week 3)": [
            {
                "hour_range": "Hours 85-88 (Student A - 4 hours)",
                "task": "Testing & Quality Assurance",
                "description": "QA testing checklist:\n1. Functional tests: do all slicers work? Do filters update visuals correctly?\n2. Calculation tests: spot-check 5 KPIs manually (Excel calc vs. Power BI)\n3. Data accuracy: does Mecca bookings spike in Hajj season? Yes/No?\n4. Performance: does each dashboard load in <3 seconds?\n5. Aesthetic: colors consistent, no typos, fonts readable\n6. Cross-filter: clicking one visual updates others correctly\nDocument pass/fail for each test.",
                "output": "QA Test Report (Excel/Word): 50+ tests, 95%+ pass rate",
                "tools": "Power BI, Excel, testing template"
            },
            {
                "hour_range": "Hours 89-90 (Student B - 2 hours)",
                "task": "Final Presentation Prep & Demo Walkthrough",
                "description": "Prepare 15-minute demo/presentation:\n1. Practice navigating each dashboard (2 min × 4 = 8 min)\n2. Key findings to highlight (e.g., 'Mecca market dominates during Hajj', 'Conversion rate 3.2%')\n3. Create demo script with talking points\n4. Record screen walkthrough (optional, 5 min) showing all 4 dashboards\n5. Prepare 1-page summary (executive summary of insights)",
                "output": "Demo script, screen recording (.mp4), 1-page executive summary",
                "tools": "PowerPoint, Camtasia or OBS for recording"
            },
            {
                "handoff": "Project complete. Ready for presentation to instructors/stakeholders."
            }
        ]
    },
    "Final Summary": {
        "Total Hours": "120 hours (6 hours/day × 20 working days)",
        "Student A (4h/day)": "80 hours - Data generation, data model, KPI development, dashboard building, testing, documentation",
        "Student B (2h/day)": "40 hours - Scope review, BI setup, data validation, calculated columns, complementary dashboard work, user guide, presentation prep",
        "Deliverables": [
            "1 Power BI report file (.pbix) with 4 dashboards, 25 KPIs, star schema model",
            "12 synthetic data CSVs (3 fact tables, 9 dimension tables)",
            "Complete documentation (data dictionary, schema guide, DAX catalog, user guide)",
            "QA test report (50+ tests)",
            "15-minute presentation with screen recording"
        ],
        "Key Milestones": [
            "Day 3 (Friday Week 1): All deliverables reviewed, tools installed",
            "Day 7 (Tuesday Week 2): All 12 CSVs generated, validated, imported into Power BI",
            "Day 10 (Friday Week 2): All 25 KPIs created and tested",
            "Day 14 (Thursday Week 3): All 4 dashboards built, complete documentation written",
            "Day 15 (Friday Week 3): Final testing, presentation ready"
        ]
    }
}

# Export to CSV format for easy viewing
timeline_flat = []
current_day = ""
current_week = ""

for week_key, days_dict in timeline_data.items():
    if "Summary" in week_key:
        continue
    for day_key, tasks_list in days_dict.items():
        for task_dict in tasks_list:
            timeline_flat.append({
                'Week': week_key.split(' - ')[0],
                'Day': day_key,
                'Hour Range': task_dict.get('hour_range', ''),
                'Task': task_dict.get('task', ''),
                'Description': task_dict.get('description', '')[:100] + '...' if len(task_dict.get('description', '')) > 100 else task_dict.get('description', ''),
                'Expected Output': task_dict.get('output', '')
            })

timeline_df = pd.DataFrame(timeline_flat)

print("✅ 120-HOUR PROJECT TIMELINE - 20 WORKING DAYS\n")
print(f"Total Days: 15 (across 3 weeks)")
print(f"Student A: 4 hours/day × 20 days = 80 hours")
print(f"Student B: 2 hours/day × 20 days = 40 hours")
print(f"Total: 120 hours\n")

print(timeline_df.to_string(index=False))

timeline_df.to_csv('hotel_ota_120hour_timeline.csv', index=False)
print("\n✅ Exported: hotel_ota_120hour_timeline.csv")
