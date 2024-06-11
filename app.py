import streamlit as st
import pandas as pd
import tensorflow as tf

url = "https://github.com/mandar-rane/Customer-Churn-Analysis-and-Prediction-using-ML"


st.title("Customer Churn Prediction 📈")
st.text("- Mandar Rane")
st.write("GitHub: (%s)" % url)
col1, col2, col3 = st.columns(3)

with col1:
    seniorCitizenOption = st.selectbox("Senior Citizen", ("No", "Yes"))
    monthlyCharges = st.number_input(label="Monthly Charges", min_value=0, max_value=20000)
    totalCharges = st.number_input(label="Total Charges", min_value=0, max_value=20000)
    tenure = st.number_input(label="Tenure", min_value=0, max_value=100)
    genderOption = st.selectbox("Gender", ("Male", "Female"))
    multipleLinesOption = st.selectbox("Multiple Lines", ("No", "Yes", "No phone service"))
    streamingTVOption = st.selectbox("Streaming TV", ("No", "Yes", "No internet service"))
with col2:
    tenureGroupOption = st.selectbox("Tenure Group", ("1 - 12", "13 - 24", "25 - 36","37 - 48", "49 - 60", "61 - 72"))
    contractOption = st.selectbox("Contract Type", ("One Year", "Two Year", "Month-to-Month"))
    internetServiceOption = st.selectbox("Internet Service", ("DSL", "Fiber Optic", "No"))
    onlineSecurityOption = st.selectbox("Online Security", ("No", "Yes", "No internet service"))
    deviceProtectionOption = st.selectbox("Device Protection", ("No", "Yes", "No internet service"))
    techSupportOption = st.selectbox("Tech Support", ("No", "Yes", "No internet service"))
    streamingMoviesOption = st.selectbox("Streaming Movies", ("No", "Yes", "No internet service"))
with col3:
    onlineBackupOption = st.selectbox("Online Backup", ("No", "Yes", "No internet service"))
    PaperlessBillingOption = st.selectbox("Paperless Billing", ("No", "Yes"))
    partnerOption = st.selectbox("Partner Option", ("No", "Yes"))
    dependentsOption = st.selectbox("Dependents", ("No", "Yes"))
    phoneServiceOption = st.selectbox("Phone Service", ("No", "Yes"))
    paymentMethodOption= st.selectbox("Payment Method", ("Electronic Check", "Mailed Check", "Bank transfer (automatic)", "Credit card (automatic)"))
    
input_data = {
    "SeniorCitizen": 0,
    "MonthlyCharges": 0,
    "TotalCharges": 0,
    "gender_Female": 0,
    "gender_Male": 0,
    "Partner_No": 0,
    "Partner_Yes": 0,
    "Dependents_No": 0,
    "Dependents_Yes": 0,
    "PhoneService_No": 0,
    "PhoneService_Yes": 0,
    "MultipleLines_No": 0,
    "MultipleLines_No phone service": 0,
    "MultipleLines_Yes": 0,
    "InternetService_DSL": 0,
    "InternetService_Fiber optic": 0,
    "InternetService_No": 0,
    "OnlineSecurity_No": 0,
    "OnlineSecurity_No internet service": 0,
    "OnlineSecurity_Yes": 0,
    "OnlineBackup_No": 0,
    "OnlineBackup_No internet service": 0,
    "OnlineBackup_Yes": 0,
    "DeviceProtection_No": 0,
    "DeviceProtection_No internet service": 0,
    "DeviceProtection_Yes": 0,
    "TechSupport_No": 0,
    "TechSupport_No internet service": 0,
    "TechSupport_Yes": 0,
    "StreamingTV_No": 0,
    "StreamingTV_No internet service": 0,
    "StreamingTV_Yes": 0,
    "StreamingMovies_No": 0,
    "StreamingMovies_No internet service": 0,
    "StreamingMovies_Yes": 0,
    "Contract_Month-to-month": 0,
    "Contract_One year": 0,
    "Contract_Two year": 0,
    "PaperlessBilling_No": 0,
    "PaperlessBilling_Yes": 0,
    "PaymentMethod_Bank transfer (automatic)": 0,
    "PaymentMethod_Credit card (automatic)": 0,
    "PaymentMethod_Electronic check": 0,
    "PaymentMethod_Mailed check": 0,
    "tenure_group_1 - 12": 0,
    "tenure_group_13 - 24": 0,
    "tenure_group_25 - 36": 0,
    "tenure_group_37 - 48": 0,
    "tenure_group_49 - 60": 0,
    "tenure_group_61 - 72": 0
}

