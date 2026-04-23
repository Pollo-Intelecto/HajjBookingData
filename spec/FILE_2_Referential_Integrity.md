# FILE 2: REFERENTIAL INTEGRITY SPECIFICATIONS (COMPLETE)

## 1. FOREIGN KEY RELATIONSHIPS (13 Total)

### Fact_Bookings Relationships

#### 1.1 Fact_Bookings → Dim_Hotel
```
From_Table: Fact_Bookings
To_Table: Dim_Hotel
FK_Column: Hotel_ID
PK_Column: Hotel_ID
Cardinality: Many-to-One (many bookings per hotel)
Nullability: NOT NULL (every booking must reference a hotel)
Cascade_On_Delete: RESTRICT (do not allow deletion of hotels with active bookings)
Cascade_On_Update: CASCADE (if hotel ID changes, update all booking references)
Unique_Constraint: No (multiple bookings per hotel allowed)
Business_Logic_Notes: Hotel must exist and be active (Active_Flag = True) when booking created
Validation_Query: SELECT f.Booking_ID FROM Fact_Bookings f LEFT JOIN Dim_Hotel h ON f.Hotel_ID = h.Hotel_ID WHERE h.Hotel_ID IS NULL
```

#### 1.2 Fact_Bookings → Dim_Customer
```
From_Table: Fact_Bookings
To_Table: Dim_Customer
FK_Column: Customer_ID
PK_Column: Customer_ID
Cardinality: Many-to-One (customer makes multiple bookings)
Nullability: NOT NULL (every booking must have a customer)
Cascade_On_Delete: RESTRICT (do not delete customers with booking history)
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Customer must be registered before booking; Email must be valid format
Validation_Query: SELECT f.Booking_ID FROM Fact_Bookings f LEFT JOIN Dim_Customer c ON f.Customer_ID = c.Customer_ID WHERE c.Customer_ID IS NULL
```

#### 1.3 Fact_Bookings → Dim_RoomType
```
From_Table: Fact_Bookings
To_Table: Dim_RoomType
FK_Column: Room_Type_ID
PK_Column: Room_Type_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Room type must support guest count (Number_Of_Guests <= Room_Capacity)
Validation_Query: SELECT f.Booking_ID, f.Number_Of_Guests FROM Fact_Bookings f JOIN Dim_RoomType r ON f.Room_Type_ID = r.Room_Type_ID WHERE f.Number_Of_Guests > r.Room_Capacity
```

#### 1.4 Fact_Bookings → Dim_Date (Booking_Date_ID)
```
From_Table: Fact_Bookings
To_Table: Dim_Date
FK_Column: Booking_Date_ID
PK_Column: Date_ID
Cardinality: Many-to-One (many bookings per day)
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Role-playing dimension; Booking_Date_ID must be <= CheckIn_Date_ID
Validation_Query: SELECT COUNT(*) FROM Fact_Bookings WHERE Booking_Date_ID > CheckIn_Date_ID
```

#### 1.5 Fact_Bookings → Dim_Date (CheckIn_Date_ID)
```
From_Table: Fact_Bookings
To_Table: Dim_Date
FK_Column: CheckIn_Date_ID
PK_Column: Date_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Role-playing dimension; must be > Booking_Date_ID and < CheckOut_Date_ID
Validation_Query: SELECT COUNT(*) FROM Fact_Bookings WHERE CheckIn_Date_ID <= Booking_Date_ID OR CheckIn_Date_ID >= CheckOut_Date_ID
```

#### 1.6 Fact_Bookings → Dim_Date (CheckOut_Date_ID)
```
From_Table: Fact_Bookings
To_Table: Dim_Date
FK_Column: CheckOut_Date_ID
PK_Column: Date_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Must always be > CheckIn_Date_ID; Length_Of_Stay = CheckOut - CheckIn
Validation_Query: SELECT COUNT(*) FROM Fact_Bookings WHERE CheckOut_Date_ID <= CheckIn_Date_ID
```

#### 1.7 Fact_Bookings → Dim_Channel
```
From_Table: Fact_Bookings
To_Table: Dim_Channel
FK_Column: Channel_ID
PK_Column: Channel_ID
Cardinality: Many-to-One (many bookings via same channel)
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Channel indicates how customer booked (website, mobile app, travel agent, etc.)
Validation_Query: SELECT COUNT(*) FROM Fact_Bookings f WHERE NOT EXISTS (SELECT 1 FROM Dim_Channel c WHERE f.Channel_ID = c.Channel_ID)
```

#### 1.8 Fact_Bookings → Dim_LoyaltyTier (Optional)
```
From_Table: Fact_Bookings
To_Table: Dim_LoyaltyTier
FK_Column: Loyalty_Tier_ID
PK_Column: Loyalty_Tier_ID
Cardinality: Many-to-One
Nullability: NULL (optional; NULL means non-member)
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Loyalty_Tier_ID = 0 means no loyalty program; 1-4 = membership tiers
Validation_Query: SELECT COUNT(*) FROM Fact_Bookings WHERE Loyalty_Tier_ID NOT IN (SELECT Loyalty_Tier_ID FROM Dim_LoyaltyTier) AND Loyalty_Tier_ID IS NOT NULL
```

### Fact_Searches Relationships

#### 1.9 Fact_Searches → Dim_Customer (Optional)
```
From_Table: Fact_Searches
To_Table: Dim_Customer
FK_Column: Customer_ID
PK_Column: Customer_ID
Cardinality: Many-to-One
Nullability: NULL (searches can be anonymous)
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: NULL indicates anonymous search; tracked via browser cookies/IP
```

