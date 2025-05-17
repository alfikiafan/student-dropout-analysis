import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("model/logreg_model.joblib")
model_columns = joblib.load("model/model_columns.joblib")

st.set_page_config(page_title="Dropout Prediction", layout="wide")
st.title("🎓 Dropout Prediction System")
st.markdown("Enter student data to predict the potential for **Dropout**.")

with st.form("student_form"):
    st.header("🧑 Personal Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"], help="Select the gender of the student")
        age = st.number_input("Age at enrollment", min_value=15, max_value=70, value=20, help="Age when enrolling")
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Widower", "Divorced", "Facto Union", "Legally Separated"], help="Marital status of the student")
        displaced = st.selectbox("Displaced", ["No", "Yes"], help="Whether the student is a displaced person")
    with col2:
        scholarship = st.selectbox("Scholarship Holder", ["No", "Yes"], help="Does the student hold a scholarship?")
        international = st.selectbox("International Student", ["No", "Yes"], help="Is the student international?")
        application_mode = st.selectbox("Application Mode", ["1st phase - general contingent", "Ordinance No. 612/93", "1st phase - special contingent (Azores Island)", 
                                                           "Holders of other higher courses", "Ordinance No. 854-B/99", "International student (bachelor)", 
                                                           "1st phase - special contingent (Madeira Island)", "2nd phase - general contingent", 
                                                           "3rd phase - general contingent", "Ordinance No. 533-A/99, item b2) (Different Plan)", 
                                                           "Ordinance No. 533-A/99, item b3 (Other Institution)", "Over 23 years old", "Transfer", "Change of course", 
                                                           "Technological specialization diploma holders", "Change of institution/course", "Short cycle diploma holders", 
                                                           "Change of institution/course (International)"], help="Method of application used by the student")
        application_order = st.slider("Application Order (0=first choice, 9=last)", 0, 9, 0, help="Order in which the student applied")
    with col3:
        course = st.selectbox("Course", ["Biofuel Production Technologies", "Animation and Multimedia Design", "Social Service (evening attendance)", 
                                        "Agronomy", "Communication Design", "Veterinary Nursing", "Informatics Engineering", "Equinculture", 
                                        "Management", "Social Service", "Tourism", "Nursing", "Oral Hygiene", "Advertising and Marketing Management", 
                                        "Journalism and Communication", "Basic Education", "Management (evening attendance)"], help="The course taken by the student")
        previous_qualification = st.selectbox("Previous Qualification", [
            "Secondary Education", 
            "Higher Education - Bachelor's Degree", "Higher Education - Degree", 
            "Higher Education - Master's", "Higher Education - Doctorate", 
            "Frequency of Higher Education", "12th Year of Schooling - Not Completed", 
            "11th Year of Schooling - Not Completed", "Other - 11th Year of Schooling", 
            "10th Year of Schooling", "10th Year of Schooling - Not Completed", 
            "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent", 
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent", 
            "Technological Specialization Course", "Higher Education - Degree (1st Cycle)", 
            "Professional Higher Technical Course", "Higher Education - Master (2nd Cycle)"
        ], help="Previous qualification obtained before enrolling in higher education")
        prev_qual_grade = st.slider("Previous Qualification Grade", 0, 200, 150, help="Grade of the previous qualification (between 0 and 200)")
        admission_grade = st.slider("Admission Grade", 0, 200, 150, help="Admission grade (between 0 and 200)")

    col4, col5 = st.columns(2)
    with col4:
        daytime_evening_attendance = st.selectbox("Daytime or Evening Attendance", ["Daytime", "Evening"], help="Whether the student attends classes during the day or in the evening")
    with col5:
        nationality = st.selectbox("Nationality", ["Portuguese", "German", "Spanish", "Italian", "Dutch", "English", 
            "Lithuanian", "Angolan", "Cape Verdean", "Guinean", "Mozambican", 
            "Santomean", "Turkish", "Brazilian", "Romanian", "Moldovan", "Mexican", 
            "Ukrainian", "Russian", "Cuban", "Colombian"], help="Nationality of the student")

    st.header("👪 Parents Data")
    col6, col7 = st.columns(2)
    with col6:
        mothers_qualification = st.selectbox("Mother's Qualification", [
            "Secondary Education - 12th Year of Schooling or Equivalent", 
            "Higher Education - Bachelor's Degree", "Higher Education - Degree", 
            "Higher Education - Master's", "Higher Education - Doctorate", 
            "Frequency of Higher Education", "12th Year of Schooling - Not Completed", 
            "11th Year of Schooling - Not Completed", "7th Year (Old)", 
            "Other - 11th Year of Schooling", "10th Year of Schooling", 
            "General Commerce Course", "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent", 
            "Technical-Professional Course", "7th Year of Schooling", 
            "2nd Cycle of the General High School Course", "9th Year of Schooling - Not Completed", 
            "8th Year of Schooling", "Unknown", "Can't Read or Write", 
            "Can Read without Having a 4th Year of Schooling", 
            "Basic Education 1st Cycle (4th/5th Year) or Equivalent", 
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent", 
            "Technological Specialization Course", "Higher Education - Degree (1st Cycle)", 
            "Specialized Higher Studies Course", "Professional Higher Technical Course", 
            "Higher Education - Master (2nd Cycle)", "Higher Education - Doctorate (3rd Cycle)"
        ], help="Qualification of the student's mother")
        fathers_qualification = st.selectbox("Father's Qualification", [
            "Secondary Education - 12th Year of Schooling or Equivalent", 
            "Higher Education - Bachelor's Degree", "Higher Education - Degree", 
            "Higher Education - Master's", "Higher Education - Doctorate", 
            "Frequency of Higher Education", "12th Year of Schooling - Not Completed", 
            "11th Year of Schooling - Not Completed", "7th Year (Old)", 
            "Other - 11th Year of Schooling", "10th Year of Schooling", 
            "General Commerce Course", "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent", 
            "Technical-Professional Course", "7th Year of Schooling", 
            "2nd Cycle of the General High School Course", "9th Year of Schooling - Not Completed", 
            "8th Year of Schooling", "Unknown", "Can't Read or Write", 
            "Can Read without Having a 4th Year of Schooling", 
            "Basic Education 1st Cycle (4th/5th Year) or Equivalent", 
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent", 
            "Technological Specialization Course", "Higher Education - Degree (1st Cycle)", 
            "Specialized Higher Studies Course", "Professional Higher Technical Course", 
            "Higher Education - Master (2nd Cycle)", "Higher Education - Doctorate (3rd Cycle)"
        ], help="Qualification of the student's father")
    with col7:
        mothers_occupation = st.selectbox("Mother's Occupation", [
            "Student", "Representatives of Legislative Power and Executive Bodies, Directors, Directors and Executive Managers", 
            "Specialists in Intellectual and Scientific Activities", "Intermediate Level Technicians and Professions", "Administrative staff", 
            "Personal Services, Security and Safety Workers and Sellers", "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 
            "Skilled Workers in Industry, Construction and Craftsmen", "Installation and Machine Operators and Assembly Workers", "Unskilled Workers", 
            "Armed Forces Professions", "Other Situation", "Health professionals", "Teachers", 
            "Specialists in Information and Communication Technologies (ICT)", "Intermediate Level Science and Engineering Technicians and Professions", 
            "Technicians and Professionals, Intermediate Level of Health", "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services", 
            "Office Workers, Secretaries in General and Data Processing Operators", "Data, Accounting, Statistical, Financial Services and Registry-Related Operators", 
            "Other Administrative Support Staff", "Personal Service Workers", "Sellers", "Personal Care Workers and the Like", 
            "Skilled Construction Workers and the Like, Except Electricians", "Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like", 
            "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts", "Cleaning Workers", 
            "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry", "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport", 
            "Meal Preparation Assistants"
        ], help="Occupation of the student's mother")
        fathers_occupation = st.selectbox("Father's Occupation", [
            "Student", "Representatives of Legislative Power and Executive Bodies, Directors, Directors and Executive Managers", 
            "Specialists in Intellectual and Scientific Activities", "Intermediate Level Technicians and Professions", "Administrative staff", 
            "Personal Services, Security and Safety Workers and Sellers", "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 
            "Skilled Workers in Industry, Construction and Craftsmen", "Installation and Machine Operators and Assembly Workers", "Unskilled Workers", 
            "Armed Forces Professions", "Other Situation", "Health professionals", "Teachers", 
            "Specialists in Information and Communication Technologies (ICT)", "Intermediate Level Science and Engineering Technicians and Professions", 
            "Technicians and Professionals, Intermediate Level of Health", "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services", 
            "Office Workers, Secretaries in General and Data Processing Operators", "Data, Accounting, Statistical, Financial Services and Registry-Related Operators", 
            "Other Administrative Support Staff", "Personal Service Workers", "Sellers", "Personal Care Workers and the Like", 
            "Skilled Construction Workers and the Like, Except Electricians", "Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like", 
            "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts", "Cleaning Workers", 
            "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry", "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport", 
            "Meal Preparation Assistants"
        ], help="Occupation of the student's father")

    st.header("📚 Academic Data")
    col8, col9 = st.columns(2)
    with col8:
        st.subheader("Semester 1")
        curricular_credited_1st = st.number_input("Units Credited", 0, 20, 0, help="Number of units credited in the first semester")
        curricular_enrolled_1st = st.number_input("Units Enrolled", 1, 20, 6, help="Number of units enrolled in the first semester")
        curricular_evaluated_1st = st.number_input("Units Evaluated", 0, 20, 5, help="Number of units evaluated in the first semester")
        curricular_approved_1st = st.number_input("Units Approved", 0, 20, 4, help="Number of units approved in the first semester")
        curricular_grade_1st = st.slider("Grade", 0, 20, 10, help="Grade obtained in the first semester")
    with col9:
        st.subheader("Semester 2")
        curricular_credited_2nd = st.number_input("Units Credited", 0, 20, 0, key="cred2", help="Number of units credited in the second semester")
        curricular_enrolled_2nd = st.number_input("Units Enrolled", 0, 20, 6, key="enr2", help="Number of units enrolled in the second semester")
        curricular_evaluated_2nd = st.number_input("Units Evaluated", 0, 20, 5, key="eval2", help="Number of units evaluated in the second semester")
        curricular_approved_2nd = st.number_input("Units Approved", 0, 20, 4, key="app2", help="Number of units approved in the second semester")
        curricular_grade_2nd = st.slider("Grade", 0, 20, 10, key="grade2", help="Grade obtained in the second semester")      

    st.header("🔖 Status and Conditions")
    tuition_up_to_date = st.selectbox("Tuition Fees Up-to-date", ["No", "Yes"], help="Whether the student's tuition fees are up to date")
    debtor = st.selectbox("Debtor", ["No", "Yes"], help="Is the student a debtor?")
    special_needs = st.selectbox("Special Needs", ["No", "Yes"], help="Does the student have any special educational needs?")

    submitted = st.form_submit_button("🔍 Predict Dropout")

