import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set Streamlit page configuration
st.set_page_config(page_title="Metabolic Syndrome Risk Predictor", layout="centered")

# App title and description
st.title("🧠 Metabolic Syndrome Risk Predictor")
st.markdown("A machine learning demo that predicts your risk of metabolic syndrome based on key health and lifestyle metrics.")

# Load the trained model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# Input form
st.header("📋 Enter Your Health Metrics")
with st.form("input_form"):
    age = st.slider("Age", 18, 90, 35)
    sex = st.selectbox("Sex", ["Male", "Female"])
    bmi = st.slider("BMI", 15.0, 45.0, 25.0)
    glucose = st.slider("Fasting Glucose (mg/dL)", 60, 200, 90)
    systolic_bp = st.slider("Systolic BP (mm Hg)", 90, 200, 120)
    diastolic_bp = st.slider("Diastolic BP (mm Hg)", 60, 120, 80)
    triglycerides = st.slider("Triglycerides (mg/dL)", 50, 400, 150)
    smoker = st.selectbox("Do you smoke?", ["No", "Yes"])

    submitted = st.form_submit_button("🔍 Predict Risk")

# Process input and predict
if submitted:
    sex_encoded = 1 if sex == "Male" else 0
    smoker_encoded = 1 if smoker == "Yes" else 0

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex_encoded],
        "bmi": [bmi],
        "glucose": [glucose],
        "systolic_bp": [systolic_bp],
        "diastolic_bp": [diastolic_bp],
        "triglycerides": [triglycerides],
        "smoker": [smoker_encoded]
    })

    try:
        prediction = model.predict(input_data)[0]
        risk_score = model.predict_proba(input_data)[0][1]

        st.subheader("🧾 Risk Assessment Result")
        if prediction == 1:
            st.error(f"⚠️ High risk of metabolic syndrome.\n\n**Risk Score:** {risk_score:.2%}")
        else:
            st.success(f"✅ Low risk of metabolic syndrome.\n\n**Risk Score:** {risk_score:.2%}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# Footer
st.markdown("---")
st.caption("Made by Charles Otieno | [GitHub](https://github.com/charlie257)")