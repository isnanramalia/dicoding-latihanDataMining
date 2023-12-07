# dashboard untuk visualisasi data bike sharing dgn streamlit

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data


@st.cache_data
def load_data():
    all_data = pd.read_csv('all_data.csv')
    return all_data


data = load_data()
sns.set(style='dark')

# Load data


@st.cache_data
def load_data():
    all_data = pd.read_csv('all_data.csv')
    return all_data


data = load_data()

# Sidebar
st.sidebar.title("Navigation")
# Add an image to the sidebar (replace with your image path)
st.sidebar.image("image.jpeg")
st.sidebar.write(
    "This is a dashboard for visualizing bike sharing data. You can select the options below to display different aspects of the data.")

option = st.sidebar.selectbox(
    'What do you want to display?',
    ('Raw data', 'Number of bikes rented on Monday', 'Number of bikes rented on Friday in summer',
     'Number of bikes rented on weekdays vs weekends', 'Day with the most rented bikes',
     'Correlation between temperature and number of rented bikes'))

if option == 'Raw data':
    st.subheader('Raw data')
    st.write(data)

elif option == 'Number of bikes rented on Monday':
    st.subheader('Number of bikes rented on Monday')
    num_bikes_monday = data[data['weekday_x'] == 1]['cnt_x'].sum()
    st.write(num_bikes_monday)

elif option == 'Number of bikes rented on Friday in summer':
    st.subheader('Number of bikes rented on Friday in summer')
    num_bikes_friday_summer = data[(data['weekday_x'] == 5) & (
        data['season_x'] == 2)]['cnt_x'].sum()
    st.write(num_bikes_friday_summer)

elif option == 'Number of bikes rented on weekdays vs weekends':
    st.subheader('Number of bikes rented on weekdays vs weekends')
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x='hr', y='cnt_x', hue='weekday_x', ax=ax)
    st.pyplot(fig)

elif option == 'Day with the most rented bikes':
    st.subheader('Day with the most rented bikes')
    most_bikes_weekday = data.groupby('weekday_x')['cnt_x'].sum().idxmax()
    st.write(most_bikes_weekday)

elif option == 'Correlation between temperature and number of rented bikes':
    st.subheader('Correlation between temperature and number of rented bikes')
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='temp_x', y='cnt_x', ax=ax)
    st.pyplot(fig)
# Title
st.title("Bike Sharing Analysis Dashboard")

# Display raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Number of bikes rented on Monday
st.subheader('Number of bikes rented on Monday')
num_bikes_monday = data[data['weekday_x'] == 1]['cnt_x'].sum()
st.write(num_bikes_monday)

# Number of bikes rented on Friday in summer
st.subheader('Number of bikes rented on Friday in summer')
num_bikes_friday_summer = data[(data['weekday_x'] == 5) & (
    data['season_x'] == 2)]['cnt_x'].sum()
st.write(num_bikes_friday_summer)

# Number of bikes rented on weekdays vs weekends
st.subheader('Number of bikes rented on weekdays vs weekends')
fig, ax = plt.subplots()
sns.lineplot(data=data, x='hr', y='cnt_x', hue='weekday_x', ax=ax)
st.pyplot(fig)

# Day with the most rented bikes
st.subheader('Day with the most rented bikes')
most_bikes_weekday = data.groupby('weekday_x')['cnt_x'].sum().idxmax()
st.write(most_bikes_weekday)

# Correlation between temperature and number of rented bikes
st.subheader('Correlation between temperature and number of rented bikes')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='temp_x', y='cnt_x', ax=ax)
st.pyplot(fig)
