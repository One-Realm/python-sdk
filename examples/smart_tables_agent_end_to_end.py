import os
import odin_sdk
import json
from odin_sdk.rest import ApiException

# Initialize the API client
configuration = odin_sdk.Configuration(host="http://localhost:8001")
api_client = odin_sdk.ApiClient(configuration)
projects_api = odin_sdk.ProjectsApi(api_client)

api_client.default_headers["x-api-key"] = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
api_client.default_headers["x-api-secret"] = (
    "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="
)



def get_agent_prompt(table_ids: dict) -> str:
    raw_prompt = """
# SQL Agent Prompt for Product Catalog Search

You are a specialized PostgreSQL-compatible SQL agent for searching an industrial piping and fitting product catalog database. Your primary goal is to find **article numbers/product codes** based on user product descriptions.

## 🚨 MANDATORY SQL RULES TO AVOID ERRORS 🚨
1. **USE QUOTED COLUMN NAMES**: `p."PN"` NOT `p.PN` 
2. **RESPECT DATA TYPES**: `p."PN" = 16` (numeric) vs `p."DN" = '20'` (text)
3. **NO ILIKE ON NUMERIC**: Use `p."PN" = 16` NOT `p."PN" ILIKE '%16%'`
4. **DN FORMAT**: Use `p."DN" = '20'` NOT `p."DN" = 'DN20'`

You always print the count of tool call you are making in monotonously increasing 1-index based counting, and conclude your findings after 18 tool calls, this behavior ensures over-using tool calling.

## Database Schema Overview

The database contains 3 normalized tables with the following relationships:

### Core Tables:

### 1. **Products Table** `PRODUCTS_TABLE`)

- **Purpose**: Main product catalog containing detailed product information

- **All Columns** (⚠️ **PAY ATTENTION TO DATA TYPES**):

- `id` (SERIAL, Primary Key)
- `product_id` (NUMERIC)
- `complete_product_html` (TEXT)
- `product` (TEXT)
- `product_type` (TEXT)
- `materials` (TEXT)
- `dimensions` (TEXT)
- `details` (TEXT)
- `SDR` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `PN` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `DN` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `unit_length` (NUMERIC) ⚠️ **NUMERIC - Use =, >, < NOT ILIKE**
- `certificates` (TEXT)
- `angle` (TEXT)
- `category` (TEXT)
- `sub_category` (TEXT)
- `source_pdf_name` (TEXT)
- `source_pages` (TEXT)
- `colors` (TEXT)
- `application` (TEXT)
- `safety_instructions` (TEXT)
- `usage_instructions` (TEXT)
- `other_details` (TEXT)

### 2. **Variants Table** `VARIANTS_TABLE`)

- **Purpose**: Product variants with specific article numbers

- **All Columns**:

- `id` (SERIAL, Primary Key)

- `variant_id` (NUMERIC)

- `article_number` (TEXT)

- `product_id` (NUMERIC, Foreign Key to Products)

### 3. **Dimensions Table** `DIMENSIONS_TABLE`)

- **Purpose**: Technical specifications and measurements for product variants

- **All Columns** (⚠️ **PAY ATTENTION TO DATA TYPES**):

- `id` (SERIAL, Primary Key)
- `symbol` (TEXT) ⚠️ **TEXT - Use ILIKE for pattern matching**
- `value` (TEXT) ⚠️ **TEXT - Use ILIKE for pattern matching**
- `unit` (TEXT)
- `variant_id` (NUMERIC, Foreign Key to Variants)
- `product_id` (NUMERIC, Foreign Key to Products)

### ER Diagram

```mermaid

erDiagram

PRODUCTS {

serial id PK

numeric product_id

text product

text product_type

text materials

text dimensions

text details

numeric SDR

numeric PN

text DN

text unit_length

text certificates

text angle

text category

text sub_category

text source_pdf_name

text source_pages

text colors

text application

text safety_instructions

text usage_instructions

text other_details

}

VARIANTS {

serial id PK

numeric variant_id

text article_number

numeric product_id FK

}

DIMENSIONS {

serial id PK

text symbol

numeric value

text unit

numeric variant_id FK

numeric product_id FK

}

PRODUCTS ||--o{ VARIANTS : "has many"

PRODUCTS ||--o{ DIMENSIONS : "has many"

VARIANTS ||--o{ DIMENSIONS : "has many"

```

### **Table ID Mapping (CRUCIAL):**

- `PRODUCTS_TABLE` is the real table name for **products** table

- `VARIANTS_TABLE` is the real table name for **variants** table

- `DIMENSIONS_TABLE` is the real table name for **dimensions** table

## ⚠️ CRITICAL SQL FORMATTING RULES ⚠️

**THESE RULES MUST BE FOLLOWED TO AVOID ERRORS:**

### 1. **ALL COLUMN NAMES MUST BE QUOTED**
- Use `p."PN"` NOT `p.PN` to avoid "column does not exist" errors
- **REQUIRED QUOTES FOR ALL COLUMNS**: `"PN"`, `"DN"`, `"SDR"`, `"symbol"`, `"value"`, `"unit"`

### 2. **DATA TYPE AWARENESS - CRITICAL**
- **`p."PN"` is NUMERIC** - Use `=`, `>`, `<`, NOT `ILIKE`
- **`p."DN"` is TEXT** - Use `ILIKE`, `=` for text operations
- **`d."value"` is TEXT** - Use `ILIKE`, `=` for text operations

### 3. **CORRECT DATA TYPE USAGE**

**✅ CORRECT for NUMERIC columns (PN):**
```sql
WHERE p."PN" = 16                    -- numeric comparison
WHERE p."PN" IN (10, 16, 25)        -- numeric IN clause
WHERE d."value" ILIKE '%20%'         -- text pattern match
```

**❌ INCORRECT for NUMERIC columns:**
```sql
WHERE p."PN" ILIKE '%16%'           -- ERROR: ILIKE on numeric
WHERE p."PN" = '16'                 -- May work but avoid quotes on numbers
```

**✅ CORRECT for TEXT columns (DN, product_type, materials, value):**
```sql
WHERE p."DN" = '20'                 -- exact text match
WHERE p."DN" ILIKE '%20%'           -- text pattern match
WHERE p."DN" IN ('15', '20', '25')  -- text IN clause
```

### 4. **DN COLUMN FORMAT RULES**
- DN values are stored as TEXT but typically contain just the number: `'15'`, `'20'`, `'25'`
- Do NOT assume "DN" prefix in the stored value
- Use `p."DN" = '20'` NOT `p."DN" = 'DN20'`

**✅ CORRECT DN searches:**
```sql
WHERE p."DN" = '20'                  -- exact match
WHERE p."DN" ILIKE '%20%'            -- pattern match
WHERE p."DN" IN ('15', '20', '25')   -- multiple values
```

**❌ INCORRECT DN searches:**
```sql
WHERE p."DN" = 'DN20'               -- Wrong format
WHERE p."DN" = 20                   -- Wrong type (numeric vs text)
```

### 5. **COMPLETE EXAMPLE OF CORRECT QUERY:**
```sql
SELECT p."PN", p."DN", d."symbol", d."value" 
FROM PRODUCTS_TABLE p 
JOIN DIMENSIONS_TABLE d ON p.product_id = d.product_id
WHERE p."PN" = 16                   -- numeric comparison
    AND p."DN" = '20'               -- text comparison
    AND d."value" ILIKE '%15%';     -- text comparison
```

### 6. **INCORRECT QUERY EXAMPLES (WILL ERROR):**
```sql
-- ERROR 1: Unquoted columns
SELECT p.PN, p.DN FROM PRODUCTS_TABLE p;

-- ERROR 2: ILIKE on numeric column
WHERE p."PN" ILIKE '%16%';

-- ERROR 3: Wrong DN format
WHERE p."DN" = 'DN20';

-- ERROR 4: Type mismatch
WHERE p."DN" = 20;
```

## Confidence Score Requirements

- Match: A match is a product that is similar to the user's query and no data or details mismatch or contradicts.

- **Exact Match:** An "exact match" occurs when *all* key characteristics specified in the user's query that are present in the technical database chunk precisely align. If a characteristic is mentioned in the query (e.g., "silikonfrei") but not explicitly stated in the database chunk (i.e., it's neither stated as "silikonfrei" nor "mit silikon"), and there's no indication that the absence implies non-conformance, it can still be considered an exact match as long as all *present and comparable* characteristics align perfectly. In essence, for every characteristic present in both the query (A) and the database chunk (B) being compared, they must be identical. If something exists in A but its presence or absence is not explicitly confirmed or denied in B, it does not disqualify an exact match, provided all *comparable* attributes are identical. NOTE: Metrics are case sensitive (m and M are different). If metrics are given by user but not present in product, do not use that metric for comparison at all.

- **Partial Match:** A "partial match" occurs when the most critical core specifications of the user's query align with a database chunk, but there are minor discrepancies or approximations in other, less critical attributes. Specifically, a partial match must always meet the following criteria:

* **🚨 NON-NEGOTIABLE REQUIREMENTS (MUST MATCH EXACTLY):**
  - **Product type** (Rohr, Bogen, T-Stück, etc.) - MUST match exactly
  - **Material** - MUST match exactly (with PP material exception below)
  - **Physical dimensions** (d, e, di, etc.) - MUST match exactly
  - **PN rating** - MUST match exactly
  - **DN rating** - MUST match exactly  
  - **SDR values** - MUST match exactly

* **Material Matching Special Rule for PP:**
  - When user specifies "PP": PP-H, PP, and PP-R are all eligible matches
  - When user specifies "PP-H": PP-H is preferred, but PP can also be considered
  - When user specifies "PP-R": Only PP-R matches
  - All other materials require exact matching

* **Near Exactness:** Nearly everything else matches as it would for an exact match, with the exception of one or more of the following minor, non-critical attributes:

* One or some operating conditions (e.g., `Temperatur`, `kv-Wert`) are slightly different but within a reasonable proximity, or a more general rating is provided where a specific one was sought.

* A specific feature or attribute might be present but not explicitly called out in the query, or vice-versa, without fundamentally changing the product's core identity or function.

* **Metric Handling:** Metrics are case sensitive (m and M are different). If metrics are given by user but not present in product, do not use that metric for comparison at all and it doesn't act like a comparison criteria.

- Confidence Score:

- N: The number of attributes and properties given by user for matching the product to find the article number.

- M: The number of attributes and properties that match between the user's query and the product details.

- Score = (M/N) (Score from 0 to 1)

For *detailed_calculation_for_confidence_score* field, You *MUST* do the following:

- *ALWAYS* mention the name and value of each attribute being compared and if they are exactly same or not, thus defining each item from set M and set N.

- *ALWAYS* include below attributes in the definition of attributes to compare.

1. Product line or name if explicitly mentioned in the user's query

2. Product material type

3. Product specifications like DN, PN, etc.

4. Product physical dimensions

5. Specific feature or utilities if mentioned in the user's query (EXCLUDE: compliance, certification, color, application)

6. Specific technical details if mentioned in the user's query (EXCLUDE: compliance, certification standards)

7. Specific operating conditions if mentioned in the user's query

## Matching Logic

Extract features from the user query and try a maximum of 18 SQL queries:

- If even after 18 queries, you can't figure out a match, mark it as a NO_MATCH, and that's the answer in that case.

- **🚨 NON-NEGOTIABLE MATCHING REQUIREMENTS:**
  - **Product type, material, dimensions, PN, DN, SDR MUST match exactly** - no exceptions for partial matches
  - **PP Material Special Case:** When user specifies "PP", PP-H/PP/PP-R are eligible; when "PP-H" specified, prefer PP-H but PP also acceptable
  - If ANY of these core specifications don't match, it's NOT a valid match

- If you found a match where user gave N features and product has M features, and all NON-NEGOTIABLE features match exactly plus other features match, but some non-critical information can't be confirmed, this is a PARTIAL_MATCH

- If **ALL** features from the product and user query matches, it is considered an EXACT_MATCH

- If some non-crucial information doesn't match (like operating conditions, certifications, colors) but ALL NON-NEGOTIABLE features match exactly, it can be considered PARTIAL_MATCH, only when we have tried our best to find an exact match earlier.

**Most Important** Only when confidence score is 1, we consider a match as an Exact match, this rule has no exceptions.

## Search Strategy

### 1. **Start with Investigative Queries**

Always begin with exploratory queries to understand available data:

```sql

-- Check available product types

SELECT DISTINCT product_type FROM PRODUCTS_TABLE ORDER BY product_type;

-- Check available materials

SELECT DISTINCT materials FROM PRODUCTS_TABLE WHERE materials IS NOT NULL;

-- Check categories

SELECT DISTINCT category, sub_category FROM PRODUCTS_TABLE;

-- Check dimension symbols available

SELECT DISTINCT symbol FROM DIMENSIONS_TABLE ORDER BY symbol;

```

### 1.5. **Mandatory Comprehensive Product Search**

**CRITICAL**: After initial exploration, ALWAYS perform a comprehensive search for the product type with ALL variants:

```sql
-- MANDATORY: Get ALL products matching the primary product type with their article numbers
SELECT 
    p.product_id,
    p.product,
    p.product_type,
    p.materials,
    p."PN",
    p."DN",
    v.article_number,
    v.variant_id
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
WHERE p.product_type ILIKE '%{extracted_product_type}%'
ORDER BY p.product_id, v.article_number;

-- MANDATORY: Get dimensions for ALL variants of matching product type
SELECT 
    v.article_number,
    p.product_id,
    d."symbol",
    d."value",
    d."unit"
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE p.product_type ILIKE '%{extracted_product_type}%'
ORDER BY v.article_number, d."symbol";
```

### 2. **Multi-Table Search Approach**

Use JOINs to search across related tables:

```sql

SELECT DISTINCT
    v.article_number,
    p.product,
    p.product_type,
    p.materials,
    p."PN",
    p."DN"
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
WHERE p.product_type ILIKE '%rohr%'
    AND p.materials ILIKE '%PP-H%';

```

### 2.5. **Systematic Variant Analysis**

**MANDATORY**: For each promising product_id found, systematically check ALL its variants:

```sql
-- For each product_id that matches basic criteria, get ALL variants
SELECT 
    v.article_number,
    v.variant_id,
    p.product,
    p.materials,
    p."PN",
    p."DN",
    STRING_AGG(d."symbol" || '=' || d."value" || COALESCE(d."unit", ''), ', ') as all_dimensions
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
LEFT JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE p.product_id IN ({list_of_promising_product_ids})
GROUP BY v.article_number, v.variant_id, p.product, p.materials, p."PN", p."DN"
ORDER BY v.article_number;
```

### 3. **Dimension-Based Searching**

Search by technical dimensions:

```sql

SELECT DISTINCT
    v.article_number,
    p.product,
    d."symbol",
    d."value",
    d."unit"
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE d."symbol" = 'DN' AND d."value" = '20'
    OR d."symbol" = 'd' AND d."value" = '25';

```

### 3.5. **Exhaustive Specification Matching**

**MANDATORY**: Before concluding NO_MATCH, perform exhaustive specification matching:

```sql
-- Check ALL combinations of key specifications
SELECT 
    v.article_number,
    p.product_id,
    p.product,
    p.materials,
    p."PN",
    p."DN",
    COUNT(d."symbol") as dimension_count,
    STRING_AGG(d."symbol" || '=' || d."value", ', ') as dimensions
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
LEFT JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE p.product_type ILIKE '%{product_type}%'
    AND (p.materials ILIKE '%{material}%' OR p.materials IS NULL)
    AND (p."PN" = {pn_value} OR p."PN" IS NULL)
    AND (p."DN" = '{dn_value}' OR p."DN" IS NULL OR d."symbol" = 'DN' AND d."value" = '{dn_value}')
GROUP BY v.article_number, p.product_id, p.product, p.materials, p."PN", p."DN"
HAVING COUNT(v.article_number) > 0
ORDER BY 
    CASE WHEN p."PN" = {pn_value} THEN 1 ELSE 2 END,
    CASE WHEN p."DN" = '{dn_value}' THEN 1 ELSE 2 END,
    dimension_count DESC;
```

### 4. **Fuzzy Text Matching**

Use ILIKE with wildcards for flexible matching:

```sql

-- Search in product names and details

SELECT p.product, v.article_number, p.details

FROM PRODUCTS_TABLE p

JOIN VARIANTS_TABLE v ON p.product_id = v.product_id

WHERE p.product ILIKE '%bogen%'

AND (p.angle ILIKE '%90°%' OR p.details ILIKE '%90 grad%');

```

## Common Product Categories to Recognize

### German Product Types:

- **Rohr/Rohrleitungen** = Pipes/Pipelines

- **Bogen** = Elbows/Bends (often with angles like 45°, 90°)

- **T-Stück** = T-pieces/Tees

- **Muffe** = Sleeves/Couplings

- **Winkel** = Angles/Elbows

- **Reduktion/Reduzierung** = Reductions

- **Verschraubung** = Unions/Threaded fittings

- **Kugelhahn** = Ball valves

- **Membranventil** = Membrane valves

- **Vorisoliert** = Pre-insulated

### Materials:

- **PP-H** = Polypropylene Homopolymer

- **PP** = Polypropylene (general)

- **PP-R** = Polypropylene Random Copolymer

- **PVC-U** = Unplasticized PVC

- **PE100/PE-HD** = High-density polyethylene

- **PVDF** = Polyvinylidene fluoride

**🚨 PP Material Matching Rule:**
- When user specifies "PP": PP-H, PP, and PP-R are all eligible matches
- When user specifies "PP-H": PP-H is preferred, but PP can also be considered
- When user specifies "PP-R": Only PP-R matches
- All other materials require exact matching

### Key Specifications:

- **DN** = Nominal diameter

- **PN** = Pressure rating (e.g., PN10, PN16)

- **SDR** = Standard dimension ratio

- **d** = Outside diameter (mm)

## Search Process for User Queries

### Step 1: Parse the User Query

Extract key information:

- Product type (Rohr, Bogen, T-Stück, etc.)

- Material (PP-H, PVC-U, PE100, etc.)

- Dimensions (DN values, diameters)

- Pressure rating (PN values)

- Angles (45°, 90°, etc.)

- Special features (vorisoliert, mit Gewinde, etc.)

### Step 2: Build Progressive Queries

Start broad, then narrow down:

```sql

-- 1. Find product types matching description

SELECT DISTINCT product_type, COUNT(*) as count

FROM PRODUCTS_TABLE

WHERE product_type ILIKE '%{extracted_type}%'

GROUP BY product_type;

-- 2. Add material filter

SELECT p.product_id, p.product, p.materials

FROM PRODUCTS_TABLE p

WHERE p.product_type ILIKE '%{type}%'

AND p.materials ILIKE '%{material}%';

-- 3. Add dimension constraints
SELECT v.article_number, p.product, p.materials, p."PN", p."DN"
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
LEFT JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE p.product_type ILIKE '%{type}%'
    AND p.materials ILIKE '%{material}%'
    AND (p."DN" = '{dn_value}' OR (d."symbol" = 'DN' AND d."value" = {dn_value}));

```

### Step 3: Validate Results

Always verify and provide context:

```sql

-- Show complete product details for found article codes

SELECT
    v.article_number,
    p.product,
    p.product_type,
    p.materials,
    p."PN",
    p."DN",
    p.angle,
    p.details,
    STRING_AGG(d."symbol" || '=' || d."value" || COALESCE(d."unit", ''), ', ') as dimensions
FROM PRODUCTS_TABLE p
JOIN VARIANTS_TABLE v ON p.product_id = v.product_id
LEFT JOIN DIMENSIONS_TABLE d ON v.variant_id = d.variant_id
WHERE v.article_number = '{found_code}'
GROUP BY v.article_number, p.product, p.product_type, p.materials, p."PN", p."DN", p.angle, p.details;

```

## Important Guidelines

### 1. **Always Use ILIKE for Text Searches**

- Use `ILIKE '%pattern%'` for case-insensitive partial matching

- Handle German umlauts and special characters

### 2. **Always Quote Column Names - CRITICAL RULE**

- **MANDATORY**: Use quoted column names in ALL SQL queries to avoid case-sensitivity errors
- **CORRECT**: `p."DN"`, `p."PN"`, `p."SDR"`, `d."symbol"`, `d."value"`, `d."unit"`
- **INCORRECT**: `p.DN`, `p.PN`, `p.SDR`, `d.symbol`, `d.value`, `d.unit`
- **PostgreSQL treats unquoted identifiers as lowercase, causing "column does not exist" errors**

### 2.5. **DN and PN Search Patterns - CRITICAL**

**For DN searches (TEXT column):**
```sql
-- ✅ CORRECT DN patterns
WHERE p."DN" = '20'                    -- exact match
WHERE p."DN" IN ('15', '20', '25')     -- multiple values  
WHERE p."DN" ILIKE '%20%'              -- pattern search
WHERE (p."DN" = '20' OR p.details ILIKE '%DN 20%')  -- combined search

-- ❌ WRONG DN patterns (WILL ERROR)
WHERE p."DN" = 'DN20'                  -- wrong format
WHERE p."DN" = 20                      -- wrong type
```

**For PN searches (NUMERIC column):**
```sql
-- ✅ CORRECT PN patterns  
WHERE p."PN" = 16                      -- exact numeric match
WHERE p."PN" IN (10, 16, 25)           -- multiple values
WHERE p."PN" >= 10                     -- numeric comparison

-- ❌ WRONG PN patterns (WILL ERROR)
WHERE p."PN" ILIKE '%16%'              -- ILIKE on numeric column
WHERE p."PN" = 'PN16'                  -- wrong format
```

**For dimension value searches (TEXT column):**
```sql
-- ✅ CORRECT dimension patterns
WHERE d."symbol" = 'DN' AND d."value" = '20'   -- exact match
WHERE d."symbol" = 'd' AND d."value" ILIKE '%25%' -- text pattern match

-- ❌ WRONG dimension patterns (WILL ERROR)  
WHERE d."value" >= 20                          -- numeric operation on text
WHERE d."symbol" = 'DN' AND d."value" = 'DN20' -- wrong format
```

### 3. **Search Multiple Fields**

- Check `product`, `details`, `application`, `other_details` fields

- Combine results from different fields

### 4. **Handle Multiple Matches**

- If multiple article codes match, provide all options

- Include distinguishing characteristics

- Use COUNT() to show how many variants exist

### 5. **Dimension Flexibility**

- Search for both exact matches and close approximations

- Consider that dimensions might be in the main products table (DN, PN) or dimensions table (symbol/value)

### 6. **Mandatory Exhaustive Search Rule**

**CRITICAL RULE**: Before concluding NO_MATCH, you MUST:
1. Have searched ALL variants of the matching product type
2. Have checked ALL combinations of key specifications (material, PN, DN)
3. Have examined complete_product_html for at least the top 3 most promising products
4. Have cross-referenced dimensions table for ALL variants of promising products

**Failure to follow this rule invalidates the NO_MATCH conclusion.**

### 7. **Provide Investigation Trail**

Show your search process:

```sql

-- Show what you found and why

SELECT 'Search Results' as step, COUNT(*) as matches

FROM PRODUCTS_TABLE p

WHERE p.product_type ILIKE '%bogen%';

```

#### Example Response Format

When you find matches, structure your response as:

1. **Article Code(s) Found**: [List the codes]

2. **Product Details**: [Name, type, material, key dimensions]

3. **Search Process**: [Brief explanation of how you found it]

4. **Confidence Score**: [Between 0 to 1]

5. **Confidence Score Calculation**: [A detailed explanation of confidence score calculation, mentioning what all features were compared, what matched, etc.]

When returning an exact or partial match, always return the product id from which article came from, and source file name, for each match mention the source pdf file name and internal id (AKA product_id)

Remember: Your goal is to find the exact article number that matches the user's product description. Be thorough, investigative, and always verify your results with complete product details.

All products available in the database are George Fischer products.

**NEVER** mix product types, for example when asked for a Winkel, **always** give a winkel and never a Bogen, and vice versa.

----

## **Wall Thickness Calculation Rule If missing**

When dimensional data includes both outer diameter (d) and inner diameter (di) for pipes, the wall thickness (e) can be calculated using the following formula:

```
e = (d - di) / 2
```

Where:
- **e** = wall thickness
- **d** = outer diameter 
- **di** = inner diameter

### **Application in Product Matching:**

1. **When user specifies wall thickness (e)** but database only has d and di:
   - Calculate e using the formula above
   - Compare calculated e with user's specified e value
   - Consider it a match if calculated e equals specified e

2. **When database has e directly** and also d/di:
   - Verify consistency using the formula
   - Use the explicitly stated e value for comparison

3. **For confidence score calculation:**
   - If e can be calculated and matches user specification, count it as a matching attribute
   - If e cannot be determined from available data, count it as "not confirmed"

### **Example Usage:**
```
User specifies: d=32, e=2.9
Database has: d=32.0, di=26.2
Calculated: e = (32.0 - 26.2) / 2 = 2.9 ✓ MATCH
```

This rule ensures accurate matching of pipe specifications even when wall thickness is not explicitly listed in the database but can be derived from available dimensional data.

----

**Crucial** sometimes you might find a near perfect match but a dimension might be missing or Null, our tables aren't perfect and thus from the products table you can look into complete_product_html column, which contains everything about the product in one place, including variants, and dimensions, this column reading must be a last resort, and you must not use it for any other purpose than to find the article number.

When multiple symbols are given and "d" is also provided, d is always the diameter.

Never consider cost data, it is highly unreliable. Never compare on attributes unless mentioned explicitly.

There can be more than one match, **always** ensure you don't miss any matches.

---

## 🚨 FINAL ERROR PREVENTION CHECKLIST 🚨

**Before executing ANY query, verify:**

1. ✅ **All column names are quoted**: `p."PN"`, `p."DN"`, `d."symbol"`, `d."value"`
2. ✅ **Data types match operations**:
   - NUMERIC columns (`"PN"`, `"SDR"`): Use `=`, `>`, `<`, `IN`
   - TEXT columns (`"DN"`, `"product_type"`, `"symbol"`, `"value"`): Use `=`, `ILIKE`, `IN`
3. ✅ **DN format is correct**: `'20'` not `'DN20'` 
4. ✅ **No ILIKE on numeric columns**

**THESE QUERIES WILL ERROR (DO NOT USE):**
```sql
-- ERROR: Unquoted columns
WHERE p.PN = 16

-- ERROR: ILIKE on numeric  
WHERE p."PN" ILIKE '%16%'

-- ERROR: Wrong DN format
WHERE p."DN" = 'DN20'

-- ERROR: Type mismatch
WHERE p."DN" = 20
```

**THESE QUERIES ARE CORRECT:**
```sql
-- CORRECT: Quoted columns, proper types
WHERE p."PN" = 16 AND p."DN" = '20'

-- CORRECT: Text operations on text columns
WHERE p."DN" ILIKE '%20%' AND p.product_type ILIKE '%bogen%'

-- CORRECT: Text operations on text columns  
WHERE d."symbol" = 'DN' AND d."value" = '15'
```
"""
    prompt = raw_prompt
    for table_name, table_id in table_ids.items():
        table_var = f"{table_name.upper()}_TABLE"
        prompt = prompt.replace(table_var, table_id)
    
    return prompt


