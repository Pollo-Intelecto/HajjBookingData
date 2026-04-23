
import pandas as pd
import json
from datetime import datetime, timedelta

# Create complete KPI catalog
kpis_data = {
    "Revenue Performance KPIs": [
        {
            "kpi_id": "REV_001",
            "name": "Revenue Per Available Room (RevPAR)",
            "simple_definition": "How much revenue is earned from each available room, whether sold or empty. Think of it like: if you have 100 rooms and earn $10,000 total, RevPAR = $100.",
            "why_it_matters": "Shows how efficiently your hotel property generates revenue from its room inventory. Higher RevPAR means you're making better use of your physical space.",
            "business_value": "Helps pricing decisions: if RevPAR is low, you may need to lower prices or attract more customers. Used to compare hotel performance to competitors.",
            "formula": "RevPAR = Total Room Revenue ÷ Total Rooms Available",
            "dax_formula": "[RevPAR] = DIVIDE([Total Room Revenue], [Rooms Available], 0)",
            "target_range": "$40-$150 (budget: $40-60, mid-range: $60-120, luxury: $120-150+)",
            "data_required": ["Total Room Revenue (from Fact_Bookings)", "Total Rooms Available (from Dim_Hotel)"],
            "calculation_frequency": "Daily / Weekly / Monthly"
        },
        {
            "kpi_id": "REV_002",
            "name": "Total Commission Revenue",
            "simple_definition": "Total money earned from commissions on all bookings. OTAs make money by taking a percentage fee (typically 15-25%) from each hotel booking.",
            "why_it_matters": "This is the OTA's main revenue source. Growing commission revenue means the business is scaling and becoming profitable.",
            "business_value": "Determines business viability; without healthy commission revenue, the OTA cannot sustain operations. Tracks top-line business growth.",
            "formula": "Commission Revenue = SUM(Booking Amount × Commission Percentage)",
            "dax_formula": "[Commission Revenue] = SUMPRODUCT([Booking Amount], [Commission %])",
            "target_range": "15-25% of Gross Booking Value (varies by hotel partner agreement)",
            "data_required": ["Booking Amount (Fact_Bookings)", "Commission % (Dim_Competitor or negotiated rate)"],
            "calculation_frequency": "Daily / Monthly / Quarterly"
        },
        {
            "kpi_id": "REV_003",
            "name": "Average Booking Value (ABV)",
            "simple_definition": "Average amount a customer pays per booking. If 100 customers book and spend $20,000 total, ABV = $200.",
            "why_it_matters": "Reflects customer willingness to pay and hotel quality mix. Higher ABV may indicate luxury segment success or seasonal premium pricing.",
            "business_value": "Guides pricing strategy and customer segmentation. Helps identify which customer segments are most valuable.",
            "formula": "ABV = Total Booking Revenue ÷ Number of Bookings",
            "dax_formula": "[ABV] = DIVIDE([Total Booking Revenue], COUNTA([Booking ID]), 0)",
            "target_range": "$70-$400 (depends heavily on city: Mecca Hajj can see $300+, Riyadh business typical $100-200)",
            "data_required": ["Total Booking Revenue (Fact_Bookings)", "Booking Count (Fact_Bookings)"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "REV_004",
            "name": "Revenue Per Booking",
            "simple_definition": "Average revenue earned by the OTA per booking transaction (commission revenue only).",
            "why_it_matters": "Measures OTA's earnings efficiency per transaction. Helps optimize commission structures and hotel partnerships.",
            "business_value": "Determines if commission rate is sustainable; if too low, partnerships become unprofitable.",
            "formula": "Revenue Per Booking = Total Commission Revenue ÷ Total Bookings",
            "dax_formula": "[Revenue Per Booking] = DIVIDE([Commission Revenue], [Booking Count], 0)",
            "target_range": "$10-$100 per booking (depends on commission % and ABV)",
            "data_required": ["Commission Revenue", "Booking Count"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "REV_005",
            "name": "Revenue Per Customer",
            "simple_definition": "Total revenue generated from each customer on average. Tracks how much value each customer brings to the OTA.",
            "why_it_matters": "Identifies most valuable customer segments and guides marketing spend. A customer worth $500 needs different treatment than one worth $50.",
            "business_value": "Drives customer acquisition and retention strategies. Helps prioritize loyalty program focus.",
            "formula": "Revenue Per Customer = Total Commission Revenue ÷ Unique Customers",
            "dax_formula": "[Revenue Per Customer] = DIVIDE([Commission Revenue], DISTINCTCOUNT([Customer ID]), 0)",
            "target_range": "$50-$500 (highly variable by loyalty tier and booking frequency)",
            "data_required": ["Commission Revenue", "Unique Customer Count"],
            "calculation_frequency": "Monthly / Quarterly"
        },
        {
            "kpi_id": "REV_006",
            "name": "Gross Booking Value (GBV)",
            "simple_definition": "Total value of all bookings before any deductions or commissions. Raw transaction volume in dollars.",
            "why_it_matters": "Indicates total market volume the OTA is transacting. Growing GBV = business expansion.",
            "business_value": "Top-line metric for board/investor reporting. Shows market penetration and competitive positioning.",
            "formula": "GBV = SUM(All Booking Amounts)",
            "dax_formula": "[GBV] = SUM([Booking Amount])",
            "target_range": "$100,000-$5,000,000/month (depends on scale: startup vs. established player)",
            "data_required": ["Booking Amount (Fact_Bookings)"],
            "calculation_frequency": "Daily / Monthly"
        },
        {
            "kpi_id": "REV_007",
            "name": "Average Daily Rate (ADR)",
            "simple_definition": "Average nightly room rate across all bookings. If 100 nights are sold at rates ranging $50-200, ADR = average of all rates.",
            "why_it_matters": "Shows pricing power and hotel quality mix. Rising ADR (without volume loss) = healthy business.",
            "business_value": "Competitive benchmarking tool. Compare your ADR to competitors' to assess pricing strategy effectiveness.",
            "formula": "ADR = Total Room Revenue ÷ Total Nights Booked",
            "dax_formula": "[ADR] = DIVIDE([Total Room Revenue], [Total Nights Booked], 0)",
            "target_range": "$50-$300/night (Mecca Hajj: $200+, Riyadh business: $100-150, Jeddah leisure: $80-150)",
            "data_required": ["Total Room Revenue", "Total Nights Booked (Fact_Bookings)"],
            "calculation_frequency": "Daily / Weekly"
        }
    ],
    "Customer Behavior KPIs": [
        {
            "kpi_id": "CUST_001",
            "name": "Conversion Rate (Search to Booking)",
            "simple_definition": "% of people who search for hotels that actually complete a booking. If 1000 people search and 20 book, conversion = 2%.",
            "why_it_matters": "Measures effectiveness of OTA's website/app in turning interest into sales. Low conversion = bad UX or pricing issues.",
            "business_value": "Guides product improvements. A 1% improvement in conversion can increase revenue 10%+ without more marketing spend.",
            "formula": "Conversion Rate = (Bookings ÷ Searches) × 100",
            "dax_formula": "[Conversion Rate %] = DIVIDE([Booking Count], [Search Count], 0) * 100",
            "target_range": "2-5% (industry average: 2-3%, luxury hotels: 3-5%, budget: 1-2%)",
            "data_required": ["Booking Count (Fact_Bookings)", "Search Count (Fact_Searches)"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "CUST_002",
            "name": "Booking Lead Time",
            "simple_definition": "Average number of days before check-in that a booking is made. If someone books 14 days before arrival, lead time = 14 days.",
            "why_it_matters": "Helps forecast demand and plan inventory. Last-minute bookers vs. planners need different marketing approaches.",
            "business_value": "Enables revenue management: last-minute bookings can command premium prices, while advance bookings drive volume.",
            "formula": "Booking Lead Time = AVG(Check-In Date - Booking Date)",
            "dax_formula": "[Avg Lead Time Days] = AVERAGEX([Fact_Bookings], [Days_Between_Booking_And_Checkin])",
            "target_range": "14-30 days average (ranges: last-minute 0-3 days, advance 30+ days)",
            "data_required": ["Booking Date (Fact_Bookings)", "Check-In Date (Fact_Bookings)"],
            "calculation_frequency": "Weekly / Monthly"
        },
        {
            "kpi_id": "CUST_003",
            "name": "Customer Lifetime Value (CLV)",
            "simple_definition": "Total revenue a customer is expected to generate over their entire relationship with the OTA.",
            "why_it_matters": "Identifies high-value customers worth investing in. A customer with $500 CLV justifies $100+ acquisition spend.",
            "business_value": "Drives loyalty program ROI. Focus on customers with high CLV for retention efforts.",
            "formula": "CLV = (Avg Revenue Per Customer) × (Years as Customer) - (Acquisition Cost)",
            "dax_formula": "[CLV] = ([Revenue Per Customer] * [Years as Customer] - [Acquisition Cost])",
            "target_range": "$200-$2000 (high-value loyalty members: $1000+, occasional bookers: $200-500)",
            "data_required": ["Revenue Per Customer", "Customer Age", "Acquisition Cost"],
            "calculation_frequency": "Monthly / Quarterly"
        },
        {
            "kpi_id": "CUST_004",
            "name": "Repeat Customer Rate",
            "simple_definition": "% of customers who have made more than one booking. If 1000 customers have booked, and 200 booked twice+, repeat rate = 20%.",
            "why_it_matters": "High repeat rate = customer satisfaction and brand loyalty. New customers are expensive to acquire; repeat customers are profitable.",
            "business_value": "Indicates product-market fit. Guides loyalty program investment decisions.",
            "formula": "Repeat Customer Rate = (Customers with 2+ Bookings ÷ Total Customers) × 100",
            "dax_formula": "[Repeat Customer %] = DIVIDE(COUNTIF([Booking Count] >= 2), DISTINCTCOUNT([Customer ID]), 0) * 100",
            "target_range": "20-40% (startups: 10-20%, mature platforms: 40-50%)",
            "data_required": ["Customer ID (Fact_Bookings)", "Booking Count per Customer"],
            "calculation_frequency": "Monthly / Quarterly"
        },
        {
            "kpi_id": "CUST_005",
            "name": "Cart Abandonment Rate",
            "simple_definition": "% of customers who add a booking to cart but don't complete checkout. If 100 carts started and 80 completed, abandonment = 20%.",
            "why_it_matters": "Identifies friction in checkout process. High abandonment = broken payment, unclear pricing, technical issues.",
            "business_value": "Quick wins for revenue: even 5% reduction in abandonment = 5% revenue increase with no marketing.",
            "formula": "Abandonment Rate = ((Carts Initiated - Bookings Completed) ÷ Carts Initiated) × 100",
            "dax_formula": "[Abandonment Rate %] = DIVIDE(([Carts Initiated] - [Bookings Completed]), [Carts Initiated], 0) * 100",
            "target_range": "20-40% (industry average: 25-30%, optimized platforms: 15-20%)",
            "data_required": ["Carts Initiated (Fact_Searches)", "Bookings Completed (Fact_Bookings)"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "CUST_006",
            "name": "Search-to-Book Ratio",
            "simple_definition": "For every search, how many bookings result? If 1000 searches yield 50 bookings, ratio = 1:20 (or 5%).",
            "why_it_matters": "Overall funnel health metric. Combines conversion + cart abandonment effects.",
            "business_value": "Monitors end-to-end UX effectiveness. Trends show if product improvements are working.",
            "formula": "Search-to-Book Ratio = Bookings ÷ Searches",
            "dax_formula": "[Search to Book Ratio] = DIVIDE([Booking Count], [Search Count], 0)",
            "target_range": "1:20 to 1:40 (industry: 1:25, high-performing: 1:15)",
            "data_required": ["Booking Count", "Search Count"],
            "calculation_frequency": "Daily / Weekly"
        }
    ],
    "Operational Efficiency KPIs": [
        {
            "kpi_id": "OPS_001",
            "name": "Cancellation Rate",
            "simple_definition": "% of bookings that are cancelled (by customer or hotel). If 1000 bookings occur and 100 are cancelled, rate = 10%.",
            "why_it_matters": "High cancellations = revenue loss + inventory uncertainty. Impacts revenue forecasting.",
            "business_value": "Guides cancellation policy design. Flexible policies attract bookings but increase risk; strict policies reduce bookings.",
            "formula": "Cancellation Rate = (Cancelled Bookings ÷ Total Bookings) × 100",
            "dax_formula": "[Cancellation Rate %] = DIVIDE(COUNTIF([Reservation Status] = 'Cancelled'), [Booking Count], 0) * 100",
            "target_range": "8-15% (industry average: 10%, luxury: 5-8%, budget: 12-15%)",
            "data_required": ["Reservation Status (Fact_Bookings)", "Booking Count"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "OPS_002",
            "name": "Payment Success Rate",
            "simple_definition": "% of payment attempts that succeed without error. If 100 payments attempted, 98 succeed, rate = 98%.",
            "why_it_matters": "Payment failures = lost revenue + customer frustration. Below 95% is critical issue.",
            "business_value": "Identifies payment gateway issues. Guides provider selection/support improvements.",
            "formula": "Payment Success Rate = (Successful Payments ÷ Payment Attempts) × 100",
            "dax_formula": "[Payment Success Rate %] = DIVIDE(COUNTIF([Payment Status] = 'Success'), [Payment Attempts], 0) * 100",
            "target_range": "95-99% (below 95%: major issue; above 99%: excellent)",
            "data_required": ["Payment Status (Fact_Bookings)", "Payment Attempt Count"],
            "calculation_frequency": "Daily / Real-time"
        },
        {
            "kpi_id": "OPS_003",
            "name": "Inventory Utilization Rate",
            "simple_definition": "% of available rooms that are booked. If 1000 rooms available on a night and 700 are booked, utilization = 70%.",
            "why_it_matters": "Shows how well OTA is filling hotel inventory. Also called 'occupancy rate' from hotel perspective.",
            "business_value": "Guides pricing: low utilization = lower prices needed; high utilization = raise prices.",
            "formula": "Utilization Rate = (Rooms Booked ÷ Rooms Available) × 100",
            "dax_formula": "[Inventory Utilization %] = DIVIDE([Rooms Booked], [Rooms Available], 0) * 100",
            "target_range": "60-90% (varies by city: Mecca Hajj 90%+, Riyadh off-peak 40-60%)",
            "data_required": ["Rooms Booked (Fact_Bookings)", "Rooms Available (Dim_Hotel)"],
            "calculation_frequency": "Daily"
        },
        {
            "kpi_id": "OPS_004",
            "name": "Average Response Time",
            "simple_definition": "Average time (in hours) for customer support to respond to inquiries. If avg response is 2 hours, that's the metric.",
            "why_it_matters": "Fast response = happy customers = positive reviews = more bookings.",
            "business_value": "Drives NPS (Net Promoter Score) and review ratings. Guides staffing decisions.",
            "formula": "Avg Response Time = AVG(Response Time per Ticket)",
            "dax_formula": "[Avg Response Time Hours] = AVERAGE([Response_Time_Hours])",
            "target_range": "1-4 hours (best practice: <2 hours)",
            "data_required": ["Response Time per Support Ticket"],
            "calculation_frequency": "Daily / Weekly"
        },
        {
            "kpi_id": "OPS_005",
            "name": "Error Rate (Failed Bookings)",
            "simple_definition": "% of booking attempts that fail due to technical/system errors (not user cancellation). If 100 attempts, 2 fail = 2% error rate.",
            "why_it_matters": "System reliability metric. High errors = lost sales + poor UX.",
            "business_value": "Guides infrastructure/platform investments. Identifies critical bugs.",
            "formula": "Error Rate = (Failed Bookings ÷ Booking Attempts) × 100",
            "dax_formula": "[Error Rate %] = DIVIDE(COUNTIF([Booking Status] = 'Failed'), [Booking Attempts], 0) * 100",
            "target_range": "0.5-2% (below 0.5%: excellent; above 2%: critical issue)",
            "data_required": ["Booking Status (Fact_Bookings)"],
            "calculation_frequency": "Real-time / Daily"
        },
        {
            "kpi_id": "OPS_006",
            "name": "Customer Support Tickets per 1000 Bookings",
            "simple_definition": "How many support issues arise per 1000 bookings made. If 10,000 bookings generate 100 tickets, ratio = 10 per 1000.",
            "why_it_matters": "Indicates product quality and UX. High tickets = unhappy customers / buggy product.",
            "business_value": "Prioritizes product fixes. Guides staffing needs for support team.",
            "formula": "Support Ticket Ratio = (Support Tickets ÷ Bookings) × 1000",
            "dax_formula": "[Support Tickets per 1000 Bookings] = DIVIDE([Support Ticket Count], [Booking Count], 0) * 1000",
            "target_range": "5-15 per 1000 (low: <10 indicates good product; high: >20 indicates serious issues)",
            "data_required": ["Support Ticket Count", "Booking Count"],
            "calculation_frequency": "Weekly / Monthly"
        }
    ],
    "Competitive Position KPIs": [
        {
            "kpi_id": "COMP_001",
            "name": "Price Competitiveness Index",
            "simple_definition": "How your prices compare to competitors. Index of 100 = same price, 90 = you're 10% cheaper, 110 = you're 10% more expensive.",
            "why_it_matters": "Shows pricing strategy effectiveness. Being 10% cheaper attracts price-sensitive customers.",
            "business_value": "Guides pricing adjustments. Tells you if you can raise prices or need to drop them.",
            "formula": "Price Index = (Your ADR ÷ Competitor Avg ADR) × 100",
            "dax_formula": "[Price Competitiveness Index] = DIVIDE([Our ADR], [Competitor Avg ADR], 100) * 100",
            "target_range": "95-105 (below 95: very competitive/risky; 105+: premium positioning)",
            "data_required": ["Your ADR (Fact_Bookings)", "Competitor ADR (Fact_Competitor_Prices)"],
            "calculation_frequency": "Daily"
        },
        {
            "kpi_id": "COMP_002",
            "name": "Market Share by City",
            "simple_definition": "% of total bookings in a city that come through your OTA. If 1000 total bookings in Riyadh and you have 200, your market share = 20%.",
            "why_it_matters": "Shows competitive position. Growing market share = winning customers from rivals.",
            "business_value": "Strategic focus area. If market share is declining, urgent action needed.",
            "formula": "Market Share = (Your Bookings ÷ Total Market Bookings) × 100",
            "dax_formula": "[Market Share %] = DIVIDE([Your Booking Count], [Total Market Bookings], 0) * 100",
            "target_range": "Startup: 5-15%, growing: 15-30%, established: 30%+",
            "data_required": ["Your Booking Count (Fact_Bookings)", "Competitor Booking Counts (estimated from Fact_Competitor_Prices)"],
            "calculation_frequency": "Monthly"
        },
        {
            "kpi_id": "COMP_003",
            "name": "Inventory Overlap with Competitors",
            "simple_definition": "% of hotels listed on your platform that are also listed on each competitor platform.",
            "why_it_matters": "Shows hotel partnership strategy. High overlap = harder to differentiate; low overlap = exclusive advantage.",
            "business_value": "Guides hotel acquisition strategy. Exclusive hotels = competitive moat.",
            "formula": "Overlap % = (Overlapping Hotels ÷ Your Total Hotels) × 100",
            "dax_formula": "[Inventory Overlap %] = DIVIDE(COUNTIF([Listed on Competitor] = TRUE), [Total Hotels], 0) * 100",
            "target_range": "60-90% (most hotels multi-list; <60% suggests niche/exclusive focus)",
            "data_required": ["Hotel Listing Status across Competitors"],
            "calculation_frequency": "Monthly / Quarterly"
        },
        {
            "kpi_id": "COMP_004",
            "name": "Feature Parity Score",
            "simple_definition": "Score (1-10 or %) showing how many features your platform has vs. top 5 competitors. Covers: filters, payment options, mobile, cancellation flexibility.",
            "why_it_matters": "Shows if your product is competitive. Missing key features = customers go to better platforms.",
            "business_value": "Product roadmap prioritization. Identifies must-have features vs. nice-to-haves.",
            "formula": "Feature Parity = (Your Feature Count ÷ Competitor Max Feature Count) × 100",
            "dax_formula": "[Feature Parity Score] = DIVIDE([Your Feature Count], [Competitor Max Feature Count], 0) * 100",
            "target_range": "70-100% (below 70%: critical gaps; 100%: feature leader)",
            "data_required": ["Your Feature List", "Competitor Feature Lists"],
            "calculation_frequency": "Quarterly"
        },
        {
            "kpi_id": "COMP_005",
            "name": "Average Review Score vs Competitors",
            "simple_definition": "Your average guest review rating (1-5 stars) compared to competitors. If you avg 4.2 and competitors avg 4.0, you're leading.",
            "why_it_matters": "Guest satisfaction drives bookings. Higher reviews = higher conversion.",
            "business_value": "Quality/service differentiator. Guides customer experience improvements.",
            "formula": "Review Score Advantage = Your Avg Score - Competitor Avg Score",
            "dax_formula": "[Review Score Delta] = [Our Avg Review] - [Competitor Avg Review]",
            "target_range": "+0.3 to +0.5 is competitive advantage; -0.2 or lower is concerning",
            "data_required": ["Review Scores (from hotel partners/OTA data)", "Competitor Review Scores (from Agoda/Booking scrape)"],
            "calculation_frequency": "Monthly"
        },
        {
            "kpi_id": "COMP_006",
            "name": "Commission Competitiveness",
            "simple_definition": "Your commission rate vs. industry average. If you charge 18% and industry average is 20%, you're competitive.",
            "why_it_matters": "Affects hotel willingness to list. Lower commission = more hotel partners; but revenue suffers.",
            "business_value": "Hotel acquisition lever. Guides pricing of partnerships.",
            "formula": "Commission Competitiveness = Your Rate ÷ Industry Avg Rate × 100",
            "dax_formula": "[Commission Competitiveness Index] = DIVIDE([Our Commission %], [Industry Avg Commission %], 0) * 100",
            "target_range": "90-110 (below 90: very competitive; 110+: premium/selective approach)",
            "data_required": ["Your Commission % (from Hotel agreements)", "Industry Avg Commission % (from market research)"],
            "calculation_frequency": "Quarterly / Semi-Annual"
        }
    ]
}

# Convert to DataFrame for better readability
all_kpis = []
for category, kpi_list in kpis_data.items():
    for kpi in kpi_list:
        kpi['category'] = category
        all_kpis.append(kpi)

kpi_df = pd.DataFrame(all_kpis)
print(f"✅ COMPLETE KPI CATALOG CREATED: {len(all_kpis)} KPIs across 4 categories")
print(f"\nBreakdown:")
print(f"  - Revenue Performance: {len(kpis_data['Revenue Performance KPIs'])}")
print(f"  - Customer Behavior: {len(kpis_data['Customer Behavior KPIs'])}")
print(f"  - Operational Efficiency: {len(kpis_data['Operational Efficiency KPIs'])}")
print(f"  - Competitive Position: {len(kpis_data['Competitive Position KPIs'])}")
print(f"\nTotal KPIs: {len(all_kpis)}")

# Save to CSV
kpi_df.to_csv('hotel_ota_kpi_catalog.csv', index=False)
print("\n✅ KPI Catalog exported to: hotel_ota_kpi_catalog.csv")
