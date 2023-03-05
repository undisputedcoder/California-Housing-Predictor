import streamlit as st
import pandas as pd
from joblib import load

from util import transform_data
    
model = load('housing_model.pkl')

OCEAN_PROXIMITY = ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND']

ocean_proximity = ""

def input_features():
    st.sidebar.header("Enter house features")
    longitude = st.sidebar.number_input('Longitude', -125.0, -113.0, -117.24, step=0.01)
    latitude = st.sidebar.number_input('Latitude', 32.0, 42.0, 32.79, step=0.01)
    housing_median_age = st.sidebar.number_input('Housing Median Age', 1.0, 52.0, 20.0, step=1.0)
    total_rooms = st.sidebar.number_input("Total Rooms", 2.0, 39320.0, 961.0, step=1.0)
    total_bedrooms = st.sidebar.number_input("Total Bedrooms", 1.0, 6445.0, 278.0, step=1.0)
    population = st.sidebar.number_input("Population", 3.0, 35682.0, 525.0, step=1.0)
    households = st.sidebar.number_input("Households", 1.0, 6082.0, 254.0, step=1.0)
    median_income = st.sidebar.number_input("Median Income", 0.5, 15.0, 3.18, step=0.01)
    ocean_proximity = st.sidebar.selectbox("Ocean Proximity", OCEAN_PROXIMITY)

    data = {
        'Longitude': longitude,
        'Latitude': latitude,
        'Housing Median Age': housing_median_age,
        'Total Rooms': total_rooms,
        'Total Bedrooms': total_bedrooms,
        'Population': population,
        'Households': households,
        'Median Income': median_income
    }

    features = pd.DataFrame(data, index = [0])
    return features, ocean_proximity

df, ocean_proximity = input_features()

transformed_df = transform_data(df, ocean_proximity)

prediction = int(model.predict(transformed_df))
prediction_nice = f"{prediction:,d}"

st.header('California Median House Value Predictor')

st.write('Housing features entered')
st.table(df)

st.markdown('Based on your selections, the value of the house is estimated to be worth **$%s USD.**' % prediction_nice)