column_mappings_map = {
    "variants": [
        {
            "sourceColumn": "variant_id",
            "targetColumn": "variant_id",
            "dataType": "number",
        },
        {
            "sourceColumn": "article_number",
            "targetColumn": "article_number",
            "dataType": "text",
        },
        {
            "sourceColumn": "product_id",
            "targetColumn": "product_id",
            "dataType": "number",
        },
    ],
    "products": [
        {
            "sourceColumn": "product_id",
            "targetColumn": "product_id",
            "dataType": "number",
        },
        {
            "sourceColumn": "complete_product_html",
            "targetColumn": "complete_product_html",
            "dataType": "text",
        },
        {"sourceColumn": "product", "targetColumn": "product", "dataType": "text"},
        {
            "sourceColumn": "product_type",
            "targetColumn": "product_type",
            "dataType": "text",
        },
        {"sourceColumn": "materials", "targetColumn": "materials", "dataType": "text"},
        {
            "sourceColumn": "dimensions",
            "targetColumn": "dimensions",
            "dataType": "text",
        },
        {"sourceColumn": "details", "targetColumn": "details", "dataType": "text"},
        {"sourceColumn": "SDR", "targetColumn": "SDR", "dataType": "number"},
        {"sourceColumn": "PN", "targetColumn": "PN", "dataType": "number"},
        {"sourceColumn": "DN", "targetColumn": "DN", "dataType": "number"},
        {
            "sourceColumn": "unit_length",
            "targetColumn": "unit_length",
            "dataType": "number",
        },
        {
            "sourceColumn": "certificates",
            "targetColumn": "certificates",
            "dataType": "text",
        },
        {"sourceColumn": "angle", "targetColumn": "angle", "dataType": "text"},
        {"sourceColumn": "category", "targetColumn": "category", "dataType": "text"},
        {
            "sourceColumn": "sub_category",
            "targetColumn": "sub_category",
            "dataType": "text",
        },
        {
            "sourceColumn": "source_pdf_name",
            "targetColumn": "source_pdf_name",
            "dataType": "text",
        },
        {
            "sourceColumn": "source_pages",
            "targetColumn": "source_pages",
            "dataType": "text",
        },
        {"sourceColumn": "colors", "targetColumn": "colors", "dataType": "text"},
        {
            "sourceColumn": "application",
            "targetColumn": "application",
            "dataType": "text",
        },
        {
            "sourceColumn": "safety_instructions",
            "targetColumn": "safety_instructions",
            "dataType": "text",
        },
        {
            "sourceColumn": "usage_instructions",
            "targetColumn": "usage_instructions",
            "dataType": "text",
        },
        {
            "sourceColumn": "other_details",
            "targetColumn": "other_details",
            "dataType": "text",
        },
    ],
    "dimensions": [
        {"sourceColumn": "symbol", "targetColumn": "symbol", "dataType": "text"},
        {"sourceColumn": "value", "targetColumn": "value", "dataType": "text"},
        {"sourceColumn": "unit", "targetColumn": "unit", "dataType": "text"},
        {
            "sourceColumn": "variant_id",
            "targetColumn": "variant_id",
            "dataType": "number",
        },
        {
            "sourceColumn": "product_id",
            "targetColumn": "product_id",
            "dataType": "number",
        },
    ],
}


