import streamlit as st
import joblib
import pandas as pd

# ----------------------------
# Load trained model
# ----------------------------
model = joblib.load("random_forest_model.pkl")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# ----------------------------
# Title
# ----------------------------
st.title("🎓 Student Placement Predictor")

st.markdown("""
This application predicts whether a student is **likely to be placed**
based on academic and extracurricular performance using a **Random Forest Machine Learning model**.
""")

st.info(
    "Please enter values within the ranges used during model training for the most reliable prediction."
)

st.divider()

# ----------------------------
# Input Section
# ----------------------------

st.subheader("📋 Student Details")

iq = st.number_input(
    "IQ",
    min_value=41,
    max_value=158,
    value=100,
    help="Valid range: 41 - 158"
)

cgpa = st.number_input(
    "CGPA",
    min_value=4.54,
    max_value=10.00,
    value=7.50,
    step=0.01,
    format="%.2f",
    help="Valid range: 4.54 - 10.00"
)

academic = st.slider(
    "Academic Performance",
    min_value=1,
    max_value=10,
    value=5,
    help="Score between 1 and 10"
)

internship = st.selectbox(
    "Internship Experience",
    ["No", "Yes"]
)

extra = st.slider(
    "Extra Curricular Score",
    min_value=0,
    max_value=10,
    value=5
)

communication = st.slider(
    "Communication Skills",
    min_value=1,
    max_value=10,
    value=5
)

projects = st.slider(
    "Projects Completed",
    min_value=0,
    max_value=5,
    value=2
)

# Convert Internship to numerical
internship_value = 1 if internship == "Yes" else 0

st.divider()

# ----------------------------
# Prediction
# ----------------------------

if st.button("🔍 Predict Placement"):

    input_df = pd.DataFrame(
        [[
            iq,
            cgpa,
            academic,
            internship_value,
            extra,
            communication,
            projects
        ]],
        columns=[
            "IQ",
            "CGPA",
            "Academic_Performance",
            "Internship_Experience",
            "Extra_Curricular_Score",
            "Communication_Skills",
            "Projects_Completed"
        ]
    )

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    confidence = probability[0][prediction[0]] * 100

    st.subheader("📊 Input Summary")

    st.dataframe(input_df, use_container_width=True)

    st.subheader("🎯 Prediction Result")

    if prediction[0] == 1:
        st.success("🎉 Student is likely to be Placed")
    else:
        st.error("❌ Student is likely to NOT be Placed")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

st.divider()

st.caption(
    "Model: Random Forest Classifier | Dataset: Student Placement Dataset | Developed using Streamlit"
)