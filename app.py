import pickle
import numpy as np
import pandas as pd
import streamlit as st

pipe = pickle.load(open('model/pipe.pkl', 'rb'))

teams = [
 'Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka'
]

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title("Cricket Score Predictor")

col1, col2 = st.beta_columns(2)

with col1:
    batting_team = st.selectbox("Select batting team", sorted(teams))
    
with col2:
    bowling_team = st.selectbox("Select bowling team", sorted(teams))

city = st.selectbox("Select city", sorted(cities))

col3, col4, col5 = st.beta_columns(3)

with col3:
    current_score = st.number_input("Current Score")

with col4:
    overs = st.number_input("Overs done(works for over>5)")
    
with col5:
    wickets = st.number_input("Wickets out")
    
last_five = st.number_input("Runs scored in last 5 overs")

if st.button('Predict Score'):
    pass