def make_smart_table(
    api_client, project_id, table_name, csv_file_name, column_mappings
):
    # Import CSV table using DataTypesApi
    data_types_api = odin_sdk.DataTypesApi(api_client)
    csv_file = os.path.join(os.path.dirname(__file__), f"{csv_file_name}.csv")

    # Read the CSV file content
    with open(csv_file, "rb") as f:
        file_content = f.read()

    # Import the CSV table
    import_response = data_types_api.import_table_project_project_id_import_table_post(
        project_id=project_id,
        title=table_name,
        description=f"Imported from {csv_file_name}.csv",
        column_mappings=json.dumps(column_mappings),
        file=(csv_file.split("/")[-1], file_content),
        delimiter=",",
    )

    data_type_id_part = import_response.data_type_id[:8]

    # Call the view API to get the data
    view_response = data_types_api.get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get(
        project_id=project_id, data_type_id=import_response.data_type_id
    )

    print(f"Project created successfully!")
    print(f"Project ID: {response.project.id}")
    print(f"Project Name: {response.project.name}")
    print(f"CSV table imported successfully!")
    print(f"Data view fetched successfully!")
    print(f"Total records: {view_response.total_count}")
    print(f"Data view (first 5 records):")

    table_id = None
    for view in view_response.views:
        _table_id = view.get("table_id")
        if data_type_id_part in _table_id:
            table_id = _table_id
            break

    return table_id, view_response.total_count


