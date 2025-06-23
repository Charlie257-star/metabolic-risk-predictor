
# 🧠 Metabolic Syndrome Risk Predictor

A machine learning web app that predicts the risk of **metabolic syndrome** based on biometric and lifestyle data. This project supports the goals of **weight-inclusive, preventive healthcare** and demonstrates how data science can improve early detection and patient support.

---

## 🚀 Live Demo

👉 [Try the Streamlit App Here](https://your-app.streamlit.app)

---

## 📊 Tools Used

- **Python** (pandas, numpy, matplotlib, seaborn)
- **Machine Learning**: XGBoost Classifier
- **Web App**: Streamlit
- **IDE**: Jupyter Notebook & VS Code

---

## 🔍 Problem Statement

**Metabolic Syndrome** is a group of conditions (like high blood pressure, obesity, and insulin resistance) that increase the risk of heart disease and diabetes. Early risk prediction can help prevent serious health complications.

This project builds a predictive model to assess an individual's risk level based on health metrics, and provides a simple user interface for use by patients or healthcare professionals.

---

## 💾 Dataset

- Source: Public health datasets (e.g., NHANES, Kaggle)
- Features: Age, BMI, Glucose, Blood Pressure, Triglycerides, Gender, Smoking Status

---

## 🧠 How It Works

1. Train a model using XGBoost to classify risk
2. Save the trained model using `pickle`
3. Build a Streamlit app to take user input and display risk results
4. Host the app publicly on Streamlit Cloud

---

## 📁 Project Structure
metabolic-risk-predictor/
├── app.py # Streamlit app interface
├── model.pkl # Trained XGBoost model
├── requirements.txt # Dependencies for deployment
├── README.md # This file
├── notebook.ipynb # Full data analysis and model building