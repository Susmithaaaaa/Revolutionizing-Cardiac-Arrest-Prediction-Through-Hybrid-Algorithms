"""This modules contains data about prediction page"""
# Import necessary modules
import streamlit as st
# Import necessary functions from web_functions
from web_functions import predict
def app(df, X, y):
    """This function create the prediction page"""
    # Add title to the page
    st.title("Prediction Page")
    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Cardiac Disease Prediction.
            </p>
        """, unsafe_allow_html=True)    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")
    # Take input of features from the user.
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))    
    gen = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    hr = st.slider("HR", int(df["HR"].min()), int(df["HR"].max()))    
    maxhr = st.slider("MaxHR", int(df["MaxHR"].min()), int(df["MaxHR"].max()))    
    dbp = st.slider("Diastolic_BP", float(df["Diastolic_BP"].min()), float(df["Diastolic_BP"].max()))    
    sbp = st.slider("Systolic_BP", float(df["Systolic_BP"].min()), float(df["Systolic_BP"].max()))    
    bs = st.slider("BS", float(df["BS"].min()), float(df["BS"].max()))    
    dia = st.slider("Diabetes", int(df["Diabetes"].min()), int(df["Diabetes"].max()))    
    resrate = st.slider("Respiratory_Rate",int(df["Respiratory_Rate"].min()),int(df["Respiratory_Rate"].max()))    
    bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))    
    obs = st.slider("Obesity", int(df["Obesity"].min()), int(df["Obesity"].max()))
    die = st.slider("Diet", int(df["Diet"].min()), int(df["Diet"].max()))     
    stress = st.slider("Stress_Level", int(df["Stress_Level"].min()), int(df["Stress_Level"].max()))    
    alc = st.slider("Alcohol_Consumption", int(df["Alcohol_Consumption"].min()), int(df["Alcohol_Consumption"].max()))    
    smoke = st.slider("Smoking", int(df["Smoking"].min()), int(df["Smoking"].max()))    
    phy = st.slider("Physical_Activity", float(df["Physical_Activity"].min()), float(df["Physical_Activity"].max()))
    sleep = st.slider("Sleep_Hours", int(df["Sleep_Hours"].min()), int(df["Sleep_Hours"].max()))    
    famHis = st.slider("Family_History", int(df["Family_History"].min()), int(df["Family_History"].max()))    
    ph = st.slider("Previous_History", int(df["Previous_History"].min()), int(df["Previous_History"].max()))
    # Create a list to store all the features
    features = [age, gen, hr, maxhr, sbp, dbp, bs, dia, resrate, bmi, obs, die, stress, alc, smoke, phy, sleep, famHis, ph]
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0
        st.info("Predicted Sucessfully...")
        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get cardiac arrest!!")
        else:
            st.success("The person is relatively safe from cardiac arrest")
        # Print the score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")

