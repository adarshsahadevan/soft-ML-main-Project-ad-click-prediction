# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 02:02:27 2024

@author: ACER
"""

import pickle
import streamlit as st
import pandas as pd



# Load the saved model
ad_predict_model = pickle.load(open('https://raw.githubusercontent.com/adarshsahadevan/ML-Project-ad-/main/ad_predict.sav'))


# Load the dataframe (assuming it's a CSV file)
df1 = pd.read_csv('https://raw.githubusercontent.com/adarshsahadevan/ML-Project-ad-/main/advertising.csv')

st.title('Ad_Predict using ML')

AdTopicLine = st.text_input('Enter Ad Topic Line')

# Define the retrieve_ad_info function
def retrieve_ad_info(Ad_Topic_Line):
    try:
        ad_row = df1.loc[df1['Ad Topic Line'] == Ad_Topic_Line].iloc[0]
        relevant_info = {
            'Clicked on Ad': ad_row['Clicked on Ad'],
            'Daily Time Spent on Site': ad_row['Daily Time Spent on Site'],
            'Age': ad_row['Age'],
            'Daily Internet Usage' : ad_row['Daily Internet Usage'],
            'Male' : ad_row['Male'],
            'City' : ad_row['City'],
            'Country' : ad_row['Country'],
            'Timestamp' : ad_row['Timestamp']
        }
        return relevant_info
    except IndexError:
        return None

# Create a button for prediction
if st.button('Ad - Clicked or Not'):
    input_ad_topic = AdTopicLine
    retrieved_info = retrieve_ad_info(input_ad_topic)
    if retrieved_info:
        st.write(f"Ad Topic: {input_ad_topic}")
        st.write('\n')
        st.write(f"CLICKED ON AD: {'Yes' if retrieved_info['Clicked on Ad'] else 'No'}")
        st.write('\n')
        st.write("DETAILS : ")
        st.write(f"Daily Time Spent on site: {retrieved_info['Daily Time Spent on Site']} minutes")
        st.write(f"Age: {retrieved_info['Age']} years")
        st.write(f"Daily Internet Usage: {retrieved_info['Daily Internet Usage']} GB")
        st.write(f"City: {retrieved_info['City']}")
        st.write(f"Gender: {'Male' if retrieved_info['Male'] else 'Female'}")
        st.write(f"Country: {retrieved_info['Country']}")
        st.write(f"Date & Time: {retrieved_info['Timestamp']}")
       
        
    else:
        st.write(f"Ad topic '{input_ad_topic}' not found in the dataset.")
