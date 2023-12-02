# BASIC WIDGETS 
# (https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets)
# (https://docs.streamlit.io/library/api-reference/widgets)
# INPUT WIDGETS
import pandas as pd
import datetime
import streamlit as st

# 1: Text Input
name = st.text_input(label='Nam alengkap', value='')
st.write('Nama: ', name)


# 2: Text Area Input
text = st.text_area('Feedback')
st.write('Feedback: ', text)


# 3: Number Input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')


# 4: Date Input
date = st.date_input(label='Tanggal lahir',
                     min_value=datetime.date(1900, 1, 1))
st.write('Tanggal Lahir:', date)


# 5: File uploader
uploaded_file = st.file_uploader('Choose a CSV file')
# st.dataframe(df) --->df error gk tau knp :(


# 6: Camera Input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


# 7: Button
if st.button('Say hello'):
    st.write('Hello there')


# 8: Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp gais heheheh')


# 9: Radio Button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)


# 10: SelectBox / Dropdown
option = st.selectbox(
    label='How would you like to be contacted?',
    options=('Email', 'Home phone', 'Mobile phone')
)


# 11: MultiSelect
genre = st.multiselect(
    label='What are your favorite genres',
    options=('Comedy', 'Drama', 'Documentary')
)


# 12: Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
