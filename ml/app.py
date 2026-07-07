# ────────────────────────────────────────────
#  Flask ML Service – Customer Churn Prediction
#  Loads the trained model once and serves
#  predictions via a single POST endpoint.
# ────────────────────────────────────────────

from flask import Flask, request, jsonify
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── App setup ──────────────────────────────
app = Flask(__name__)

# ── Load model & scaler once at startup ────
model  = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ── Columns that the scaler was trained on ─
# These 5 numeric columns get scaled first.
NUMERIC_COLS = ["tenure", "MonthlyCharges", "TotalCharges", "AvgMonthlySpend", "ServiceCount"]

# ── All 32 features in the EXACT order the model expects ──
# (extracted from model.feature_names_in_)
MODEL_FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",                              # scaled
    "PhoneService",
    "PaperlessBilling",
    "MonthlyCharges",                      # scaled
    "TotalCharges",                        # scaled
    "AvgMonthlySpend",                     # scaled
    "ServiceCount",                        # scaled
    "MultipleLines_No phone service",
    "MultipleLines_Yes",
    "InternetService_Fiber optic",
    "InternetService_No",
    "OnlineSecurity_No internet service",
    "OnlineSecurity_Yes",
    "OnlineBackup_No internet service",
    "OnlineBackup_Yes",
    "DeviceProtection_No internet service",
    "DeviceProtection_Yes",
    "TechSupport_No internet service",
    "TechSupport_Yes",
    "StreamingTV_No internet service",
    "StreamingTV_Yes",
    "StreamingMovies_No internet service",
    "StreamingMovies_Yes",
    "Contract_One year",
    "Contract_Two year",
    "PaymentMethod_Credit card (automatic)",
    "PaymentMethod_Electronic check",
    "PaymentMethod_Mailed check",
]


def encode_input(data):
    """
    Convert the friendly JSON input into the 32-feature vector
    that the model was trained on.

    Numeric columns are scaled. Categorical columns are one-hot
    encoded to match what pd.get_dummies() produced during training.
    """

    # ── 1. Start with all zeros (default = 'No' for every flag) ──
    row = {col: 0 for col in MODEL_FEATURES}

    # ── 2. Numeric fields (will be scaled below) ──────────────────
    row["gender"]          = 1 if data.get("gender", "Male") == "Male" else 0
    row["SeniorCitizen"]   = int(data.get("SeniorCitizen", 0))
    row["Partner"]         = 1 if data.get("Partner", "No") == "Yes" else 0
    row["Dependents"]      = 1 if data.get("Dependents", "No") == "Yes" else 0
    row["PhoneService"]    = 1 if data.get("PhoneService", "Yes") == "Yes" else 0
    row["PaperlessBilling"]= 1 if data.get("PaperlessBilling", "No") == "Yes" else 0

    # Computed / directly passed numeric values
    tenure           = float(data.get("tenure", 1))
    monthlyCharges   = float(data.get("MonthlyCharges", 0))
    totalCharges     = float(data.get("TotalCharges", monthlyCharges * tenure))
    avgMonthlySpend  = float(data.get("AvgMonthlySpend", monthlyCharges))
    serviceCount     = int(data.get("ServiceCount", 1))

    # ── 3. Scale the 5 numeric columns ────────────────────────────
    numeric_values = np.array([[tenure, monthlyCharges, totalCharges, avgMonthlySpend, serviceCount]])
    scaled = scaler.transform(numeric_values)[0]

    row["tenure"]          = scaled[0]
    row["MonthlyCharges"]  = scaled[1]
    row["TotalCharges"]    = scaled[2]
    row["AvgMonthlySpend"] = scaled[3]
    row["ServiceCount"]    = scaled[4]

    # ── 4. One-hot: MultipleLines ──────────────────────────────────
    ml = data.get("MultipleLines", "No")
    if ml == "No phone service":
        row["MultipleLines_No phone service"] = 1
    elif ml == "Yes":
        row["MultipleLines_Yes"] = 1
    # "No" → both flags stay 0

    # ── 5. One-hot: InternetService ────────────────────────────────
    internet = data.get("InternetService", "DSL")
    if internet == "Fiber optic":
        row["InternetService_Fiber optic"] = 1
    elif internet == "No":
        row["InternetService_No"] = 1
    # "DSL" → both flags stay 0

    # ── 6. Helper for Yes / No internet service columns ───────────
    no_inet = (internet == "No")

    def binary_service(field, yes_key, noint_key, default="No"):
        val = data.get(field, default)
        if no_inet:
            row[noint_key] = 1
        elif val == "Yes":
            row[yes_key] = 1

    binary_service("OnlineSecurity",   "OnlineSecurity_Yes",   "OnlineSecurity_No internet service")
    binary_service("OnlineBackup",     "OnlineBackup_Yes",     "OnlineBackup_No internet service")
    binary_service("DeviceProtection", "DeviceProtection_Yes", "DeviceProtection_No internet service")
    binary_service("TechSupport",      "TechSupport_Yes",      "TechSupport_No internet service")
    binary_service("StreamingTV",      "StreamingTV_Yes",      "StreamingTV_No internet service")
    binary_service("StreamingMovies",  "StreamingMovies_Yes",  "StreamingMovies_No internet service")

    # ── 7. One-hot: Contract ───────────────────────────────────────
    contract = data.get("Contract", "Month-to-month")
    if contract == "One year":
        row["Contract_One year"] = 1
    elif contract == "Two year":
        row["Contract_Two year"] = 1

    # ── 8. One-hot: PaymentMethod ──────────────────────────────────
    payment = data.get("PaymentMethod", "Bank transfer (automatic)")
    if payment == "Credit card (automatic)":
        row["PaymentMethod_Credit card (automatic)"] = 1
    elif payment == "Electronic check":
        row["PaymentMethod_Electronic check"] = 1
    elif payment == "Mailed check":
        row["PaymentMethod_Mailed check"] = 1

    # ── 9. Return as ordered array ────────────────────────────────
    return np.array([row[col] for col in MODEL_FEATURES]).reshape(1, -1)


# ── Health check ───────────────────────────
@app.route("/", methods=["GET"])
def health():
    return jsonify({"message": "Flask ML Service Running"})


# ── Prediction endpoint ────────────────────
@app.route("/predict", methods=["POST"])
def predict():
    # 1. Read the JSON body
    data = request.get_json()

    # 2. Build the 32-feature vector
    features = encode_input(data)

    # 3. Predict (0 = Not Churn, 1 = Churn)
    prediction  = model.predict(features)[0]

    # 4. Probability of churn (class index 1)
    probability = model.predict_proba(features)[0][1]

    # 5. Human-readable label
    label = "Likely to Churn" if prediction == 1 else "Not Likely to Churn"

    return jsonify({
        "prediction": label,
        "probability": round(float(probability), 2)
    })


# ── Run on port 5000 ──────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
