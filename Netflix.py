import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data

def load_data():
    df = pd.read_csv('Netflix.csv', index_col = 'Country_code')
    return df

st.title('Netflix Data')

df = load_data()

cols = df.columns
option = st.multiselect('What sources do you want to display?', cols, cols[0])

if st.sidebar.checkbox('Data'):
    st.write(df)