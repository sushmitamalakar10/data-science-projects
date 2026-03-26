# Telco Customer Churn Prediction

A machine learning project to predict customer churn for telecommunications companies using ensemble and tree-based classification models. 

## 📊 Project Overview

**Objective:** Build a predictive model to identify which customers are likely to churn (leave) the telecom company.

**Dataset:** Telco Customer Churn Dataset
- **Total Records:** 7,043 customers
- **Features:** 19 input features (after preprocessing)
- **Target Variable:** Churn (Yes/No)
- **Class Distribution:** 
  - No Churn: 5,174 
  - Churn: 1,869 
  - **Class Imbalance Handled:** SMOTE (Synthetic Minority Over-sampling Technique)


## 📋 Features

### Customer Demographics
- Gender
- Senior Citizen (0/1)
- Partner (Yes/No)
- Dependents (Yes/No)

### Service Subscriptions
- Phone Service
- Multiple Lines
- Internet Service (DSL, Fiber optic, No)
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies

### Account Information
- Tenure (months with company)
- Contract Type (Month-to-month, One year, Two year)
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

## 🔄 Data Processing Pipeline

### 1. **Data Cleaning**
- Removed `customerID` (non-predictive identifier)
- Handled 11 empty values in `TotalCharges` column (replaced with 0.0)
- Converted `TotalCharges` from object to float type
- No missing values in remaining features

### 2. **Exploratory Data Analysis (EDA)**
- Statistical distribution analysis of numerical features
- Categorical feature frequency analysis
- Correlation analysis (Tenure, Monthly Charges, Total Charges)
- Visual exploration with histograms, box plots, and count plots

### 3. **Feature Encoding**
- **Categorical Variables:** Label Encoding using scikit-learn's `LabelEncoder`
- **Target Variable:** Binary encoding (Yes=1, No=0)
- **Encoder Persistence:** All 15 encoders saved in `encoders.pkl` for production inference

### 4. **Class Imbalance Handling**
- **Technique:** SMOTE (Synthetic Minority Over-sampling)
- **Result:** Balanced training set (4,138 samples per class)
- **Application:** Applied to training set only; test set remains untouched

### 5. **Train-Test Split**
- **Test Size:** 20% 
- **Training Size:** 80%
- **Random State:** 42 (reproducibility)

## 🤖 Machine Learning Models

Three ensemble and tree-based models were trained, hyperparameter-tuned, and evaluated:

### 1. **Random Forest Classifier**
### 2. **Decision Tree Classifier**
### 3. **Gradient Boosting Classifier** 


## 🔧 Technologies & Libraries

# Core Libraries
- **numpy**         
- **pandas**          
- **scikit-learn**      
- **imbalanced-learn** 
- **matplotlib**        
- **seaborn**          
- **joblib**            
- **pickle**             





