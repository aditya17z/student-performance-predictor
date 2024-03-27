import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
model = pickle.load(open('model (2).pkl', 'rb'))

# Function to predict
def predict_performance(data):
    return model.predict(data)

def main():
    st.title('Student Performance Predictor 📊')

    # Input fields
    st.header('Student details')
    age = st.number_input('Age', min_value=0, max_value=100, step=1)
    cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, step=0.1)
    sem1_marks = st.number_input('Marks obtained in Semester 1 (MSc)', min_value=0, max_value=100, step=1)
    sem2_marks = st.number_input('Marks obtained in Semester 2 (MSc)', min_value=0, max_value=100, step=1)
    attendance = st.number_input('Attendance (%)', min_value=0, max_value=100, step=1)
    hours_per_day = st.number_input('Study hours per day', min_value=0, max_value=24, step=1)
    currently_working = st.selectbox('Currently Working', ['No', 'Yes'])
    student_status = st.selectbox('Student Status', ['No', 'Yes'])
    gender = st.radio('Gender', ['Female', 'Male'])
    financial_support = st.selectbox('Financial Support', ['No', 'Yes'])
    learning_needs = st.selectbox('Learning Needs', ['No', 'Yes'])
    study_motivation = st.selectbox('Study Motivation', ['Consistent studying', 'Exam cramming'])
    extracurricular_activities = st.selectbox('Extracurricular Activities', ['Maybe', 'No', 'Yes'])
    study_materials = st.selectbox('Study Materials', ['No', 'Yes'])
    mental_health = st.selectbox('Mental Health', ['Balanced', 'Struggling'])
    peers = st.selectbox('Peers', ['Indifferent', 'Pleasant', 'Unpleasant'])

    # Convert categorical features to binary
    gender_female = 1 if gender == 'Female' else 0
    gender_male = 1 if gender == 'Male' else 0
    currently_working_status = 1 if currently_working == 'Yes' else 0
    student_status_yes = 1 if student_status == 'Yes' else 0
    financial_support_yes = 1 if financial_support == 'Yes' else 0
    learning_needs_yes = 1 if learning_needs == 'Yes' else 0
    extracurricular_maybe = 1 if extracurricular_activities == 'Maybe' else 0
    extracurricular_no = 1 if extracurricular_activities == 'No' else 0
    extracurricular_yes = 1 if extracurricular_activities == 'Yes' else 0
    study_materials_yes = 1 if study_materials == 'Yes' else 0
    mental_health_balanced = 1 if mental_health == 'Balanced' else 0
    peers_indifferent = 1 if peers == 'Indifferent' else 0
    peers_pleasant = 1 if peers == 'Pleasant' else 0
    peers_unpleasant = 1 if peers == 'Unpleasant' else 0

    # Prepare input data for prediction
    input_data = {
        'Age': age,
        'CGPA': cgpa,
        'sem 1(MSc)': sem1_marks,
        'sem 2(MSc)': sem2_marks,
        'attendance': attendance,
        'hours per day ': hours_per_day,
        'status_Currently working.': currently_working_status,
        'status_Student.': student_status_yes,
        'Gender_Female.': gender_female,
        'Gender_Male.': gender_male,
        'financial support_No': 1 if financial_support == 'No' else 0,
        'financial support_Yes': financial_support_yes,
        ' learning needs_No.': 1 if learning_needs == 'No' else 0,
        ' learning needs_Yes.': learning_needs_yes,
        'study motivation_Consistent studying': 1 if study_motivation == 'Consistent studying' else 0,
        'study motivation_Exam cramming': 1 if study_motivation == 'Exam cramming' else 0,
        ' extracurricular _Maybe': extracurricular_maybe,
        ' extracurricular _No': extracurricular_no,
        ' extracurricular _Yes': extracurricular_yes,
        ' study materials_No': 1 if study_materials == 'No' else 0,
        ' study materials_Yes': study_materials_yes,
        'mental health_Balanced': mental_health_balanced,
        'mental health_Struggling': 1 if mental_health == 'Struggling' else 0,
        'peers_Indifferent ': peers_indifferent,
        'peers_Pleasant': peers_pleasant,
        'peers_Unpleasant': peers_unpleasant
    }

    input_df = pd.DataFrame([input_data])

    if st.button('Predict 3rd Semester Performance'):
        prediction = predict_performance(input_df)
        st.subheader('Predicted 3rd Semester Performance')
        st.write(prediction)

if __name__ == '__main__':
    main()
