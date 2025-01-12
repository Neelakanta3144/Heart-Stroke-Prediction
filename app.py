import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model=pickle.load(open('model.pkl','rb'))

def main():
    st.title("Heart Stroke Prediction App")
    st.markdown("This app predicts the probability of a stroke based on user input.")

    # User inputs for the features
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
    hypertension = st.selectbox("Hypertension", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    heart_disease = st.selectbox("Heart Disease", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=100.0, step=0.1)
    bmi = st.number_input("BMI", min_value=0.0, value=25.0, step=0.1)

    # Gender options
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    gender_features = [1 if gender == "Female" else 0, 1 if gender == "Male" else 0, 1 if gender == "Other" else 0]

    # Work type options
    work_type = st.selectbox("Work Type", ["Govt_job", "Never_worked", "Private", "Self-employed", "children"])
    work_features = [1 if work_type == wt else 0 for wt in ["Govt_job", "Never_worked", "Private", "Self-employed", "children"]]

    # Residence type
    residence_type = st.selectbox("Residence Type", ["Rural", "Urban", "Unknown"])
    residence_features = [1 if residence_type == rt else 0 for rt in ["Rural", "Urban", "Unknown"]]

    # Smoking status
    smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes"])
    smoking_features = [1 if smoking_status == ss else 0 for ss in ["formerly smoked", "never smoked", "smokes"]]

    # Combine all inputs into a single array
    features = [
        age,
        hypertension,
        heart_disease,
        avg_glucose_level,
        bmi,
        *gender_features,
        *work_features,
        *residence_features,
        *smoking_features
    ]

    # Predict button
    if st.button("Predict"):
        prediction = model.predict([features])
        probability = model.predict_proba([features])[0][1]  # Probability of stroke

        st.write(f"Prediction: {'Stroke' if prediction[0] == 1 else 'No Stroke'}")
        st.write(f"Probability of Stroke: {probability * 100:.2f}%")

if __name__ == "__main__":
    main()
