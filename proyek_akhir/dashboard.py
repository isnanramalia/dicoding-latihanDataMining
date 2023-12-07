# dashboard untuk visualisasi data bike sharing dgn streamlit

"""
Alur Latihan:
1. Persiapan
2. Menyiapkan dataframe yg akan digunakan
3. Membuat komponen filter pd dashboard
4. Melengkapi dashboard dgn berbagai visualisasi data
"""

# TODO 1: Persiapan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# TODO 2: Menyiapkan dataframe yg akan digunakan
# membuat fungsi utk membuat dataframe yg akan digunakan dari bike sharing dataset
