import streamlit as st, requests
from student_score_prediction import confidence_interval



st.markdown("<h1 style='text-align: center; color: #166d3b;'>STUDENT EXAM SCORE PREDICTOR</h1>", unsafe_allow_html=True)
st.markdown("> Fill in the details below to estimate the likely exam score and prediction confidence!")


# Input widgets for features
study_hours_per_day = st.number_input("Study Hours per Day", min_value=0.0, max_value=24.0, value=3.5, step=0.1, format="%.1f")
part_time_job = st.selectbox("Part-time Job", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
attendance_percentage = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0, value=84.0, step=0.1, format="%.1f")
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.0, step=0.1, format="%.1f")
mental_health_rating = st.slider("Mental Health Rating (1-10)", 1, 10, 7)
extracurricular_participation = st.selectbox("Extracurricular Participation", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
social_media_netflix_hrs = st.number_input("Social Media + Netflix Hours", min_value=0.0, max_value=24.0, value=3.0, step=0.1, format="%.1f")


# Button to trigger prediction
if st.button("Predict Exam Score",type="primary"):
    # Prepare input list
    input_features = [
        study_hours_per_day,
        part_time_job,
        attendance_percentage,
        sleep_hours,
        mental_health_rating,
        extracurricular_participation,
        social_media_netflix_hrs
    ]

    prediction,confidence=confidence_interval(input_features)
    st.metric("Predicted Exam Score", f"{prediction:.2f}")
    st.success(f"Prediction Confidence: **{confidence}**")

st.sidebar.title("About App")
st.sidebar.write("This app predicts student exam scores using machine learning based on daily habits, participation, and ratings. Confidence intervals help you judge reliability.")

# Optional clear input button
if st.button("Clear"):
    st.rerun()
