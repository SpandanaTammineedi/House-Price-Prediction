import pandas as pd
import numpy as np
#import seaborn as sns
import joblib
from joblib import dump,load
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
import streamlit as st
#import matplotlib.pyplot as plt 
#%matplotlib inline
#import os

#Read the file and save as data frame
data = pd.read_csv('kc_house_data.csv')

#Log Transformation of Price column to remove right skewness and become normally distributed. Done to remove effect of outliers.
data['log_price'] = np.log(data.price)

#Remove features that are not required for training
data = data.drop(['id','date','zipcode','sqft_above','sqft_lot15','sqft_living15'],axis=1)

data.yr_built = data.yr_built.astype(str)
data.yr_renovated = data.yr_renovated.astype(str)

#Train Test Split
X = data.drop(['price','log_price'],axis=1)
y = data['log_price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)


scaler = MinMaxScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

st.sidebar.header('Specify Input Parameters - these will determine the predicted value.')

def features_from_user():
    Bedrooms = st.sidebar.slider('Bedrooms', float(full_df.Bedrooms.min()), float(full_df.Bedrooms.max()), float(full_df.Bedrooms.mean()))
    Bathrooms = st.sidebar.slider('Bathrooms', float(full_df.Bathrooms.min()), float(full_df.Bathrooms.max()), float(full_df.Bathrooms.mean()))
    sqft_living = st.sidebar.slider('Size in sqft', float(full_df.sqft_living.min()), float(full_df.sqft_living.max()), float(full_df.sqft_living.mean()))
    sqft_lot = st.sidebar.slider('Lot Size', float(full_df.sqft_lot.min()), float(full_df.sqft_lot.max()), float(full_df.sqft_lot.mean()))
    floors = st.sidebar.slider('Number of floors', float(full_df.floors.min()), float(full_df.floors.max()), float(full_df.floors.mean()))
    waterfront = st.sidebar.slider('Waterfront', float(full_df.waterfront.min()), float(full_df.waterfront.max()), float(full_df.waterfront.mean()))
    view = st.sidebar.slider('View', float(full_df.view.min()), float(full_df.view.max()), float(full_df.view.mean())) 
    condition = st.sidebar.slider('Condition', float(full_df.condition.min()), float(full_df.condition.max()), float(full_df.condition.mean()))
    grade = st.sidebar.slider('Grade', float(full_df.grade.min()), float(full_df.grade.max()), float(full_df.grade.mean()))
    sqft_basement = st.sidebar.slider('Basement size in sqft', float(full_df.sqft_basement.min()), float(full_df.sqft_basement.max()), float(full_df.sqft_basement.mean()))
    yr_built = st.sidebar.slider('Year Built', float(full_df.yr_built.min()), float(full_df.yr_built.max()), float(full_df.yr_built.mean()))
    yr_renovated = st.sidebar.slider('Year Renovated', float(full_df.yr_renovated.min()), float(full_df.yr_renovated.max()), float(full_df.yr_renovated.mean()))
    lat = st.sidebar.slider('Latitude', float(full_df.lat.min()), float(full_df.lat.max()), float(full_df.lat.mean()))
    long = st.sidebar.slider('Longitude', float(full_df.long.min()), float(full_df.long.max()), float(full_df.long.mean()))
    
    

    user_data = {'Bedrooms':Bedrooms,'Bathrooms':Bathrooms,'Size in sqft':sqft_living,'Lot Size':sqft_lot,
             'Number of floors':floors,'Waterfront':waterfront,'View':view,'Condition':condition,'Grade':grade,
            'Basement size in sqft':sqft_basement,'Year Built':yr_built,'Year Renovated':yr_renovated,'Latitude':lat,
            'Longitude':long}

    features = pd.DataFrame(user_data, index = [0])
    return features

df = features_from_user()

# Display specified input parameters
st.write('Specified Input Parameters:')
st.table(df)
st.write('---')

#X = X.drop('Unnamed: 0', axis=1)





#Gradient Boost Model

GB = GradientBoostingRegressor(learning_rate = 0.02, subsample = 0.5, n_estimators = 1500, max_depth = 6)
GB.fit(X_train,y_train)

#Saving the model
dump(GB,'model.joblib')

#Loading the model
model1 = load('data/model.joblib')

#Prediction
prediction = int(model1.predict(df))
GB_prediction = f"{prediction:,d}"



st.header('Prediction of Median House Value:')
st.write('Based on your selections, the model predicts a value of %s US Dollars.' % GB_prediction)