input_data['SeniorCitizen'] = 1 if seniorCitizenOption == "Yes" else 0
input_data['MonthlyCharges'] = monthlyCharges
input_data['TotalCharges'] = totalCharges
input_data['gender_Female'] = 1 if genderOption == "Female" else 0
input_data['gender_Male'] = 1 if genderOption == "Male" else 0
input_data['Partner_No'] = 1 if partnerOption == "No" else 0
input_data['Partner_Yes'] = 1 if partnerOption == "Yes" else 0
input_data['Dependents_No'] = 1 if dependentsOption == "No" else 0
input_data['Dependents_Yes'] = 1 if dependentsOption == "Yes" else 0
input_data['PhoneService_No'] = 1 if phoneServiceOption == "No" else 0
input_data['PhoneService_Yes'] = 1 if phoneServiceOption == "Yes" else 0
input_data['PaperlessBilling_No'] = 1 if PaperlessBillingOption == "No" else 0
input_data['PaperlessBilling_Yes'] = 1 if PaperlessBillingOption == "Yes" else 0

if multipleLinesOption == "No":
    input_data['MultipleLines_No'] = 1.0
    input_data['MultipleLines_No phone service']= 0.0
    input_data['MultipleLines_Yes'] = 0.0
elif multipleLinesOption == "No phone service":
    input_data['MultipleLines_No'] = 0.0
    input_data['MultipleLines_No phone service'] = 1.0
    input_data['MultipleLines_Yes'] = 0.0
elif multipleLinesOption == "Yes":
    input_data['MultipleLines_No'] = 0.0
    input_data['MultipleLines_No phone service'] = 0.0
    input_data['MultipleLines_Yes'] = 1.0

if internetServiceOption == "DSL":
    input_data['InternetService_DSL'] = 1.0
    input_data['InternetService_Fiber optic']= 0.0
    input_data['InternetService_No']= 0.0
elif internetServiceOption == "Fiber Optic":
    input_data['InternetService_DSL']= 0.0
    input_data['InternetService_Fiber optic'] = 1.0
    input_data['InternetService_No']= 0.0
elif internetServiceOption == "No":
    input_data['InternetService_DSL'] = 0.0
    input_data['InternetService_Fiber optic'] = 0.0
    input_data['InternetService_No']= 1.0

if onlineSecurityOption == "No":
    input_data['OnlineSecurity_No'] = 1.0
    input_data['OnlineSecurity_No internet service'] = 0.0
    input_data['OnlineSecurity_Yes'] = 0.0
elif onlineSecurityOption == "No internet service":
    input_data['OnlineSecurity_No'] = 0.0
    input_data['OnlineSecurity_No internet service']= 1.0
    input_data['OnlineSecurity_Yes'] = 0.0
elif onlineSecurityOption == "Yes":
    input_data['OnlineSecurity_No'] = 0.0
    input_data['OnlineSecurity_No internet service']= 0.0
    input_data['OnlineSecurity_Yes']= 1.0

if onlineBackupOption == "No":
    input_data['OnlineBackup_No'] = 1.0
    input_data['OnlineBackup_No internet service']= 0.0
    input_data['OnlineBackup_Yes']= 0.0
elif onlineBackupOption == "No internet service":
    input_data['OnlineBackup_No']= 0.0
    input_data['OnlineBackup_No internet service'] = 1.0
    input_data['OnlineBackup_Yes']= 0.0
elif onlineBackupOption == "Yes":
    input_data['OnlineBackup_No']= 0.0
    input_data['OnlineBackup_No internet service'] = 0.0
    input_data['OnlineBackup_Yes']= 1.0 

if deviceProtectionOption == "No":
    input_data['DeviceProtection_No']= 1.0
    input_data['DeviceProtection_No internet service']= 0.0
    input_data['DeviceProtection_Yes'] = 0.0
elif deviceProtectionOption == "No internet service":
    input_data['DeviceProtection_No'] = 0.0
    input_data['DeviceProtection_No internet service']= 1.0
    input_data['DeviceProtection_Yes'] = 0.0
elif deviceProtectionOption == "Yes":
    input_data['DeviceProtection_No']= 0.0
    input_data['DeviceProtection_No internet service']= 0.0
    input_data['DeviceProtection_Yes']= 1.0

if techSupportOption == "No":
    input_data['TechSupport_No']= 1.0
    input_data['TechSupport_No internet service']= 0.0
    input_data['TechSupport_Yes'] = 0.0
elif techSupportOption == "No internet service":
    input_data['TechSupport_No'] = 0.0
    input_data['TechSupport_No internet service']= 1.0
    input_data['TechSupport_Yes']= 0.0
elif techSupportOption == "Yes":
    input_data['TechSupport_No']= 0.0
    input_data['TechSupport_No internet service']= 0.0
    input_data['TechSupport_Yes'] = 1.0

if streamingTVOption == "No":
    input_data['StreamingTV_No']= 1.0
    input_data['StreamingTV_No internet service']= 0.0
    input_data['StreamingTV_Yes'] = 0.0
elif streamingTVOption == "No internet service":
    input_data['StreamingTV_No']= 0.0
    input_data['StreamingTV_No internet service']= 1.0
    input_data['StreamingTV_Yes'] = 0.0
elif streamingTVOption == "Yes":
    input_data['StreamingTV_No'] = 0.0
    input_data['StreamingTV_No internet service']= 0. 
    input_data['StreamingTV_Yes']= 1.0

