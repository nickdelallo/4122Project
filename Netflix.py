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
    
if st.sidebar.checkbox('Library Size'):
        
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
        
    totalLibrary = df.sort_values(['Total_Library_Size'], ascending=False)
    totalLibrary = pd.concat([totalLibrary.head(10),totalLibrary.tail(10)]).sort_index()
    totalLibraryChart = alt.Chart(totalLibrary).mark_bar().encode(
    x=alt.X('Total_Library_Size:Q', title='Total Library Size'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Total_Library_Size:Q')
    ).properties(width=600)
    with col1:
        st.write(totalLibraryChart)
        
if st.sidebar.checkbox('Cost'):
    
    basicCost = df.sort_values(['Cost_Per_Month_Basic'], ascending=False)
    basicCost = pd.concat([basicCost.head(10),basicCost.tail(10)]).sort_index()
    basicCostChart = alt.Chart(basicCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Basic:Q', title='Basic Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Basic:Q')
    ).properties(width=350)
    with col1:
        st.write(basicCostChart)
        
    standardCost = df.sort_values(['Cost_Per_Month_Standard'], ascending=False)
    standardCost = pd.concat([standardCost.head(10),standardCost.tail(10)]).sort_index()
    standardCostChart = alt.Chart(standardCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Standard:Q', title='Standard Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Standard:Q')
    ).properties(width=350)
    with col2:
        st.write(standardCostChart)
        
    premiumCost = df.sort_values(['Cost_Per_Month_Premium'], ascending=False)
    premiumCost = pd.concat([premiumCost.head(10),premiumCost.tail(10)]).sort_index()
    premiumCostChart = alt.Chart(premiumCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Premium:Q', title='Premium Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Premium:Q')
    ).properties(width=350)
    with col1:
        st.write(premiumCostChart)

if st.sidebar.checkbox('Findings'):
    basicCostPerDollar = df
    basicCostPerDollar['result'] = basicCostPerDollar['Total_Library_Size']/basicCostPerDollar['Cost_Per_Month_Basic']
    basicCostPerDollar = basicCostPerDollar.sort_values(['result'], ascending=False)
    basicCostPerDollar = pd.concat([basicCostPerDollar.head(10),basicCostPerDollar.tail(10)]).sort_index()
    basicCostPerDollarChart = alt.Chart(basicCostPerDollar).mark_bar().encode(
    x=alt.X('result:Q', title='Basic Cost Per $'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('result:Q')
    ).properties(width=350)
    with col1:
        st.write(basicCostPerDollarChart)
    
if st.sidebar.checkbox('Solution'):
    st.write(df)