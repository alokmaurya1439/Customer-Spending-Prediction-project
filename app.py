import pickle

import streamlit as st
import pandas as pd



#load the model (model deserialization)
with open("best_model/best_model_pipeline.pkl","rb") as file:
    best_pipeline = pickle.load(file)

st.set_page_config(page_title="Customer Spending Prediction",page_icon="assets/Spend_analytics.png")

with st.sidebar:
    st.title("Customer Spending Prediction")
    st.image("assets/logo.png")

#load the dataset
df = pd.read_csv("dataset/cleaned_spending_data.csv")



col1, col2 = st.columns(2,border=True)
with col1:
    Age=st.slider("Age",min_value=1,max_value=100,value=1)
    Annual_Income=st.number_input("Annual Income",min_value=1000,max_value=10000000,step=5000)
    Website_Visits=st.number_input("Website Visits",min_value=0,max_value=100,step=2)
    Previous_Purchases=st.number_input("Previous Purchases",min_value=0,max_value=100,step=1)

with col2:
    Membership_Type=st.selectbox("Membership Type", options=df['Membership_Type'].unique())
    Preferred_Category=st.selectbox("Preferred Category", options=df['Preferred_Category'].unique())
    City_Tier=st.selectbox("City Tier", options=df['City_Tier'].unique())
    Discount_Used=st.selectbox("Discount Used", options=df['Discount_Used'].unique())

st.header("Prediction Spending...")

if st.button("Check Spending Amount"):
    missing_value=[
        Age,Annual_Income,Website_Visits,Previous_Purchases,Membership_Type,Preferred_Category,City_Tier,Discount_Used
    ]

    if any(value is None for value in missing_value):
        st.error("Please fill in all the required fields.")

    else:
        input_data= pd.DataFrame({
            'Age':[Age],
            'Annual_Income':[Annual_Income],
            'Website_Visits':[Website_Visits],
            'Previous_Purchases':[Previous_Purchases],
            'Membership_Type':[Membership_Type],
            'Preferred_Category':[Preferred_Category],
            'City_Tier':[City_Tier],
            'Discount_Used':[Discount_Used]
        })

        prediction=best_pipeline.predict(input_data)
        st.success("Predicted Spending Amount: {:.2f}".format(prediction[0]))