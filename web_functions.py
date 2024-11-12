from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
@st.cache_data
def load_data():
    """This function returns the preprocessed data"""
    # Load the Heart Disease dataset into DataFrame.
    df = pd.read_csv('heart_attack_prediction_dataset.csv')
    # Perform feature and target split
    X = df[["Age", "Gender", "BMI", "Systolic_BP", "Diastolic_BP", "HR", "MaxHR", "BS", "Respiratory_Rate", "Diabetes", "Obesity", "Alcohol_Consumption", "Smoking", "Diet", "Sleep_Hours", "Stress_Level", "Physical_Activity", "Family_History", "Previous_History"]]
    y = df['Heart Attack Risk']
    return df, X, y
@st.cache_data
def train_model(X, y):
    """This function trains the model and returns the model and model score"""
    # Ensure X and y are writable numpy arrays
    X = np.array(X)
    y = np.array(y)
    # Create the model
    model = DecisionTreeClassifier(
        ccp_alpha=0.0,
        class_weight=None,
        criterion='entropy',
        max_depth=4,
        max_features=None,
        max_leaf_nodes=None,
        min_impurity_decrease=0.0,
        min_samples_leaf=1,
        min_samples_split=2,
        min_weight_fraction_leaf=0.0,
        random_state=42,
        splitter='best'
    )
    # Fit the data on model
    model.fit(X, y)
    # Get the model score
    score = model.score(X, y)
    # Return the values
    return model, score
def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Ensure features is a writable numpy array
    features = np.array(features).astype(np.float64)
    # Predict the value
    prediction = model.predict(features.reshape(1, -1))
    return prediction, score