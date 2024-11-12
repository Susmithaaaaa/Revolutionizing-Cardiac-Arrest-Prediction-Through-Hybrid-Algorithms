"""This modules contains data about home page"""
# Import necessary modules
import streamlit as st
def app():
    """This function create the home page"""    
    # Add title to the home page
    st.title("Cardiac Arrest Prediction")
    # Add image to the home page
    st.image("./images/home.png")
    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
    A heart attack, or myocardial infarction, is a serious health condition that occurs when the blood flow to a part of the heart muscle is blocked, causing damage to the heart tissue. 
    It is not classified as a disease, but rather a phenomenon of sudden cardiac arrest, which can occur due to a variety of factors, including high cholesterol, poor diet, and lack of physical activity. 
    Prevention is key, and maintaining a healthy lifestyle with a balanced diet rich in low-cholesterol foods, regular exercise, and avoiding smoking can significantly reduce the risk of heart attack. 
    This web app aims to assist in predicting the likelihood of a person experiencing a heart attack by analyzing various factors that contribute to heart health. It leverages a Decision Tree Classifier to process and evaluate the input data, such as age, cholesterol levels, blood pressure, and other health indicators. 
    By using this model, the app can determine whether a person is at risk of a cardiac arrest event in the near future. 
    Early detection and intervention are crucial in managing heart health, and the goal of this app is to provide valuable insights and empower individuals to make informed decisions about their lifestyle choices. 
    Ultimately, it serves as a preventive tool, enabling users to take proactive steps toward reducing their risk of a heart attack.        
    </p>
    """, unsafe_allow_html=True)