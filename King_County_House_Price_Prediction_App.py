import pandas as pd
import numpy as np
#import seaborn as sns
import joblib
from joblib import dump,load
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
import streamlit as st
import pickle
#import matplotlib.pyplot as plt 
#%matplotlib inline
#import os

#Read the file and save as data frame
data = pd.read_csv('kc_house_data.csv')

#Log Transformation of Price column to remove right skewness and become normally distributed. Done to remove effect of outliers.
data['log_price'] = np.log(data.price)

#Remove features that are not required for training
data = data.drop(['id','date','zipcode','sqft_above','sqft_lot15','sqft_living15','price'],axis=1)

#data.yr_built = data.yr_built.astype(str)
#data.yr_renovated = data.yr_renovated.astype(str)
total_data = data.copy()

#Train Test Split
X = data.drop(['log_price'],axis=1)
y = data['log_price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)


scaler = MinMaxScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

st.sidebar.header('Specify Input Parameters - these will determine the predicted value.')

def features_from_user():
    bedrooms = st.sidebar.slider('Bedrooms', float(total_data.bedrooms.min()), float(total_data.bedrooms.max()),         float(total_data.bedrooms.mean()))
    bathrooms = st.sidebar.slider('Bathrooms', float(total_data.bathrooms.min()), float(total_data.bathrooms.max()), float(total_data.bathrooms.mean()))
    sqft_living = st.sidebar.slider('Size in sqft', float(total_data.sqft_living.min()), float(total_data.sqft_living.max()), float(total_data.sqft_living.mean()))
    sqft_lot = st.sidebar.slider('Lot Size', float(total_data.sqft_lot.min()), float(total_data.sqft_lot.max()), float(total_data.sqft_lot.mean()))
    floors = st.sidebar.slider('Number of floors', float(total_data.floors.min()), float(total_data.floors.max()), float(total_data.floors.mean()))
    waterfront = st.sidebar.slider('Waterfront', float(total_data.waterfront.min()), float(total_data.waterfront.max()), float(total_data.waterfront.mean()))
    view = st.sidebar.slider('View', float(total_data.view.min()), float(total_data.view.max()), float(total_data.view.mean())) 
    condition = st.sidebar.slider('Condition', float(total_data.condition.min()), float(total_data.condition.max()), float(total_data.condition.mean()))
    grade = st.sidebar.slider('Grade', float(total_data.grade.min()), float(total_data.grade.max()), float(total_data.grade.mean()))
    sqft_basement = st.sidebar.slider('Basement size in sqft', float(total_data.sqft_basement.min()), float(total_data.sqft_basement.max()), float(total_data.sqft_basement.mean()))
    yr_built = st.sidebar.slider('Year Built', float(total_data.yr_built.min()), float(total_data.yr_built.max()), float(total_data.yr_built.mean()))
    yr_renovated = st.sidebar.slider('Year Renovated', float(total_data.yr_renovated.min()), float(total_data.yr_renovated.max()), float(total_data.yr_renovated.mean()))
    lat = st.sidebar.slider('Latitude', float(total_data.lat.min()), float(total_data.lat.max()), float(total_data.lat.mean()))
    long = st.sidebar.slider('Longitude', float(total_data.long.min()), float(total_data.long.max()), float(total_data.long.mean()))
    
    

    user_data = {'Bedrooms':bedrooms,'Bathrooms':bathrooms,'Size in sqft':sqft_living,'Lot Size':sqft_lot,
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

#joblib.dump(GB,'model.joblib')
#pickle.dump(GB,open('model.pkl','wb'))


#Loading the model

model = joblib.load('Data/model.jlib')
#model1 =pickle.load(open('Data/model.pkl','rb'))

#Prediction
prediction = int(model.predict(df))
GB_prediction = f"{prediction:,d}"



st.header('Prediction of Median House Value:')
st.write('Based on your selections, the model predicts a value of %s US Dollars.' % GB_prediction)