#### 1.10 Fact_Searches → Dim_Date (Search_Date_ID)
```
From_Table: Fact_Searches
To_Table: Dim_Date
FK_Column: Search_Date_ID
PK_Column: Date_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: When the search was performed
```

#### 1.11 Fact_Searches → Dim_Location (City_ID)
```
From_Table: Fact_Searches
To_Table: Dim_Location
FK_Column: City_ID
PK_Column: Location_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Which city customer searched for
```

### Fact_Competitor_Prices Relationships

#### 1.12 Fact_Competitor_Prices → Dim_Competitor
```
From_Table: Fact_Competitor_Prices
To_Table: Dim_Competitor
FK_Column: Competitor_ID
PK_Column: Competitor_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: Which competitor platform (Booking.com, Agoda, Almosafer, etc.)
```

#### 1.13 Fact_Competitor_Prices → Dim_Date (Snapshot_Date_ID)
```
From_Table: Fact_Competitor_Prices
To_Table: Dim_Date
FK_Column: Snapshot_Date_ID
PK_Column: Date_ID
Cardinality: Many-to-One
Nullability: NOT NULL
Cascade_On_Delete: RESTRICT
Cascade_On_Update: CASCADE
Unique_Constraint: No
Business_Logic_Notes: When price was captured
```

---

## 2. UNIQUE CONSTRAINTS (Per Table)

### Fact_Bookings
- **PRIMARY KEY**: Booking_ID (must be unique, never NULL)
- **UNIQUE CONSTRAINT**: (Booking_ID) - Enforces one row per booking
- **CHECK**: Booking_Date_ID <= CheckIn_Date_ID
- **CHECK**: CheckIn_Date_ID < CheckOut_Date_ID
- **CHECK**: Booking_Amount > 0
- **CHECK**: Commission_Rate_Pct BETWEEN 15 AND 25
- **CHECK**: Length_Of_Stay > 0 AND Length_Of_Stay <= 30
- **CHECK**: Number_Of_Guests > 0 AND Number_Of_Guests <= 4

### Dim_Hotel
- **PRIMARY KEY**: Hotel_ID
- **UNIQUE CONSTRAINT**: Hotel_Name, City (no duplicate hotel name per city)
- **CHECK**: Total_Rooms > 0
- **CHECK**: Star_Rating BETWEEN 1 AND 5
- **CHECK**: Commission_Rate_Pct BETWEEN 15 AND 25

### Dim_Customer
- **PRIMARY KEY**: Customer_ID
- **UNIQUE CONSTRAINT**: Email_Address (emails must be unique)
- **CHECK**: Email matches format (contains @)

### Dim_Date
- **PRIMARY KEY**: Date_ID
- **UNIQUE CONSTRAINT**: Calendar_Date (one row per date)

### Other Dimensions
- **PRIMARY KEY**: [Table]_ID for each dimension
- **UNIQUE CONSTRAINT**: If applicable (e.g., Competitor_Name must be unique)

---

## 3. NOT NULL CONSTRAINTS (Critical Fields)

| Table | Column | Reason |
|-------|--------|--------|
| Fact_Bookings | Booking_ID | Primary key |
| Fact_Bookings | Hotel_ID | Every booking must reference a hotel |
| Fact_Bookings | Customer_ID | Every booking must have a customer |
| Fact_Bookings | Booking_Date_ID | Must record when booking was made |
| Fact_Bookings | CheckIn_Date_ID | Must know check-in date |
| Fact_Bookings | CheckOut_Date_ID | Must know checkout date |
| Fact_Bookings | Booking_Amount | Revenue critical field |
| Fact_Bookings | Commission_Rate_Pct | Needed to calculate commission |
| Fact_Bookings | Reservation_Status | Must track status (Confirmed/Cancelled/etc.) |
| Fact_Bookings | Payment_Status | Critical for revenue recognition |
| Dim_Hotel | Hotel_ID | Primary key |
| Dim_Hotel | Hotel_Name | Must identify hotel |
| Dim_Hotel | City_ID | Must know location |
| Dim_Hotel | Star_Rating | Important for pricing and search |
| Dim_Customer | Customer_ID | Primary key |
| Dim_Customer | Email_Address | Required for contact |
| Dim_Date | Date_ID | Primary key |
| Dim_Date | Calendar_Date | Foundation of date dimension |

---

## 4. REFERENTIAL INTEGRITY VALIDATION APPROACH

### Pre-Generation Validation
1. Load all dimension tables
2. Verify no duplicate primary keys
3. Check all unique constraints

### Post-Generation Validation
1. **FK Existence Check**: For each fact table, verify all FK values exist in parent PK
2. **Orphan Detection**: Find records with FK values that don't exist in parent table
3. **Cardinality Check**: Verify Many-to-One relationships (one PK maps to many FKs)
4. **Cascade Logic**: If parent key changes, verify child records updated correctly
5. **Constraint Violations**: Identify any CHECK constraint violations
6. **Date Logic**: Verify Booking_Date <= CheckIn_Date < CheckOut_Date for all bookings

### Remediation Process
- If FKs violate constraints: Delete orphan records or reassign to valid parent
- If dates invalid: Regenerate dates to satisfy constraints
- If amount ranges invalid: Recalculate based on room rates and length of stay

---

## 5. IMPLEMENTATION PRIORITY

**CRITICAL (Enforce 100%)**:
- All Primary Keys must be unique
- All NOT NULL fields must be populated
- All FK references must exist

**HIGH (Enforce 95%+)**:
- Date logic constraints (Booking <= CheckIn < CheckOut)
- Amount ranges ($30-5000 SAR)
- Commission rates (15-25%)

**MEDIUM (Enforce 90%+)**:
- Email format validation
- Hotel name uniqueness per city
- Star rating ranges (1-5)