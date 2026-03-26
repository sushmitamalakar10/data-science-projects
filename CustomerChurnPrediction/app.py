import streamlit as st
import pandas as pd
import joblib
import numpy as np

@st.cache_resource
def load_artifacts():
    model = joblib.load('rf_randomcv_best.pkl')
    encoders = joblib.load('encoders.pkl')
    return model, encoders

model, encoders = load_artifacts()

# Title
st.title("Telco Customer Churn Prediction")
st.write("Enter customer details to predict churn.")

# Input fields based on data features
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12, step=1)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])

with col2:
    multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])

with col3:
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges", min_value=18.0, max_value=120.0, value=70.0, step=0.05)

total_charges = st.number_input("Total Charges", min_value=0.0, max_value=9000.0, value=800.0, step=0.05)

# Predict button
if st.button("Predict Churn"):
    # Create input dictionary
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    # Convert to DataFrame
    df_input = pd.DataFrame([input_data])

    # Apply label encoding using saved encoders
    for col in encoders:
        if col in df_input.columns:
            le = encoders[col]
            # Handle unknown values by mapping to a known class (e.g., first one)
            df_input[col] = df_input[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
            df_input[col] = le.transform(df_input[col])

    # Ensure numeric types
    df_input['tenure'] = df_input['tenure'].astype(int)
    df_input['MonthlyCharges'] = df_input['MonthlyCharges'].astype(float)
    df_input['TotalCharges'] = df_input['TotalCharges'].astype(float)

    # Prediction
    prob = model.predict_proba(df_input)[0][1]
    pred = "Yes" if prob > 0.5 else "No"

    st.markdown("---")
    st.subheader("Prediction Result")
    st.write(f"**Churn Prediction:** {pred}")
    st.write(f"**Churn Probability:** {prob:.1%}")

    if pred == "Yes":
        st.error("High risk of churn! Consider retention strategies.")
    else:
        st.success("Low risk of churn. Customer likely to stay.")