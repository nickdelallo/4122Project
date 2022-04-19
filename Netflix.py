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
# Columns
col1, col2= st.columns(2)
#option = st.multiselect('What sources do you want to display?', cols, cols[0])
    
if st.sidebar.checkbox('Objective'):
    st.title("Optimal price based on library size")
    st.write(df)
    
if st.sidebar.checkbox('Data'):
    totalLibrary = df.sort_values(['Total_Library_Size'], ascending=False)
    totalLibrary = pd.concat([totalLibrary.head(10),totalLibrary.tail(10)]).sort_index()
    totalLibraryChart = alt.Chart(totalLibrary).mark_bar().encode(
    x=alt.X('Total_Library_Size:Q', title='Total Library Size'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Total_Library_Size:Q')
    ).properties(width=600)
    st.write(totalLibraryChart)
        
    movies = df.sort_values(['Movies'], ascending=False)
    movies = pd.concat([movies.head(10),movies.tail(10)]).sort_index()
    moviesChart = alt.Chart(movies).mark_bar().encode(
    x=alt.X('Movies:Q', title='Movies'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Movies:Q')
    ).properties(width=350)
    with col1:
        st.write(moviesChart)
        
    tvshows = df.sort_values(['TV_Shows'], ascending=False)
    tvshows = pd.concat([tvshows.head(10),tvshows.tail(10)]).sort_index()
    tvshowsChart = alt.Chart(tvshows).mark_bar().encode(
    x=alt.X('TV_Shows:Q', title='TV Shows'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('TV_Shows:Q')
    ).properties(width=350)
    with col2:
        st.write(tvshowsChart)

if st.sidebar.checkbox('Findings'):
    st.write(df)
    
if st.sidebar.checkbox('Solution'):
    st.write(df)