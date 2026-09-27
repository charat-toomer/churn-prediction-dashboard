# 📉 Customer Churn Prediction Dashboard

A Plotly Dash web app that predicts telecom customer churn probability in real time using a trained Logistic Regression model.

🌐 **Live Demo:** https://churn-prediction-dashboard-e756.onrender.com

## ✨ Features

- Predict churn probability instantly based on customer inputs
- Input fields: Contract type, tenure, monthly charges, internet service type
- Trained on IBM/Kaggle Telco Customer Churn dataset (7,043 customers)
- Clean, interactive Dash UI with real-time prediction output
- Fully containerised with Docker for easy deployment

## 🛠️ Tech Stack

`Python` `Plotly Dash` `Scikit-learn` `Logistic Regression` `Pandas` `Docker`

## 📊 Dataset

- **Source:** IBM Telco Customer Churn (Kaggle)
- **Size:** 7,043 customers, 21 features
- **Target:** Binary churn classification (Yes / No)

## 🚀 How to Run

### Option 1 — Run with Docker (recommended)
```bash
git clone https://github.com/charat-toomer/churn-prediction-dashboard.git
cd churn-prediction-dashboard
docker build -t churn-dashboard .
docker run -p 8050:8050 churn-dashboard
```
Then open `http://localhost:8050` in your browser.

### Option 2 — Run locally
```bash
git clone https://github.com/charat-toomer/churn-prediction-dashboard.git
cd churn-prediction-dashboard
pip install -r requirements.txt
python app.py
```

## 📁 Project Structure
