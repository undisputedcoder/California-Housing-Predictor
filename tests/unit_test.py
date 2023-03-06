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
ocean_proximity = '<1H OCEAN'

df = pd.DataFrame(data, index = [0])

def test_transform_data():
    transformed_df = transform_data(df, ocean_proximity)
    expected_df = np.array([[-0.86028485,-0.70313058,-0.74322639,2.20674713,0.06558675,0.83991562,-0.00965168,-0.795956,1.,0.,0.,0.,0.]])
    np.testing.assert_almost_equal(transformed_df, expected_df)