if streamingMoviesOption == "No":
    input_data['StreamingMovies_No'] = 1.0
    input_data['StreamingMovies_No internet service']= 0.0
    input_data['StreamingMovies_Yes'] = 0.0
elif streamingMoviesOption == "No internet service":
    input_data['StreamingMovies_No'] = 0.0
    input_data['StreamingMovies_No internet service']= 1.0
    input_data['StreamingMovies_Yes']= 0.0
elif streamingMoviesOption == "Yes":
    input_data['StreamingMovies_No']= 0.0
    input_data['StreamingMovies_No internet service'] = 0.0
    input_data['StreamingMovies_Yes']= 1.0

if contractOption == "Month-to-Month":
    input_data['Contract_Month-to-month']= 1.0
    input_data['Contract_One year'] = 0.0
    input_data['Contract_Two year']= 0.0
elif contractOption == "One Year":
    input_data['Contract_Month-to-month']= 0.0
    input_data['Contract_One year'] = 1.0
    input_data['Contract_Two year']= 0.0
elif contractOption == "Two Year":
    input_data['Contract_Month-to-month'] = 0.0
    input_data['Contract_One year'] = 0.0
    input_data['Contract_Two year']= 1.0

if paymentMethodOption == "Bank transfer (automatic)":
    input_data['PaymentMethod_Bank transfer (automatic)'] = 1.0
    input_data['PaymentMethod_Credit card (automatic)']= 0.0
    input_data['PaymentMethod_Electronic check'] = 0.0
    input_data['PaymentMethod_Mailed check']= 0.0
elif paymentMethodOption == "Credit card (automatic)":
    input_data['PaymentMethod_Bank transfer (automatic)']= 0.0
    input_data['PaymentMethod_Credit card (automatic)']= 1.0
    input_data['PaymentMethod_Electronic check'] = 0.0
    input_data['PaymentMethod_Mailed check'] = 0.0
elif paymentMethodOption == "Electronic check":
    input_data['PaymentMethod_Bank transfer (automatic)'] = 0.0
    input_data['PaymentMethod_Credit card (automatic)']= 0.0
    input_data['PaymentMethod_Electronic check'] = 1.0
    input_data['PaymentMethod_Mailed check'] = 0.0
elif paymentMethodOption == "Mailed check":
    input_data['PaymentMethod_Bank transfer (automatic)']= 0.0
    input_data['PaymentMethod_Credit card (automatic)']= 0.0
    input_data['PaymentMethod_Electronic check']= 0.0
    input_data['PaymentMethod_Mailed check']= 1.0

if tenureGroupOption == "1 - 12":
    input_data['tenure_group_1 - 12'] = 1.0
    input_data['tenure_group_13 - 24'] = 0.0
    input_data['tenure_group_25 - 36'] = 0.0
    input_data['tenure_group_37 - 48'] = 0.0
    input_data['tenure_group_49 - 60'] = 0.0
    input_data['tenure_group_61 - 72'] = 0.0
elif tenureGroupOption == "13 - 24":
    input_data['tenure_group_1 - 12'] = 0.0
    input_data['tenure_group_13 - 24'] = 1.0
    input_data['tenure_group_25 - 36'] = 0.0
    input_data['tenure_group_37 - 48'] = 0.0
    input_data['tenure_group_49 - 60'] = 0.0
    input_data['tenure_group_61 - 72'] = 0.0
elif tenureGroupOption == "25 - 36":
    input_data['tenure_group_1 - 12'] = 0.0
    input_data['tenure_group_13 - 24'] = 0.0
    input_data['tenure_group_25 - 36'] = 1.0
    input_data['tenure_group_37 - 48'] = 0.0
    input_data['tenure_group_49 - 60'] = 0.0
    input_data['tenure_group_61 - 72'] = 0.0
elif tenureGroupOption == "37 - 48":
    input_data['tenure_group_1 - 12'] = 0.0
    input_data['tenure_group_13 - 24'] = 0.0
    input_data['tenure_group_25 - 36'] = 0.0
    input_data['tenure_group_37 - 48'] = 1.0
    input_data['tenure_group_49 - 60'] = 0.0
    input_data['tenure_group_61 - 72'] = 0.0
elif tenureGroupOption == "61 - 36":
    input_data['tenure_group_1 - 12'] = 0.0
    input_data['tenure_group_13 - 24'] = 0.0
    input_data['tenure_group_25 - 36'] = 0.0
    input_data['tenure_group_37 - 48'] = 0.0
    input_data['tenure_group_49 - 60'] = 0.0
    input_data['tenure_group_61 - 72'] = 1.0

input_df = pd.DataFrame([input_data])

model_path = "neuralnet_model.h5"
model = tf.keras.models.load_model(model_path)

def predictChurn():
    with col3:
        prediction = model.predict(input_df)  
        if round(prediction[0][0]) == 0:
            st.write("Churn Prediction: No")
        else:
            st.write("Churn Prediction: Yes")           
        st.write("Probabilty: ",prediction[0][0])


st.button("PREDICT", on_click=predictChurn)






