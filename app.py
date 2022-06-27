import streamlit as st
import pandas as pd
import numpy as np
import joblib
from joblib import dump,load




#Read the file and save as data frame
data = pd.read_csv('kc_house_data.csv')

#Log Transformation of Price column to remove right skewness and become normally distributed. Done to remove effect of outliers.
data['log_price'] = np.log(data.price)

#Remove features that are not required for training
data = data.drop(['id','date','zipcode','sqft_above','sqft_lot15','sqft_living15','price'],axis=1)


st.write("""
# King County House Price Prediction""")

st.write(""" """)

st.image("Data/image.jpg")

st.write(""" Pic Credits: Toa Heftiba from Unsplash """)
st.sidebar.header('Specify the parameters:')
def features_from_user():
    bedrooms = st.sidebar.slider('Bedrooms', float(data.bedrooms.min()), float(data.bedrooms.max()),float(data.bedrooms.mean()))
    bathrooms = st.sidebar.slider('Bathrooms', float(data.bathrooms.min()), float(data.bathrooms.max()), float(data.bathrooms.mean()))
    sqft_living = st.sidebar.slider('Size in sqft', float(data.sqft_living.min()), float(data.sqft_living.max()), float(data.sqft_living.mean()))
    floors = st.sidebar.slider('Number of floors', float(data.floors.min()), float(data.floors.max()), float(data.floors.mean()))
    waterfront = st.sidebar.radio('Waterfront Property',[1,0])
    view = st.sidebar.slider('View of the Property', int(data.view.min()), int(data.view.max()), int(data.view.mean())) 
    condition = st.sidebar.slider('Condition of the property', int(data.condition.min()), int(data.condition.max()), int(data.condition.mean()))
    grade = st.sidebar.slider('Grade', int(data.grade.min()), int(data.grade.max()), int(data.grade.mean()))
    sqft_basement = st.sidebar.slider('Basement size in sqft', float(data.sqft_basement.min()), float(data.sqft_basement.max()), float(data.sqft_basement.mean()))
    yr_built = st.sidebar.slider('Year Built', int(data.yr_built.min()), int(data.yr_built.max()), int(data.yr_built.mean()))
    yr_renovated = st.sidebar.slider('Year Renovated',1910,2015)
    lat = st.sidebar.slider('Latitude', float(data.lat.min()), float(data.lat.max()), float(data.lat.mean()))
    long = st.sidebar.slider('Longitude', float(data.long.min()), float(data.long.max()), float(data.long.mean()))

    user_data = {'Bedrooms':bedrooms,'Bathrooms':bathrooms,'Size in sqft':sqft_living,
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



#Gradient Boost Model

#GB = GradientBoostingRegressor(learning_rate = 0.02, subsample = 0.5, n_estimators = 1500, max_depth = 6)
#GB.fit(X_train,y_train)

#Saving the model

#joblib.dump(GB,'model.joblib')


#Loading the model

model = joblib.load('Data/model.jlib')

#Prediction
submit = st.button("Submit")
if submit:
    st.success("Prediction Done")
    prediction = int(model.predict(df))
    GB_prediction = f"{prediction:,d}"
    st.write('Based on your selections, the model predicts a value of %s US Dollars.' % GB_prediction)
        






