# Customer Churn Prediction – Backend

A minimal backend for the Customer Churn Prediction project.  
The Express server acts as a bridge between the Next.js frontend and the Flask ML service.

---

## Architecture

```
Next.js (frontend)
      ↓  POST /predict
Express (backend – port 3001)
      ↓  POST http://localhost:5000/predict
Flask  (ml service – port 5000)
      ↓  loads best_model.pkl + scaler.pkl
      ↑  returns prediction + probability
```

---

## Quick Start

### 1. Install Node packages

Open a terminal inside the `backend/` folder:

```bash
cd backend
npm install
```

### 2. Install Python packages

Open a terminal inside the `ml/` folder:

```bash
cd ml
pip install -r requirements.txt
```

### 3. Start the Flask ML service

```bash
cd ml
python app.py
```

Flask will start at `http://localhost:5000`

### 4. Start the Express backend

```bash
cd backend
npm start
```

Express will start at `http://localhost:3001`

---

## API Reference

### GET /

Health check – confirms the Express server is running.

**Response**
```json
{ "message": "Customer Churn Backend Running" }
```

---

### POST /predict

Send customer features and receive a churn prediction.

**Request Body**
```json
{
  "tenure": 12,
  "MonthlyCharges": 65.5,
  "TotalCharges": 786.0,
  "AvgMonthlySpend": 65.5,
  "ServiceCount": 3
}
```

**Response – Likely to Churn**
```json
{
  "prediction": "Likely to Churn",
  "probability": 0.84
}
```

**Response – Not Likely to Churn**
```json
{
  "prediction": "Not Likely to Churn",
  "probability": 0.16
}
```

---

## Notes

- The model is a **Logistic Regression** trained on 5 features.
- Feature order matters — the Flask service handles this automatically.
- No database, no authentication, no environment variables needed.
