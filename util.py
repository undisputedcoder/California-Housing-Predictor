import pandas as pd

def transform_data(df, ocean_proximity):
    if ocean_proximity == "INLAND":
        cat_attribs = {
            'inland': 1,
            'near ocean': 0,
            'near by': 0,
            'island': 0
        }
    elif ocean_proximity == "NEAR OCEAN":
        cat_attribs = {
            'inland': 0,
            'near ocean': 1,
            'near by': 0,
            'island': 0
        }
    elif ocean_proximity == "NEAR BAY":
        cat_attribs = {
            'inland': 0,
            'near ocean': 0,
            'near by': 1,
            'island': 0
        }
    elif ocean_proximity == "ISLAND":
        cat_attribs = {
            'inland': 0,
            'near ocean': 0,
            'near by': 0,
            'island': 1
        }
    else:
        cat_attribs = {
            'inland': 0,
            'near ocean': 0,
            'near by': 0,
            'island': 0
        }

    cat_attributes = pd.DataFrame(data=cat_attribs, index=[0])
    merged = pd.merge(df, cat_attributes, how="outer", on=df["Median Income"])
    merged = merged.drop(['key_0'], axis="columns")
    return merged
