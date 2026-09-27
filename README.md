# 📉 Customer Churn Prediction Dashboard

A real-time web app that predicts telecom customer churn probability using a trained Logistic Regression model — built with Plotly Dash and deployed on Render.

🌐 **Live Demo:** https://churn-prediction-dashboard-e756.onrender.com

---

## ✨ Features

- **4 interactive inputs:** Contract type (dropdown), Tenure (slider 0–72 months), Monthly Charges (slider $18–$120), Internet Service (dropdown)
- **Real-time prediction:** Churn probability updates instantly on every input change via Dash callbacks — no page reload
- **Feature engineering at inference:** Auto-computes TotalCharges (tenure × monthly), avg_monthly_spend, num_services from raw inputs
- **One-hot encoding at runtime:** Contract and Internet Service encoded dynamically to match training feature columns
- **StandardScaler preprocessing:** Numeric features scaled using the same scaler fitted during training
- Trained on IBM/Kaggle Telco Customer Churn dataset — 7,043 customers, 21 features
- Fully containerised with Docker, served with Gunicorn in production

## 🛠️ Tech Stack

`Python` `Plotly Dash` `Scikit-learn` `Logistic Regression` `Pandas` `Joblib` `Docker` `Gunicorn` `Render`

## 📊 Dataset

- **Source:** IBM Telco Customer Churn (Kaggle)
- **Size:** 7,043 customers, 21 features
- **Target:** Binary churn classification (Churn: Yes / No)
- **Key features used:** Contract type, Tenure, Monthly Charges, Internet Service

## 🧠 How It Works

```
User Input (4 fields)
        ↓
Feature Engineering
  - TotalCharges = tenure × MonthlyCharges
  - avg_monthly_spend = MonthlyCharges
  - num_services = 2 (default)
        ↓
One-Hot Encoding
  - Contract_One year / Contract_Two year
  - InternetService_Fiber optic / InternetService_No
        ↓
StandardScaler (loaded from scaler.pkl)
        ↓
Logistic Regression (loaded from model.pkl)
        ↓
Churn Probability (%) → displayed instantly
```

## 🚀 How to Run

### Option 1 — Docker (recommended)
```bash
git clone https://github.com/charat-toomer/churn-prediction-dashboard.git
cd churn-prediction-dashboard
docker build -t churn-dashboard .
docker run -p 8050:8050 churn-dashboard
```
Open `http://localhost:8050`

### Option 2 — Local
```bash
git clone https://github.com/charat-toomer/churn-prediction-dashboard.git
cd churn-prediction-dashboard
pip install -r requirements.txt
python app.py
```
Open `http://localhost:7860`

## 📁 Project Structure

```
churn-prediction-dashboard/
├── app.py                # Dash app — layout, callbacks, inference pipeline
├── model.pkl             # Trained Logistic Regression model
├── scaler.pkl            # Fitted StandardScaler for numeric features
├── feature_columns.pkl   # Ordered feature column list for input alignment
├── requirements.txt      # dash, pandas, scikit-learn, joblib, gunicorn
└── Dockerfile            # Container config — Gunicorn on PORT env variable
```

## 💡 What I Learned

- Full ML inference pipeline: feature engineering → encoding → scaling → prediction in one callback
- Serving Dash apps in production with Gunicorn and Docker
- Aligning inference-time features exactly with training-time feature columns using joblib
- Deploying containerised Python ML apps on Render
