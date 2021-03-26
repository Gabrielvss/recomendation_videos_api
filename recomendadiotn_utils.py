import pandas as pd
import re
import joblib as jb
from scipy.sparse import hstack, csr_matrix
import numpy as np 
import json
import os






mdl_logr = jb.load("logisticRegression.pkl.z")
mdl_lgbm = jb.load("lgbm.pkl.z")
title_vec = jb.load("title_vectorizer.pkl.z")

def compute_features(data):

    publish_date = pd.to_datetime(data['upload_date'])
   
    views = data['view_count']
    title = data['title']

    features = dict()

    features['tempo_desde_pub'] = (pd.Timestamp.today() - publish_date) / np.timedelta64(1, 'D')
    features['views'] = views
    features['views_por_dia'] = features['views'] / features['tempo_desde_pub']
    del features['tempo_desde_pub']

    vectorized_title = title_vec.transform([title])

    num_features = csr_matrix(np.array([features['views'], features['views_por_dia']]))
    feature_array = hstack([num_features, vectorized_title])

    return feature_array    

def compute_prediction(data):
    feature_array = compute_features(data)

    if feature_array is None:
        return 0


    p_logr = mdl_logr.predict_proba(feature_array)[0][1]
    p_lgbm = mdl_lgbm.predict_proba(feature_array)[0][1]

    p = 0.3*p_logr + 0.7*p_lgbm
    #log_data(data, feature_array, p)

    return p  

def log_data(data, feature_array, p):

    #print(data)
    video_id = data.get('og:video:url', '')
    data['prediction'] = p
    data['feature_array'] = feature_array.todense().tolist()
    #print(video_id, json.dumps(data))       