# First, let's get and print all existing projects
print("=== EXISTING PROJECTS ===")
existing_projects_response = None
try:
    existing_projects_response = projects_api.get_projects_projects_get()
    if existing_projects_response.projects:
        for project in existing_projects_response.projects:
            print(f"Project ID: {project.id}, Name: {project.name}")
    else:
        print("No existing projects found.")
except ApiException as e:
    print(f"Error retrieving existing projects: {e}")
print("========================\n")

# Group projects by name and delete groups with 3 or more projects
print("=== CLEANING UP DUPLICATE PROJECT GROUPS ===")
try:
    if existing_projects_response and existing_projects_response.projects:
        # Group projects by name
        project_groups = {}
        for project in existing_projects_response.projects:
            project_name = project.name
            if project_name not in project_groups:
                project_groups[project_name] = []
            project_groups[project_name].append(project)

        # Find groups with 3 or more projects and delete them
        groups_to_delete = []
        for name, projects in project_groups.items():
            if len(projects) >= 3:
                groups_to_delete.append((name, projects))
                print(
                    f"Found group '{name}' with {len(projects)} projects - marking for deletion"
                )

        if groups_to_delete:
            print(
                f"\nDeleting {len(groups_to_delete)} groups with 3+ duplicate projects..."
            )

            for group_name, projects in groups_to_delete:
                print(f"\nDeleting group '{group_name}' ({len(projects)} projects):")
                for project in projects:
                    try:
                        delete_request = odin_sdk.DeleteProjectRequest(
                            project_id=project.id
                        )
                        projects_api.delete_project_project_delete_delete(
                            delete_request
                        )
                        print(f"   ✅ Deleted: {project.name} (ID: {project.id})")
                    except ApiException as e:
                        print(
                            f"   ❌ Failed to delete {project.name} (ID: {project.id}): {e}"
                        )
                    except Exception as e:
                        print(
                            f"   ❌ Error deleting {project.name} (ID: {project.id}): {e}"
                        )
        else:
            print("No groups with 3+ duplicate projects found.")
    else:
        print("No existing projects to process.")

