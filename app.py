import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(page_title="Metabolic Syndrome Risk Predictor", layout="centered")
st.title("🧠 Metabolic Syndrome Risk Predictor")
st.markdown("A machine learning demo to assess your risk of developing **metabolic syndrome**, based on key health metrics. This project supports equitable, weight-inclusive preventive care.")


with open("model.pkl", "rb") as file:
    model = pickle.load(file)


st.header("📋 Enter Your Health Metrics")
with st.form("input_form"):
    age = st.slider("Age", 18, 90, 35)
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi = st.slider("Body Mass Index (BMI)", 15.0, 50.0, 25.0)
    glucose = st.slider("Fasting Glucose (mg/dL)", 60, 200, 100)
    systolic_bp = st.slider("Systolic Blood Pressure (mm Hg)", 90, 200, 120)
    diastolic_bp = st.slider("Diastolic Blood Pressure (mm Hg)", 60, 120, 80)
    triglycerides = st.slider("Triglycerides (mg/dL)", 50, 400, 150)
    smoker = st.selectbox("Do you smoke?", ["No", "Yes"])

    submitted = st.form_submit_button("🔍 Predict Risk")


if submitted:
    
    gender_encoded = 1 if gender == "Male" else 0
    smoker_encoded = 1 if smoker == "Yes" else 0

    input_df = pd.DataFrame({
        "age": [age],
        "gender": [gender_encoded],
        "bmi": [bmi],
        "glucose": [glucose],
        "systolic_bp": [systolic_bp],
        "diastolic_bp": [diastolic_bp],
        "triglycerides": [triglycerides],
        "smoker": [smoker_encoded]
    })

    
    prediction = model.predict(input_df)[0]
    risk_score = model.predict_proba(input_df)[0][1]

    
    st.subheader("🧾 Risk Assessment Result")
    if prediction == 1:
        st.error(f"⚠️ High risk of metabolic syndrome.\n\n**Risk Score:** {risk_score:.2%}")
        st.markdown("Consider consulting a healthcare provider for preventive steps.")
    else:
        st.success(f"✅ Low risk of metabolic syndrome.\n\n**Risk Score:** {risk_score:.2%}")
        st.markdown("Keep up with healthy habits!")

    
    st.markdown("---")
    st.markdown("**Disclaimer:** This tool is for educational purposes only and should not replace professional medical advice.")


st.markdown("---")
st.caption("Made by Charles Otieno | [GitHub](https://github.com/charlie257/charles-otieno-ds-projects)")