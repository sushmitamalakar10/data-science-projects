# 🌸 Period Prediction App

This is a **Period Prediction** web application built with **Streamlit**. It predicts the number of days left until your next period based on various inputs like **cycle length**, **mood**, **stress**, **sleep hours**, **pain level**, **PMS symptoms**, and more.

The app uses **machine learning models** (Random Forest and XGBoost) to predict the next period based on historical data and personal health information.

## Features:
- **Input Parameters**: 
  - Last period date
  - Previous cycle length
  - Pain level
  - Wellness scores (Mood, Energy, Stress, Health, Concentration)
  - Flow level (None, Light, Moderate, Heavy)
  - Premenstrual symptoms
  - Preparedness before period (Pads, meds, rest)
  - Ovulation status
  - Cycle phase (Menstrual, Follicular, Luteal)

- **Predictions**:
  - Days left until the next period
  - Predicted date of the next period

## Models:
The app uses two different models for prediction:
1. **Random Forest Regression**
2. **XGBoost Regression**

## Requirements:
- Python 3.7+
- Streamlit
- Pandas
- Joblib
- Scikit-learn
- XGBoost

You can install the required packages by running:

```bash
pip install streamlit pandas joblib scikit-learn xgboost