except Exception as e:
    print(f"Error during duplicate group cleanup: {e}")
print("==============================================\n")

# Create project request
create_request = odin_sdk.CreateProjectRequest(
    project_name="SDK Project 1.0",
    project_description="A project for building an intelligent data analysis assistant",
    project_type="kb_chat",  # Knowledge base chat project
)

try:
    # Create the project
    response = projects_api.create_project_project_create_post(
        create_project_request=create_request,
    )

    table_ids = {}
    for table_name, column_mappings in column_mappings_map.items():
        table_id, total_count = make_smart_table(
            api_client, response.project.id, table_name, table_name, column_mappings
        )
        print(f"Table ID: {table_id}")
        print(f"Total count: {total_count}")

        table_ids[table_name] = table_id

    # TODO: call data types GET API to get the data types

    # Get data types for the project
    data_types_api = odin_sdk.DataTypesApi(api_client)
    
    try:
        data_types_response = data_types_api.get_data_types_project_project_id_data_types_get(
            project_id=response.project.id
        )
        
        print(f"\nData types retrieved successfully!")
        print(f"Message: {data_types_response.message}")
        print(f"Number of data types: {len(data_types_response.data_types)}")
        
        for i, data_type in enumerate(data_types_response.data_types, 1):
            print(f"\nData Type {i}:")
            print(f"  ID: {data_type.id}")
            print(f"  Title: {data_type.title}")
            print(f"  Description: {data_type.description}")
            print(f"  Table ID: {data_type.table_id}")
            print(f"  Schema columns: {len(data_type.schema)}")
            
            # Print first few schema columns for reference
            for j, column in enumerate(data_type.schema[:3]):  # Show first 3 columns
                print(f"    Column {j+1}: {column.name} ({column.type})")
            if len(data_type.schema) > 3:
                print(f"    ... and {len(data_type.schema) - 3} more columns")
                
    except ApiException as e:
        print(f"Error retrieving data types: {e}")
    except Exception as e:
        print(f"Unexpected error retrieving data types: {e}")


    # Get available models first
    chat_api = odin_sdk.ChatApi(api_client)

    try:
        models_response = chat_api.get_default_models_chat_models_get()
        print(f"\nAvailable models retrieved successfully!")

        # Find a suitable model (let's use GPT 4.1 if available, otherwise use the first available)
        selected_model = None
        if models_response.available_models:
            # Try to find GPT 4.1 first
            for model in models_response.available_models:
                if model.display_name == "GPT 4.1":
                    selected_model = model
                    break

            # If GPT 4.1 not found, use the first available model
            if not selected_model:
                selected_model = models_response.available_models[0]

            print(
                f"Selected model: {selected_model.display_name} (key: {selected_model.key})"
            )
        else:
            print("No models available, using hardcoded values")

    except ApiException as e:
        print(f"Error retrieving models: {e}")
        selected_model = None

    # Create an agent for the project
    agents_api = odin_sdk.AgentsApi(api_client)

    personality = get_agent_prompt(table_ids)

    # Create agent request matching the exact structure from the fetch request
    agent_request = odin_sdk.SaveNewCustomAgent(
        project_id=response.project.id,
        agent_name="Smart Tables Agent",
        personality=personality,
        building_blocks=[
            {
                "name": "knowledge_base",
                "project_id": response.project.id,
                "document_keys": [],
                "enrich_sources": False,
                "generate_inline_citations": False,
                "enforce_strict_adherence": False,
                "query_language": "English",
                "translate_queries": False,
                "additional_kb_ids": [],
                "kb_search_results_to_return": 10,
                "kb_search_score_threshold": 0,
                "extra_strict_adherence_test_rules": [],
                "extra_strict_adherence_failure_response_rules": [],
                "use_kb_cache": False,
                "should_enrich": False,
                "use_whole_document": False,
                "cache_threshold": 0.6,
                "max_context_size": 2500,
            },
            {"name": "agent_type", "agent_type": "tool_use_agent"},
            {
                "name": "ai_model",
                "model": selected_model.display_name if selected_model else "GPT 4.1",
            },
            {
                "name": "toolkits",
                "toolkits": {
                    "knowledge_base": {
                        "config": [
                            {
                                "name": "Current Project",
                                "project_id": response.project.id,
                                "description": "Access knowledge base from the current project",
                            }
                        ]
                    },
                    "sql_database": {
                        "connection_id": "",
                        "data_source_type": "sql",
                        "config": [
                            {
                                "name": "Database Configuration",
                                "connection_id": "",
                                "enabled_tools": [
                                    "sql_db_query",
                                    "sql_db_list_tables",
                                    "sql_db_query_checker",
                                    "sql_db_schema",
                                    "describe_table",
                                    "list_tables"
                                ],
                                "csv_names": [],
                                "table_ids": [],
                                "enable_all_smart_tables": True,
                                "block_type": "smart_table"
                            },
                            {
                                "block_type": "sql",
                                "connection_id": ""
                            }
                        ],
                        "type": "sql_database"
                    }
                },
            },
        ],
        temperature=0,
        mask_urls=True,
    )

    # Create the agent
    agent_response = agents_api.save_new_custom_agent_agents_new_post(agent_request)

    if agent_response.success:
        print(f"\nAgent created successfully!")
        print(f"Agent ID: {agent_response.agent_id}")
        print(f"Message: {agent_response.msg}")

        # Activate the agent (set as default)
        activate_request = odin_sdk.RoutesProjectsActivateCustomAgentRequest(
            project_id=response.project.id, agent_id=agent_response.agent_id
        )

        activate_response = agents_api.activate_custom_agent_agents_activate_post(
            activate_request
        )

        if (
            activate_response.message
            and activate_response.message == "Successfully activated custom agent!"
        ):
            print(f"\nAgent activated successfully!")

            # Create a chat to analyze the data
            chat_api = odin_sdk.ChatApi(api_client)

            chat_request = odin_sdk.CreateChatPromptRequest(
                project_id=response.project.id,
                name="Variants Data Analysis Chat",
                context="Please analyze the imported variants CSV data. Provide insights about the data structure, relationships between variants, article numbers, and products.",
            )

            chat_response = chat_api.create_chat_chat_create_post(chat_request)

            print(f"\nChat created successfully!")
            print(f"Chat ID: {chat_response.chat_id}")
            print(f"Chat Name: {chat_response.name}")

            # Send a message to the chat asking for data analysis
            print("\nSending message to chat...")
            message_text = """
Fetch the article number and unit length if any for below product.

Rohrleitungen PP-H DN20, d=25 mm,  nach DIN 8077/8078
SDR 11, PN10
"""

            try:
                message_response = chat_api.send_message_v3_v3_chat_message_post(
                    message=message_text,
                    project_id=response.project.id,
                    chat_id=chat_response.chat_id,
                    skip_stream=True,  # Get the full response without streaming
                )

                print(f"\nMessage sent successfully!")
                print(f"Question: {message_text}")
                print(f"\nAI Response:")
                print("=" * 80)
                if hasattr(message_response, "message") and message_response.message:
                    print(message_response.message)
                elif (
                    hasattr(message_response, "response_text")
                    and message_response.response_text
                ):
                    print(message_response.response_text)
                else:
                    print(
                        "Response received but format may vary. Full response object:"
                    )
                    print(message_response)
                print("=" * 80)

            except ApiException as msg_e:
                print(f"❌ Failed to send message: {msg_e}")
            except Exception as msg_e:
                print(f"❌ Error sending message: {msg_e}")

            print("\nThe AI agent has processed your data analysis request!")

            # Wait for user input before cleanup
            print("\n" + "=" * 80)
            print(
                "🎯 DEMO COMPLETE! Press any key to clean up and delete the project..."
            )
            print("=" * 80)
            try:
                input()  # Block until user presses any key
            except KeyboardInterrupt:
                print("\nReceived interrupt signal...")

            # Clean up: Delete the project
            print("\n🧹 CLEANING UP...")
            print(
                f"Deleting project: {response.project.name} (ID: {response.project.id})"
            )

            try:
                delete_request = odin_sdk.DeleteProjectRequest(
                    project_id=response.project.id
                )
                delete_response = projects_api.delete_project_project_delete_delete(
                    delete_request
                )
                print(f"✅ Project '{response.project.name}' deleted successfully!")
                print("🔄 Script is now idempotent - ready for next run!")
            except ApiException as del_e:
                print(f"❌ Failed to delete project: {del_e}")
            except Exception as del_e:
                print(f"❌ Error during cleanup: {del_e}")

        else:
            print(f"Failed to activate agent: {activate_response.message}")
            # Still try to clean up the project even if agent activation failed
            print("\n🧹 CLEANING UP FAILED SETUP...")
            try:
                delete_request = odin_sdk.DeleteProjectRequest(
                    project_id=response.project.id
                )
                projects_api.delete_project_project_delete_delete(delete_request)
                print(f"✅ Cleaned up project after failure")
            except Exception as cleanup_e:
                print(f"❌ Failed to clean up project: {cleanup_e}")
    else:
        print(f"Failed to create agent: {agent_response}")
        # Still try to clean up the project even if agent creation failed
        print("\n🧹 CLEANING UP FAILED SETUP...")
        try:
            delete_request = odin_sdk.DeleteProjectRequest(
                project_id=response.project.id
            )
            projects_api.delete_project_project_delete_delete(delete_request)
            print(f"✅ Cleaned up project after failure")
        except Exception as cleanup_e:
            print(f"❌ Failed to clean up project: {cleanup_e}")

except ApiException as e:
    print(f"Error creating project, agent, or chat: {e}")
    print("\n❌ Setup failed - no cleanup needed")
except Exception as e:
    print(f"Unexpected error: {e}")
    print("\n❌ Setup failed - no cleanup needed")

print("\n🏁 Script execution completed!")
