import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, timedelta

@st.cache_resource
def load_artifacts():
    # model1 = joblib.load('model/rf_randomcv.pkl')  # Random Forest model
    model2 = joblib.load('model/xgb_randomcv.pkl')  # XGBoost model

    # return model1, model2
    return model2

# Load models
# model1, model2 = load_artifacts()

model2 = load_artifacts()

st.title("🌺 Period Prediction")

# Last period
last_period = st.date_input(
    "🩸 Last period date",
    value=datetime.now().date() - timedelta(days=28)
)

# Cycle info
col1, col2 = st.columns(2)
prev_cycle_length = col1.slider("Previous Cycle Length (Days)", 20, 45, 28)
pain = col2.slider("😣 Pain Level (1-10)", 1, 10, 1)

# Wellness info
col1, col2, col3 = st.columns(3)
mood = col1.slider("😊 Mood Score", 1, 10, 7)
energy = col2.slider("⚡ Energy Level", 1, 10, 6)
stress = col3.slider("🧠 Stress Score", 1, 10, 4)

col1, col2, col3 = st.columns(3)
sleep_hours = col1.slider("😴 Sleep Hours", 0, 10, 7, 1)
health = col2.slider("✨ Overall Health Score", 1, 10, 7)
concentration = col3.slider("🎯 Concentration Score", 1, 10, 7)

col1, col2 = st.columns(2)
pms_val = 1 if col1.checkbox("🤕 Premenstrual Symptoms") else 0
flow = col2.selectbox("💧 Flow Level", ["None", "Light", "Medium", "Heavy"])

flow_light = 1 if flow in ["None", "Light"] else 0
flow_medium = 1 if flow == "Medium" else 0
flow_heavy = 1 if flow == "Heavy" else 0

prepared_val = 1 if st.checkbox("Prepared Before Period (pads/meds/rest)") else 0

input_data = pd.DataFrame([{
    "prev_cycle_length": prev_cycle_length,
    "pain_level": pain,
    "pms_symptoms": pms_val,
    "mood_score": mood,
    "stress_score_cycle": stress,
    "sleep_hours_cycle": sleep_hours,
    "energy_level": energy,
    "concentration_score": concentration,
    "overall_health_score": health,
    "prepared_before_period": prepared_val,
    "flow_level_Heavy": flow_heavy,
    "flow_level_Light": flow_light,
    "flow_level_Moderate": flow_medium,
}])

if st.button("Predict Period"):
    # Predict using both models
    # days_to_period_model1 = model1.predict(input_data)[0]
    # days_to_period_model1 = max(0, round(days_to_period_model1))

    days_to_period_model2 = model2.predict(input_data)[0]
    days_to_period_model2 = max(0, round(days_to_period_model2))

    col1, col2 = st.columns(2)
    # col1.metric("Days Left (Model 1)", days_to_period_model1)
    col1.metric("Days Left", days_to_period_model2)

    # next_period_date_model1 = last_period + timedelta(days=days_to_period_model1)
    next_period_date_model2 = last_period + timedelta(days=days_to_period_model2)

    col1, col2 = st.columns(2)
    # col1.metric("Predicted Date (Model 1)", next_period_date_model1.strftime("%d %b %Y"))
    col1.metric("Predicted Date", next_period_date_model2.strftime("%d %b %Y"))
    
