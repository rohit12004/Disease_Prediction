### Documentation File (documentation.md)

```markdown
# Disease Prediction Project Documentation

## Overview
The Disease Prediction project aims to develop machine learning models that can predict various diseases based on patient data and symptoms. The project includes models for Diabetes, Chronic Kidney Disease (CKD), Heart Disease, Parkinson's Disease, and Liver Disease,
and symptoms based model.


## Requirements
- Python
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - xgboost
  - flask
  - matplotlib


## Features
- **Disease Prediction**: Predict diseases based on user input.
- **Symptom-Based Prediction**: Predict diseases based on selected symptoms.
- **Model Training**: Train models using various algorithms (SVM, Random Forest, Logistic Regression, etc.).
- **Visualization**: Display prediction probabilities and feature importance.

## Models
- **Diabetes Prediction**: Uses the PIMA Diabetes dataset.
- **CKD Prediction**: Uses the CKD dataset.
- **Heart Disease Prediction**: Uses the Heart Disease dataset.
- **Parkinson's Prediction**: Uses the Parkinson's dataset.
- **Liver Disease Prediction**: Uses the Liver Disease dataset.


# Disease Prediction Inputs

Here is a list of inputs required for each disease prediction:

---

## 1. **Diabetes Prediction**
- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 2. **Heart Disease Prediction**
- Age
- Sex (Male: 1, Female: 0)
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Max Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Major Vessels
- Thalassemia

---

## 3. **Parkinson's Disease Prediction**
- MDVP: Fo(Hz)
- MDVP: Fhi(Hz)
- MDVP: Flo(Hz)
- MDVP: Jitter(%)
- MDVP: Jitter(Abs)
- MDVP: RAP
- MDVP: PPQ
- Jitter: DDP
- MDVP: Shimmer
- MDVP: Shimmer(dB)
- Shimmer: APQ3
- Shimmer: APQ5
- MDVP: APQ
- Shimmer: DDA
- NHR
- HNR
- RPDE
- DFA
- Spread1
- Spread2
- D2
- PPE

---

## 4. **Chronic Kidney Disease (CKD) Prediction**
- Blood Pressure (Bp)
- Specific Gravity (Sg)
- Albumin (Al)
- Sugar (Su)
- Red Blood Cell Count (Rbc)
- Blood Urea (Bu)
- Serum Creatinine (Sc)
- Sodium (Sod)
- Potassium (Pot)
- Hemoglobin (Hemo)
- White Blood Cell Count (Wbcc)
- Red Blood Cell Count (Rbcc)
- Hypertension (Htn)

---

## 5. **Liver Disease Prediction**
- Age
- Gender (Male: 0, Female: 1)
- BMI
- Alcohol Consumption (No: 0, Yes: 1)
- Smoking (No: 0, Yes: 1)
- Genetic Risk (Low: 0, Medium: 1, High: 2)
- Physical Activity (0-10 hours per week)
- Diabetes (No: 0, Yes: 1)
- Hypertension (No: 0, Yes: 1)
- Liver Function Test (20-100)

---

## 6. **Symptom-Based Disease Prediction**
- Select up to 6 symptoms from a predefined list of symptoms.
