import streamlit as st
from joblib import load
import pandas as pd
from helper import df

# Function to update workclass options based on age


def update_workclass_options(age):
    return df[df['age'] == age]['workclass'].unique().tolist()

# Function to update occupation options based on age and education


def update_occupation_options(age, education, workclass):
    return df[(df['education'] == education) & (df['age'] == age) & (df['workclass'] == workclass)]['occupation'].unique().tolist()

# Function to update marital status options based on relationship


def update_marital_status_options(relationship):
    return df[df['relationship'] == relationship]['marital-status'].unique().tolist()


def predictor(input_data):
    # Load the preprocessor and classifier
    preprocessor = load('preprocessor.joblib')
    classifier = load('classifier.joblib')

    # Transform input data and make prediction
    input_df = pd.DataFrame(input_data, index=[0])
    preprocessed_data = preprocessor.transform(input_df)
    prediction = classifier.predict(preprocessed_data)

    # Display the prediction
    st.subheader("Prediction")
    if prediction[0] == 0:
        st.success("The predicted income is <= $50K.")
    else:
        st.success("The predicted income is > $50K.")


def model():
    st.title("Income Prediction App")
    st.write("Enter the required information to make a prediction.")

    # Initialize input variables
    input_data = {}

    age = st.number_input("Age", min_value=19,
                          max_value=df['age'].max(), step=1, key=f"Age")
    input_data['age'] = age

    workclass_options = update_workclass_options(input_data['age'])
    workclass = st.selectbox("Workclass", workclass_options, key=f"Workclass")
    input_data['workclass'] = workclass

    education_options = df['education'].unique()
    education = st.selectbox("Education", education_options, key=f"Education")
    input_data['education-num'] = df.loc[df['education']
                                         == education, 'education-num'].iloc[0],

    occupation_options = update_occupation_options(
        input_data['age'], education, input_data['workclass'])
    occupation = st.selectbox(
        "Occupation", occupation_options, key=f"Occupation")
    input_data['occupation'] = occupation

    sex_options = df['sex'].unique()
    sex = st.selectbox("Sex", sex_options, key=f"Sex")
    input_data['sex'] = sex

    relationship_options = df[df['sex'] ==
                              input_data['sex']]['relationship'].unique()
    relationship = st.selectbox(
        "Relationship", relationship_options, key=f"Relationship")
    input_data['relationship'] = relationship

    marital_status_options = update_marital_status_options(
        input_data['relationship'])
    marital_status = st.selectbox(
        "Marital Status", marital_status_options, key=f"Marital_Status")
    input_data['marital-status'] = marital_status

    race_options = df['race'].unique()
    race = st.selectbox("Race", race_options, key=f"Race")
    input_data['race'] = race

    hours_per_week = st.number_input("Hours per Week", min_value=df['hours-per-week'].min(
    ), max_value=df['hours-per-week'].max(), step=1, key=f"Hours_per_Week")
    input_data['hours-per-week'] = hours_per_week

    native_country_options = df['native-country'].unique().tolist()
    native_country = st.selectbox(
        "Native Country", native_country_options, key=f"Native_Country")
    input_data['native-country'] = native_country

    capital_gain = st.number_input(
        "Capital Gain", min_value=0, max_value=100000, step=100, key=f"Capital_Gain")

    capital_loss = st.number_input(
        "Capital Loss", min_value=0, max_value=100000, step=100, key=f"Capital_Loss")
    input_data['Net_Capital_Change'] = capital_gain - capital_loss

    fnlwgt = st.number_input("fnlwgt", min_value=0,
                             max_value=100000, step=100, key=f"fnlwgt")
    input_data['fnlwgt'] = fnlwgt

    if st.button("Predict"):
        predictor(input_data)
