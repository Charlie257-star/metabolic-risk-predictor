import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page setup
st.set_page_config(page_title="Metabolic Syndrome Risk Predictor", layout="centered")

# App title
st.title("🧠 Metabolic Syndrome Risk Predictor")
st.markdown("A simple app to predict your risk of metabolic syndrome based on health metrics.")

# Load trained model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# Input form
st.header("📋 Input Your Health Data")
with st.form("risk_form"):
    age = st.slider("Age", 18, 90, 35)
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi = st.slider("BMI", 15.0, 50.0, 25.0)
    glucose = st.slider("Blood Glucose (mg/dL)", 60, 200, 90)
    triglycerides = st.slider("Triglycerides (mg/dL)", 50, 400, 150)
    
    submitted = st.form_submit_button("🔍 Predict Risk")

# Prediction
if submitted:
    gender_encoded = 1 if gender == "Male" else 0

    input_df = pd.DataFrame({
        "age": [age],
        "sex": [gender_encoded],
        "bmi": [bmi],
        "glucose": [glucose],
        "triglycerides": [triglycerides]
    })

    try:
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        st.subheader("🧾 Risk Prediction Result")
        if prediction == 1:
            st.error(f"⚠️ You are likely at **high risk**.\n\n**Risk Score:** {probability:.2%}")
        else:
            st.success(f"✅ You are likely at **low risk**.\n\n**Risk Score:** {probability:.2%}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")


# Footer
st.markdown("---")
st.caption("Made by Charles Otieno | [GitHub](https://github.com/charlie257-star)")
