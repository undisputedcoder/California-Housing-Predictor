from util import transform_data
import pandas as pd
import numpy as np

data = {
    'Longitude': -17.34,
    'Latitude': 32.79,
    'Housing Median Age': 20.0,
    'Total Rooms': 961.0,
    'Total Bedrooms': 278.0,
    'Population': 525.0,
    'Households': 254.0,
    'Median Income': 3.18
}
ocean_proximity = 'NEAR OCEAN'

df = pd.DataFrame(data, index = [0])

def test_transform_data():
    transformed_df = transform_data(df, ocean_proximity)
    expected_df = pd.DataFrame({
        'Longitude': -17.34,
        'Latitude': 32.79,
        'Housing Median Age': 20.0,
        'Total Rooms': 961.0,
        'Total Bedrooms': 278.0,
        'Population': 525.0,
        'Households': 254.0,
        'Median Income': 3.18,
        'inland': 0,
        'near ocean': 1,
        'near bay': 0,
        'island': 0
    }, index=[0])
    transformed_df.equals(expected_df)