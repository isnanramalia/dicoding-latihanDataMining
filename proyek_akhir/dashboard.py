# dashboard untuk visualisasi data bike sharing dgn streamlit

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# TODO 1: Load data

all_data = pd.read_csv('all_data.csv')
datetime_columns = ["dteday"]
all_data.sort_values(by="dteday", inplace=True)
all_data.reset_index(inplace=True)

for column in datetime_columns:
    all_data[column] = pd.to_datetime(all_data[column])

# TODO 2: Sidebar
# membuat komponen filder pd dahboard
min_date = all_data["dteday"].min()
max_date = all_data["dteday"].max()

with st.sidebar:
    st.title("Navigation")
    st.image("image.jpeg")
    st.write(
        "This is a dashboard for visualizing bike sharing data. You can select the range of the date.")
    start_date = pd.Timestamp(st.date_input("Start date", min_date))  # Convert to datetime
    end_date = pd.Timestamp(st.date_input("End date", max_date))  # Convert to datetime

data = all_data[(all_data['dteday'] >= start_date)
                & (all_data['dteday'] <= end_date)]

# TODO 3: Main page
st.title("Bike Sharing Data Dashboard🚴🏻")
with st.container():
    col1, col2 = st.columns(2)

    # User selects the day in the first column
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_mapping = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 0}
    selected_day = col1.selectbox('Select a day', days)

    # User selects the season in the second column
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    season_mapping = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    selected_season = col2.selectbox('Select a season', seasons)

    # Number of bikes rented on selected day
    col1.subheader(f'Number of bikes rented on {selected_day}')
    num_bikes_selected_day = data[data['weekday_x'] == day_mapping[selected_day]]['cnt_x'].sum()
    col1.write(num_bikes_selected_day)

    # Number of bikes rented on selected day in selected season
    col2.subheader(f'Number of bikes rented on {selected_day} in {selected_season}')
    num_bikes_selected_day_season = data[(data['weekday_x'] == day_mapping[selected_day]) & (data['season_x'] == season_mapping[selected_season])]['cnt_x'].sum()
    col2.write(num_bikes_selected_day_season)

# Number of bikes rented on weekdays vs weekends
st.subheader('Number of bikes rented on weekdays vs weekends')
fig, ax = plt.subplots()
sns.lineplot(data=data, x='hr', y='cnt_x', hue='weekday_x', ax=ax)
ax.set_xlabel('Hour')
ax.set_ylabel('Number of bikes rented')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""
    Plot pertama menunjukkan jumlah sepeda yang disewa setiap jam pada hari kerja dan akhir pekan. 
    Dari plot ini, kita bisa melihat bahwa ada pola tertentu dalam sewa sepeda berdasarkan waktu dan hari.
    """)

# Day with the most rented bikes
# Reverse mapping from number to day
day_mapping_reverse = {v: k for k, v in day_mapping.items()}

# Day with the most rented bikes
st.subheader('Day with the most rented bikes')
most_bikes_weekday = data.groupby('weekday_x')['cnt_x'].sum().idxmax()
most_bikes_weekday_name = day_mapping_reverse[most_bikes_weekday]  # Convert number to day name
st.write(most_bikes_weekday_name)
fig, ax = plt.subplots()

# Create a color palette with a different color for the most rented day
palette = ['b' if x != most_bikes_weekday else 'r' for x in range(7)]

sns.barplot(data=data, x='weekday_x', y='cnt_x', ax=ax, palette=palette)
ax.set_xlabel('Day')
ax.set_ylabel('Number of bikes rented')
ax.set_xticklabels([day_mapping_reverse[i] for i in range(7)])  # Set x-tick labels to day names
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""
    Plot kedua menunjukkan hari dengan jumlah sewa sepeda terbanyak. 
    Dari plot ini, kita bisa melihat bahwa hari tertentu memiliki jumlah sewa sepeda yang lebih tinggi dibandingkan hari lainnya.
    """)

# Correlation between temperature and number of rented bikes
st.subheader('Correlation between temperature and number of rented bikes')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='temp_x', y='cnt_x', ax=ax)
ax.set_xlabel('Temperature')
ax.set_ylabel('Number of bikes rented')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""
    Plot ketiga menunjukkan korelasi antara suhu dan jumlah sepeda yang disewa. 
    Dari plot ini, kita bisa melihat bahwa suhu tertentu mungkin mempengaruhi jumlah sewa sepeda.
    """)

# Distribution of the number of rented bikes
st.subheader('Distribution of the number of rented bikes')
fig, ax = plt.subplots()
sns.histplot(data=data, x='cnt_x', ax=ax)
ax.set_xlabel('Number of bikes rented')
ax.set_ylabel('Count')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""
    Plot keempat menunjukkan distribusi jumlah sepeda yang disewa. 
    Dari plot ini, kita bisa melihat bagaimana sebaran jumlah sewa sepeda dan apakah ada outlier.
    """)

# Geoanalytics
st.subheader('Geoanalytics')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='atemp_x', y='cnt_x', ax=ax)
ax.set_xlabel('Temperature')
ax.set_ylabel('Number of bikes rented')
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""
    Plot kelima menunjukkan analisis geografis dari data sewa sepeda. 
    Dari plot ini, kita bisa melihat bagaimana sebaran sewa sepeda berdasarkan suhu dan jumlah sewa.
    """)