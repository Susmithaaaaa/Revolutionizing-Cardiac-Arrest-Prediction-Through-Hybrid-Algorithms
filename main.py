"""This is the main module to run the app"""
# Importing the necessary Python modules.
import streamlit as st
from web_functions import load_data
from Tabs import data, home, predict, visualise
# Configure the app
st.set_page_config(
    page_title = 'Cardiac Disease Prediction',
    page_icon = '🫀',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)
# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise,
}
# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")
# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))
# Loading the dataset.
df, X, y = load_data()
# Run the app function of the selected page
if page in ["Prediction", "Visualisation"]:
    # Ensure the selected page's module has an 'app' function that accepts three arguments
    if hasattr(Tabs[page], 'app'):
        Tabs[page].app(df, X, y)
    else:
        st.error(f"The selected page '{page}' does not have a valid 'app' function.")        
elif page == "Data Info":
    # Ensure the 'Data Info' page's module has an 'app' function that accepts one argument
    if hasattr(Tabs[page], 'app'):
        Tabs[page].app(df)
    else:
        st.error(f"The selected page '{page}' does not have a valid 'app' function.")        
else:
    # For pages like 'Home', no arguments are passed to the 'app' function
    if hasattr(Tabs[page], 'app'):
        Tabs[page].app()
    else:
        st.error(f"The selected page '{page}' does not have a valid 'app' function.")