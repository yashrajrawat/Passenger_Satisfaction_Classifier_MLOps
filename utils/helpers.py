
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encode(df , columns):
    le = LabelEncoder()
    label_mappings = {}

    for col in columns:
        df[col] = le.fit_transform(df[col])
        label_mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))
        
    return df,label_mappings