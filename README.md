# 📉 Telco Customer Churn Analysis

> **An end-to-end data analytics project** combining SQL, Python EDA, and Power BI dashboards — built to uncover why telecom customers leave and which segments are most at risk.

---

## 🗂️ Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Folder Structure](#-folder-structure)
- [Database & SQL Layer](#-database--sql-layer)
- [Exploratory Data Analysis](#-exploratory-data-analysis-eda)
- [Data Cleaning](#-data-cleaning)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Business Insights](#-key-business-insights)
- [How to Run](#-how-to-run)

---

## 📌 Project Overview

Customer churn — when a customer stops using a service — is one of the most costly problems in the telecom industry. Acquiring a new customer costs **5–7× more** than retaining an existing one.

This project analyzes the Telco Customer Churn dataset to:

- **Identify** patterns and segments with the highest churn rates
- **Explore** the data through rich visualizations
- **Query** business questions using structured SQL
- **Visualize** KPIs and trends through a Power BI dashboard

---

## 📦 Dataset

| Property | Details |
|---|---|
| **Source** | [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| **Origin** | IBM Sample Dataset |
| **Records** | 7,043 customers |
| **File** | `WA_Fn-UseC_-Telco-Customer-Churn.csv` |
| **Target Column** | `Churn` (Yes / No) |

### 📋 Dataset Columns

The dataset captures four categories of customer information:

**👤 Demographics**
| Column | Description |
|---|---|
| `gender` | Male / Female |
| `SeniorCitizen` | Whether the customer is a senior citizen (0 or 1) |
| `Partner` | Whether they have a partner |
| `Dependents` | Whether they have dependents |

**📱 Services Subscribed**
| Column | Description |
|---|---|
| `PhoneService` | Phone service subscription |
| `MultipleLines` | Multiple phone lines |
| `InternetService` | DSL / Fiber Optic / None |
| `OnlineSecurity` | Online security add-on |
| `OnlineBackup` | Online backup add-on |
| `DeviceProtection` | Device protection plan |
| `TechSupport` | Technical support service |
| `StreamingTV` | TV streaming service |
| `StreamingMovies` | Movie streaming service |

**💳 Account Information**
| Column | Description |
|---|---|
| `tenure` | Number of months with the company |
| `Contract` | Month-to-month / One year / Two year |
| `PaperlessBilling` | Whether billing is paperless |
| `PaymentMethod` | Electronic check / Mailed check / Bank transfer / Credit card |
| `MonthlyCharges` | Monthly billing amount |
| `TotalCharges` | Total amount charged to date |

**🎯 Target**
| Column | Description |
|---|---|
| `Churn` | Whether the customer left (`Yes` / `No`) |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Database** | MySQL | Store, query and analyze customer data |
| **Analysis** | Python (Pandas, Matplotlib, Seaborn) | EDA and data cleaning |
| **Notebooks** | Jupyter Notebook | Interactive data exploration |
| **Dashboard** | Power BI | Visual KPIs and business reporting |

---

## 🏗️ Project Architecture

```
CSV Dataset
    │
    ▼
MySQL Database  ──────────────────────────────────────►  SQL Queries
    │                                                      (Business Insights)
    │
    ▼
Python Notebook (eda.ipynb)    – Visualize churn patterns
    │
    ▼
Power BI Dashboard             – KPIs, charts, slicers for stakeholders
```

---

## 📁 Folder Structure

```
customer-churn/
│
├── data/                          # Raw and processed datasets
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Original dataset
│   └── telco_churn_clean.csv                   # Cleaned dataset
│
├── sql/                           # MySQL scripts (ordered by execution)
│   ├── 1_create_database.sql      # Create the database
│   ├── 2_create_table.sql         # Define the customer_data schema
│   ├── 3_import_data.sql          # Load CSV into the table
│   ├── 4_buisness_queries.sql     # 8 business insight queries
│   ├── 5_adv_queries.sql          # Advanced/window queries
│   ├── 6_views.sql                # Reusable SQL views
│   └── 7_indexes.sql              # Performance indexes
│
├── notebook/                      # Jupyter notebooks
│   └── eda.ipynb                  # Exploratory Data Analysis
│
└── power_bi/
    └── customer_churn.pbix        # Power BI dashboard file
```

---

## 🗃️ Database & SQL Layer

The entire dataset is loaded into a **MySQL** database called `customer_churn`, using a structured table `customer_data`.

### Schema Highlights
- 20 columns mapped exactly to the dataset features
- Proper data types: `VARCHAR`, `TINYINT`, `INT`, `DECIMAL`
- Indexed on key filter columns for fast query performance

### SQL Scripts (Run in Order)

| File | Description |
|---|---|
| `1_create_database.sql` | Creates `customer_churn` database |
| `2_create_table.sql` | Defines the `customer_data` table schema |
| `3_import_data.sql` | Imports CSV data using `LOAD DATA` |
| `4_buisness_queries.sql` | 8 business-driven analytical queries |
| `5_adv_queries.sql` | Advanced queries (window functions, etc.) |
| `6_views.sql` | Creates the `churn_summary` view |
| `7_indexes.sql` | Adds indexes on `Churn`, `Contract`, `PaymentMethod`, `InternetService` |

### 📊 Business Queries (from `4_buisness_queries.sql`)

| # | Business Question |
|---|---|
| Q1 | Churn rate by **Contract type** |
| Q2 | Churn rate by **Internet Service** type |
| Q3 | Churn rate by **Internet Service + Contract** combination |
| Q4 | Churn rate by **Payment Method** |
| Q5 | Churn rate for **Senior Citizens** vs non-seniors |
| Q6 | Churn rate by **Tech Support** subscription |
| Q7 | Average **Monthly Charges** for churned vs retained |
| Q8 | Average **Tenure** for churned vs retained |

### 🔍 Indexes for Performance
```sql
-- Speeds up GROUP BY and WHERE on commonly filtered columns
CREATE INDEX idx_churn    ON customer_data(Churn);
CREATE INDEX idx_contract ON customer_data(Contract);
CREATE INDEX idx_payment  ON customer_data(PaymentMethod);
CREATE INDEX idx_internet ON customer_data(InternetService);
```

### 👁️ SQL View
```sql
-- churn_summary view: pre-aggregated churn rate per contract type
CREATE VIEW churn_summary AS
SELECT Contract, COUNT(*) AS Total_Customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
       ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*), 2) AS Churn_Rate
FROM customer_data
GROUP BY Contract;
```

---

## 🔍 Exploratory Data Analysis (EDA)

**Notebook:** `notebook/eda.ipynb`

The EDA notebook covers:

- **Churn Distribution** — Overall churn rate across the dataset
- **Demographic Analysis** — Churn by gender, senior citizen status, partner/dependent presence
- **Service Analysis** — Churn rates across all subscribed services (internet, streaming, security, etc.)
- **Account Analysis** — Impact of contract type, payment method, and paperless billing on churn
- **Financial Analysis** — Distribution of monthly charges and total charges by churn status
- **Tenure Analysis** — How customer lifetime correlates with churn probability
- **Correlation Heatmap** — Relationships between numerical features

> Tools used: `pandas`, `matplotlib`, `seaborn`

---

## 🧹 Data Cleaning

**Notebook:** `notebook/eda.ipynb`

Key cleaning steps performed during exploration:

- **Missing value handling** — Identified and removed blank strings/null values in `TotalCharges`
- **Customer ID removal** — Dropped `customerID` as it is a non-predictive unique identifier
- **Deduplication** — Checked and removed duplicate customer entries
- **Cleaned export** — Exported the cleaned dataset as `telco_churn_clean.csv` for SQL and Power BI layers

---

## 📊 Power BI Dashboard

**File:** `power_bi/customer_churn.pbix`

The Power BI report provides an interactive business dashboard with:

- **Overall Churn KPI** — Total customers, churned count, and churn %
- **Churn by Contract Type** — Month-to-month vs yearly contracts
- **Churn by Internet Service** — Fiber Optic vs DSL vs None
- **Churn by Payment Method** — Breakdown across 4 payment types
- **Senior Citizen Churn** — Demographic-level insight
- **Monthly Charges vs Churn** — Revenue impact visualization
- **Tenure vs Churn** — How loyalty relates to retention

> Open `customer_churn.pbix` in **Microsoft Power BI Desktop** to explore the interactive report.

---

## 💡 Key Business Insights

Based on the SQL analysis and EDA:

| Insight | Finding |
|---|---|
| 📄 **Contract Type** | Month-to-month customers churn at **~42%** vs ~11% for 1-year and ~3% for 2-year contracts |
| 🌐 **Internet Service** | Fiber Optic users have the **highest churn rate** despite (or because of) higher charges |
| 💳 **Payment Method** | Customers paying via **Electronic Check** churn the most |
| 👴 **Senior Citizens** | Senior customers churn at a **higher rate** than non-seniors |
| 🔧 **Tech Support** | Customers **without Tech Support** churn significantly more |
| 💰 **Monthly Charges** | Churned customers have higher average monthly charges |
| ⏱️ **Tenure** | Customers who churn have a **much shorter average tenure** — early months are critical |

---

## ▶️ How to Run

### Prerequisites
- MySQL (v8+)
- Python 3.9+ with `pandas`, `matplotlib`, `seaborn`
- Power BI Desktop (for `.pbix` file)
- Jupyter Notebook / JupyterLab

### Step 1 — Set up the Database
```sql
-- Run in order inside MySQL Workbench or CLI
source sql/1_create_database.sql
source sql/2_create_table.sql
source sql/3_import_data.sql
```

### Step 2 — Run SQL Analysis
```sql
-- Open and run
source sql/4_buisness_queries.sql
source sql/6_views.sql
source sql/7_indexes.sql
```

### Step 3 — Run Notebooks
```bash
cd notebook
jupyter notebook
# Open eda.ipynb → Run All
```

### Step 4 — Open the Dashboard
```
Open Power BI Desktop
→ File → Open → select power_bi/customer_churn.pbix
```

---

## 👤 Author

**Kartikey**  
Data Analytics Project | 2024  
Dataset: [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) by BlastChar (IBM Sample Data)