if submitted:

    gender_map = {"Female": 0, "Male": 1}
    yes_no_map = {"No": 0, "Yes": 1}

    marital_map = {
        "Single": 1, 
        "Married": 2, 
        "Widower": 3, 
        "Divorced": 4, 
        "Facto Union": 5, 
        "Legally Separated": 6
    }

    application_mode_map = {
        "1st phase - general contingent": 1, 
        "Ordinance No. 612/93": 2, 
        "1st phase - special contingent (Azores Island)": 5, 
        "Holders of other higher courses": 7, 
        "Ordinance No. 854-B/99": 10, 
        "International student (bachelor)": 15, 
        "1st phase - special contingent (Madeira Island)": 16, 
        "2nd phase - general contingent": 17, 
        "3rd phase - general contingent": 18, 
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26, 
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27, 
        "Over 23 years old": 39, 
        "Transfer": 42, 
        "Change of course": 43, 
        "Technological specialization diploma holders": 44, 
        "Change of institution/course": 51, 
        "Short cycle diploma holders": 53, 
        "Change of institution/course (International)": 57
    }

    course_map = {
        "Biofuel Production Technologies": 33,
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014,
        "Agronomy": 9003,
        "Communication Design": 9070,
        "Veterinary Nursing": 9085,
        "Informatics Engineering": 9119,
        "Equinculture": 9130,
        "Management": 9147,
        "Social Service": 9238,
        "Tourism": 9254,
        "Nursing": 9500,
        "Oral Hygiene": 9556,
        "Advertising and Marketing Management": 9670,
        "Journalism and Communication": 9773,
        "Basic Education": 9853,
        "Management (evening attendance)": 9991
    }

    attendance_map = {
        "Daytime": 1, 
        "Evening": 0
    }

    previous_qualification_map = {
        "Secondary Education": 1, 
        "Higher Education - Bachelor's Degree": 2, 
        "Higher Education - Degree": 3, 
        "Higher Education - Master's": 4, 
        "Higher Education - Doctorate": 5, 
        "Frequency of Higher Education": 6, 
        "12th Year of Schooling - Not Completed": 9, 
        "11th Year of Schooling - Not Completed": 10, 
        "Other - 11th Year of Schooling": 12, 
        "10th Year of Schooling": 14, 
        "10th Year of Schooling - Not Completed": 15, 
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent": 19, 
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent": 38, 
        "Technological Specialization Course": 39, 
        "Higher Education - Degree (1st Cycle)": 40, 
        "Professional Higher Technical Course": 42, 
        "Higher Education - Master (2nd Cycle)": 43
    }

    nationality_map = {
        "Portuguese": 1, 
        "German": 2, 
        "Spanish": 6, 
        "Italian": 11, 
        "Dutch": 13, 
        "English": 14, 
        "Lithuanian": 17, 
        "Angolan": 21, 
        "Cape Verdean": 22, 
        "Guinean": 24, 
        "Mozambican": 25, 
        "Santomean": 26, 
        "Turkish": 32, 
        "Brazilian": 41, 
        "Romanian": 62, 
        "Moldovan": 100, 
        "Mexican": 101, 
        "Ukrainian": 103, 
        "Russian": 105, 
        "Cuban": 108, 
        "Colombian": 109
    }

    mothers_qualification_map = {
        "Secondary Education - 12th Year of Schooling or Equivalent": 1, 
        "Higher Education - Bachelor's Degree": 2, 
        "Higher Education - Degree": 3, 
        "Higher Education - Master's": 4, 
        "Higher Education - Doctorate": 5, 
        "Frequency of Higher Education": 6, 
        "12th Year of Schooling - Not Completed": 9, 
        "11th Year of Schooling - Not Completed": 10, 
        "7th Year (Old)": 11, 
        "Other - 11th Year of Schooling": 12, 
        "10th Year of Schooling": 14, 
        "General Commerce Course": 18, 
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent": 19, 
        "Technical-Professional Course": 22, 
        "7th Year of Schooling": 26, 
        "2nd Cycle of the General High School Course": 27, 
        "9th Year of Schooling - Not Completed": 29, 
        "8th Year of Schooling": 30, 
        "Unknown": 34, 
        "Can't Read or Write": 35, 
        "Can Read without Having a 4th Year of Schooling": 36, 
        "Basic Education 1st Cycle (4th/5th Year) or Equivalent": 37, 
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent": 38, 
        "Technological Specialization Course": 39, 
        "Higher Education - Degree (1st Cycle)": 40, 
        "Specialized Higher Studies Course": 41, 
        "Professional Higher Technical Course": 42, 
        "Higher Education - Master (2nd Cycle)": 43, 
        "Higher Education - Doctorate (3rd Cycle)": 44
    }

    fathers_qualification_map = {
        "Secondary Education - 12th Year of Schooling or Equivalent": 1, 
        "Higher Education - Bachelor's Degree": 2, 
        "Higher Education - Degree": 3, 
        "Higher Education - Master's": 4, 
        "Higher Education - Doctorate": 5, 
        "Frequency of Higher Education": 6, 
        "12th Year of Schooling - Not Completed": 9, 
        "11th Year of Schooling - Not Completed": 10, 
        "7th Year (Old)": 11, 
        "Other - 11th Year of Schooling": 12, 
        "2nd Year Complementary High School Course": 13, 
        "10th Year of Schooling": 14, 
        "General Commerce Course": 18, 
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent": 19, 
        "Complementary High School Course": 20, 
        "Technical-Professional Course": 22, 
        "7th Year of Schooling": 26, 
        "2nd Cycle of the General High School Course": 27, 
        "9th Year of Schooling - Not Completed": 29, 
        "8th Year of Schooling": 30, 
        "General Course of Administration and Commerce": 31, 
        "Supplementary Accounting and Administration": 33, 
        "Supplementary High School Course": 34, 
        "Unskilled Workers": 35, 
        "Market-Oriented Farmers": 36, 
        "Technological Specialization Course": 39, 
        "Higher Education - Degree (1st Cycle)": 40, 
        "Specialized Higher Studies Course": 41, 
        "Professional Higher Technical Course": 42, 
        "Higher Education - Master (2nd Cycle)": 43, 
        "Higher Education - Doctorate (3rd Cycle)": 44
    }

    mothers_occupation_map = {
        "Student": 0, 
        "Representatives of Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1, 
        "Specialists in Intellectual and Scientific Activities": 2, 
        "Intermediate Level Technicians and Professions": 3, 
        "Administrative staff": 4, 
        "Personal Services, Security and Safety Workers and Sellers": 5, 
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6, 
        "Skilled Workers in Industry, Construction and Craftsmen": 7, 
        "Installation and Machine Operators and Assembly Workers": 8, 
        "Unskilled Workers": 9, 
        "Armed Forces Professions": 10, 
        "Other Situation": 90, 
        "Health professionals": 122, 
        "Teachers": 123, 
        "Specialists in Information and Communication Technologies (ICT)": 125, 
        "Intermediate Level Science and Engineering Technicians and Professions": 131, 
        "Technicians and Professionals, Intermediate Level of Health": 132, 
        "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services": 134, 
        "Office Workers, Secretaries in General and Data Processing Operators": 141, 
        "Data, Accounting, Statistical, Financial Services and Registry-Related Operators": 143, 
        "Other Administrative Support Staff": 144, 
        "Personal Service Workers": 151, 
        "Sellers": 152, 
        "Personal Care Workers and the Like": 153, 
        "Skilled Construction Workers and the Like, Except Electricians": 171, 
        "Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like": 173, 
        "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts": 175, 
        "Cleaning Workers": 191, 
        "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry": 192, 
        "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport": 193, 
        "Meal Preparation Assistants": 194
    }

    fathers_occupation_map = {
        "Student": 0, 
        "Representatives of Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1, 
        "Specialists in Intellectual and Scientific Activities": 2, 
        "Intermediate Level Technicians and Professions": 3, 
        "Administrative staff": 4, 
        "Personal Services, Security and Safety Workers and Sellers": 5, 
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6, 
        "Skilled Workers in Industry, Construction and Craftsmen": 7, 
        "Installation and Machine Operators and Assembly Workers": 8, 
        "Unskilled Workers": 9, 
        "Armed Forces Professions": 10, 
        "Other Situation": 90, 
        "Health professionals": 122, 
        "Teachers": 123, 
        "Specialists in Information and Communication Technologies (ICT)": 125, 
        "Intermediate Level Science and Engineering Technicians and Professions": 131, 
        "Technicians and Professionals, Intermediate Level of Health": 132, 
        "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services": 134, 
        "Office Workers, Secretaries in General and Data Processing Operators": 141, 
        "Data, Accounting, Statistical, Financial Services and Registry-Related Operators": 143, 
        "Other Administrative Support Staff": 144, 
        "Personal Service Workers": 151, 
        "Sellers": 152, 
        "Personal Care Workers and the Like": 153, 
        "Skilled Construction Workers and the Like, Except Electricians": 171, 
        "Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like": 173, 
        "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts": 175, 
        "Cleaning Workers": 191, 
        "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry": 192, 
        "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport": 193, 
        "Meal Preparation Assistants": 194
    }

    # Encode input data
    input_data = pd.DataFrame([{
        "Gender": gender_map[gender],
        "Age_at_enrollment": age,
        "Marital_status": marital_map[marital_status],
        "Displaced": yes_no_map[displaced],
        "Scholarship_holder": yes_no_map[scholarship],
        "International": yes_no_map[international],
        "Application_mode": application_mode_map[application_mode],
        "Application_order": application_order,
        "Course": course_map[course],
        "Previous_qualification": previous_qualification_map[previous_qualification],
        "Previous_qualification_grade": prev_qual_grade,
        "Admission_grade": admission_grade,

        # New personal data
        "Daytime_evening_attendance": attendance_map[daytime_evening_attendance],
        "Nacionality": nationality_map[nationality],

        # Parents data
        "Mothers_qualification": mothers_qualification_map[mothers_qualification],
        "Fathers_qualification": fathers_qualification_map[fathers_qualification],
        "Mothers_occupation": mothers_occupation_map[mothers_occupation],
        "Fathers_occupation": fathers_occupation_map[fathers_occupation],

        "Curricular_units_1st_sem_credited": curricular_credited_1st,
        "Curricular_units_1st_sem_enrolled": curricular_enrolled_1st,
        "Curricular_units_1st_sem_evaluations": curricular_evaluated_1st,
        "Curricular_units_1st_sem_approved": curricular_approved_1st,
        "Curricular_units_1st_sem_grade": curricular_grade_1st,
        "Curricular_units_2nd_sem_credited": curricular_credited_2nd,
        "Curricular_units_2nd_sem_enrolled": curricular_enrolled_2nd,
        "Curricular_units_2nd_sem_evaluations": curricular_evaluated_2nd,
        "Curricular_units_2nd_sem_approved": curricular_approved_2nd,
        "Curricular_units_2nd_sem_grade": curricular_grade_2nd,

        "Tuition_fees_up_to_date": yes_no_map[tuition_up_to_date],
        "Debtor": yes_no_map[debtor],
        "Educational_special_needs": yes_no_map[special_needs],

        # Derived
        "Curricular_units_1st_sem_without_evaluations": curricular_enrolled_1st - curricular_evaluated_1st,
        "Curricular_units_2nd_sem_without_evaluations": curricular_enrolled_2nd - curricular_evaluated_2nd,
        "Unemployment_rate": 0.05,
        "Inflation_rate": 0.02,
        "GDP": 1.0
    }])

    # Derived features
    input_data['Academic_consistency'] = abs(input_data['Curricular_units_1st_sem_grade'] - input_data['Curricular_units_2nd_sem_grade'])
    input_data['Total_failed_units'] = (input_data['Curricular_units_1st_sem_enrolled'] - input_data['Curricular_units_1st_sem_approved']) + \
                                      (input_data['Curricular_units_2nd_sem_enrolled'] - input_data['Curricular_units_2nd_sem_approved'])
    input_data['Total_evaluations'] = input_data['Curricular_units_1st_sem_evaluations'] + input_data['Curricular_units_2nd_sem_evaluations']

    # Adjust columns according to model
    input_data = input_data[model_columns]

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This student is **potentially at risk of dropout**. Probability: {proba:.2%}")
    else:
        st.success(f"✅ This student is **not at risk of dropout**. Dropout probability: {proba:.2%}")
