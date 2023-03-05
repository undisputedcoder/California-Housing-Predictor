from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

def transform_data(df, ocean_proximity):
    num_pipeline = Pipeline([
        ('std_scaler', StandardScaler())
    ])

    num_attribs = np.array(df.values.tolist()).reshape(-1,1)
    housing_num = num_pipeline.fit_transform(num_attribs)

    if ocean_proximity == "<1H OCEAN":
        cat_attribs = [1,0,0,0,0]
    elif ocean_proximity == "INLAND":
        cat_attribs = [0,1,0,0,0]
    elif ocean_proximity == "NEAR OCEAN":
        cat_attribs = [0,0,0,0,1]
    elif ocean_proximity == "NEAR BAY":
        cat_attribs = [0,0,0,1,0]
    else:
        cat_attribs = [0,0,1,0,0]

    cat_attribs = np.array([cat_attribs]).reshape(-1,1)
    
    merged = np.concatenate((housing_num, cat_attribs))

    return np.array(merged).reshape(-1,13)
