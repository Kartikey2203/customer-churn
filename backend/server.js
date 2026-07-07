// ────────────────────────────────────────────
//  Express Backend – Customer Churn Prediction
//  Acts as a bridge between the Next.js
//  frontend and the Flask ML service.
// ────────────────────────────────────────────

const express = require("express");
const axios   = require("axios");
const cors    = require("cors");

// ── App setup ──────────────────────────────
const app  = express();
const PORT = 3001; // Express runs on 3001 so it doesn't clash with Next.js

// ── Middleware ─────────────────────────────
app.use(cors());        // Allow requests from the Next.js frontend
app.use(express.json()); // Parse incoming JSON request bodies


// ── API 1: Health check ────────────────────
// GET /  →  confirms the backend is alive
app.get("/", (req, res) => {
  res.json({ message: "Customer Churn Backend Running" });
});


// ── API 2: Prediction proxy ────────────────
// POST /predict  →  forwards the request to Flask and returns the result
app.post("/predict", async (req, res) => {
  try {
    // 1. Forward the customer data to the Flask ML service
    const flaskResponse = await axios.post(
      "http://localhost:5000/predict",
      req.body
    );

    // 2. Return exactly what Flask sent back
    res.json(flaskResponse.data);

  } catch (error) {
    // If Flask is down or something went wrong, return a clear error
    res.status(500).json({ error: "Could not reach the ML service. Is Flask running?" });
  }
});


// ── Start server ───────────────────────────
app.listen(PORT, () => {
  console.log(`Express server running at http://localhost:${PORT}`);
});
