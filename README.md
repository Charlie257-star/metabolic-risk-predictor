
# 🧠 Metabolic Syndrome Risk Predictor

A machine learning web app that predicts the risk of **metabolic syndrome** based on biometric and lifestyle data. This project supports the goals of **weight-inclusive, preventive healthcare** and demonstrates how data science can improve early detection and patient support.

---

## 🚀 Live Demo

👉 [Try the Streamlit App Here](https://metabolic-risk-predictor-slpdnc4hwwp3ht9qlweruj.streamlit.app/)

---
## 💡 How It Works

1. User enters 5 key health inputs:
   - Age
   - Gender
   - BMI
   - Blood Glucose (mg/dL)
   - Triglycerides (mg/dL)
2. Model processes inputs using a trained `HistGradientBoostingClassifier`

3. Returns:
   - A **Low Risk** ✅ or **High Risk** ⚠️ prediction
   - A risk score percentage (confidence level)

## 🧠 Features

- Trained on a real-world metabolic risk dataset
- Predicts binary classification (0 = low risk, 1 = high risk)
- Interactive, browser-based UI
- Fully open-source and lightweight

## 🔧 Tech Stack

| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Streamlit    | Web app front-end                     |
| scikit-learn | ML model using HistGradientBoosting   |
| pandas       | Data wrangling                        |
| numpy        | Numerical operations                  |
| matplotlib   | Visualizations (EDA)                  |
| seaborn      | Correlation and distribution plots    |
---


---

## 💾 Dataset

- Source: Public health datasets (e.g., NHANES, Kaggle)
- Features: Age, BMI, Glucose, Blood Pressure, Triglycerides, Gender, Smoking Status

---
## 📦 Installation (Run Locally)

```bash
# 1. Clone repo
git clone https://github.com/Charlie257-star/metabolic-risk-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app.py
---

## 📁 Project Structure
metabolic-risk-predictor/
├── app.py # Streamlit app interface
├── model.pkl # Trained XGBoost model
├── requirements.txt # Dependencies for deployment
├── README.md # This file
├── notebook.ipynb # Full data analysis and model building

MIT License — free to use, modify, and share.