# 📉 Telco Customer Churn Analysis

> **An end-to-end data analytics project** combining SQL, Python (EDA & preprocessing), Power BI dashboards, and a REST API backend — built to uncover why telecom customers leave and which segments are most at risk.

---

## 🗂️ Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Folder Structure](#-folder-structure)
- [Database & SQL Layer](#-database--sql-layer)
- [Exploratory Data Analysis](#-exploratory-data-analysis-eda)
- [Data Preprocessing](#-data-preprocessing)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Backend API](#-backend-api)
- [Machine Learning (Brief Note)](#-machine-learning-brief-note)
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
- **Serve** insights through a lightweight REST API

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
| **Analysis** | Python (Pandas, Matplotlib, Seaborn) | EDA and data preprocessing |
| **Notebooks** | Jupyter Notebook | Interactive data exploration |
| **Dashboard** | Power BI | Visual KPIs and business reporting |
| **Backend API** | Node.js + Express | REST API bridging frontend and ML service |
| **ML Service** | Python + Flask | Prediction endpoint (see ML note below) |

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
Python Notebooks
  ├── EDA (eda.ipynb)          – Visualize churn patterns
  └── Preprocessing            – Clean data, encode features
    │
    ▼
Power BI Dashboard             – KPIs, charts, slicers for stakeholders
    │
    ▼
Flask ML Service (port 5000)   – Prediction endpoint
    │
    ▼
Express Backend (port 3001)    – API gateway / proxy
```

---

## 📁 Folder Structure

```
customer-churn/
│
├── data/                          # Raw and processed datasets
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Original dataset
│   ├── telco_churn_clean.csv                   # Cleaned dataset
│   ├── X_train.csv / X_test.csv               # Feature splits
│   ├── y_train.csv / y_test.csv               # Label splits
│   └── churn_feature_summary.csv              # Feature importance summary
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
│   ├── eda.ipynb                  # Exploratory Data Analysis
│   └── preprocessing.ipynb        # Data cleaning & transformation
│
├── power_bi/
│   └── customer_churn.pbix        # Power BI dashboard file
│
├── backend/                       # Node.js + Express REST API
│   ├── server.js                  # API server (port 3001)
│   └── package.json
│
├── ml/                            # ML prediction service (Flask)
│   └── app.py                     # Flask app (port 5000)
│
└── models/                        # Saved ML artifacts
    ├── best_model.pkl             # Trained model (serialized)
    └── scaler.pkl                 # Feature scaler (serialized)
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

## 🧹 Data Preprocessing

**Notebook:** `notebook/preprocessing.ipynb`

Key preprocessing steps performed:

- **Missing value handling** — `TotalCharges` had blank strings converted to `NaN` and imputed
- **Data type conversion** — Converted `TotalCharges` from string to float
- **Label encoding** — Binary columns (`Yes`/`No`) encoded to `1`/`0`
- **One-hot encoding** — Multi-class categoricals (e.g., `InternetService`, `Contract`) encoded
- **Feature scaling** — Applied `StandardScaler` on numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`)
- **Train/Test split** — Data split into training (75%) and test (25%) sets
- **Output files** — `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`, `telco_churn_clean.csv`

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

## 🌐 Backend API

**Folder:** `backend/`  
**Runtime:** Node.js + Express (port `3001`)

The Express server acts as an **API gateway** — it sits between the frontend and the Flask ML prediction service.

### Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — confirms the backend is running |
| `POST` | `/predict` | Forwards customer data to Flask and returns the churn prediction |

### How it Works

```
Frontend (Next.js)
      │  POST /predict  { customer_data }
      ▼
Express Server (port 3001)
      │  Proxies request to Flask
      ▼
Flask ML Service (port 5000)
      │  Returns { prediction, probability }
      ▼
Express returns response to Frontend
```

### Running the Backend
```bash
cd backend
npm install
npm start
# Server starts at http://localhost:3001
```

---

## 🤖 Machine Learning (Brief Note)

> ⚠️ **Note:** The ML component is included in this project to complete the end-to-end pipeline (data → insights → prediction API). The focus of this project is on the **data analytics, SQL analysis, and Power BI** layers.

The ML part (`ml/app.py`) is a **Flask REST API** that:
- Loads a pre-trained model (`models/best_model.pkl`) and scaler (`models/scaler.pkl`)
- Accepts customer feature data as JSON
- Returns a churn prediction (`Yes`/`No`) and a probability score

The model was trained using the cleaned and encoded dataset from the preprocessing notebook. The serialized files (`.pkl`) are stored in the `models/` folder.

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
- Python 3.9+ with `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `flask`
- Node.js 18+
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
# Open preprocessing.ipynb → Run All
```

### Step 4 — Start the Backend API
```bash
cd backend
npm install
npm start
# Express running at http://localhost:3001
```

### Step 5 — Open the Dashboard
```
Open Power BI Desktop
→ File → Open → select power_bi/customer_churn.pbix
```

---

## 👤 Author

**Kartikey**  
Data Analytics Project | 2024  
Dataset: [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) by BlastChar (IBM Sample Data)
