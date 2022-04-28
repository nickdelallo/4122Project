#!/usr/bin/env python
# coding: utf-8

# In[3]:


# imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data

# data
def load_data():
    df = pd.read_csv('Netflix.csv', index_col = 'Country_code')
    return df

# title
st.title('Netflix Data')

# load
df = load_data()

# columns
cols = df.columns
col1, col2= st.columns(2)

# objective
if st.sidebar.checkbox('Objective'):
    st.title("Optimal price based on library size")
    st.write(df)

# library size
if st.sidebar.checkbox('Library Size'):
    
    # movies
    movies = df.sort_values(['No. of Movies'], ascending=False)
    movies = pd.concat([movies.head(10),movies.tail(10)]).sort_index()
    moviesChart = alt.Chart(movies).mark_bar().encode(
    x=alt.X('Movies:Q', title='Movies'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Movies:Q')
    ).properties(width=350)
    with col1:
        st.write(moviesChart)
    
    # tv shows
    tvshows = df.sort_values(['No. of TV Shows'], ascending=False)
    tvshows = pd.concat([tvshows.head(10),tvshows.tail(10)]).sort_index()
    tvshowsChart = alt.Chart(tvshows).mark_bar().encode(
    x=alt.X('TV_Shows:Q', title='TV Shows'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('TV_Shows:Q')
    ).properties(width=350)
    with col2:
        st.write(tvshowsChart)
    
    # total
    totalLibrary = df.sort_values(['Total Library Size'], ascending=False)
    totalLibrary = pd.concat([totalLibrary.head(10),totalLibrary.tail(10)]).sort_index()
    totalLibraryChart = alt.Chart(totalLibrary).mark_bar().encode(
    x=alt.X('Total_Library_Size:Q', title='Total Library Size'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Total_Library_Size:Q')
    ).properties(width=600)
    with col1:
        st.write(totalLibraryChart)

# cost
if st.sidebar.checkbox('Cost'):
    
    # basic
    basicCost = df.sort_values(['Cost Per Month - Basic ($)'], ascending=False)
    basicCost = pd.concat([basicCost.head(10),basicCost.tail(10)]).sort_index()
    basicCostChart = alt.Chart(basicCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Basic:Q', title='Basic Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Basic:Q')
    ).properties(width=350)
    with col1:
        st.write(basicCostChart)
        
    # standard
    standardCost = df.sort_values(['Cost Per Month - Standard ($)'], ascending=False)
    standardCost = pd.concat([standardCost.head(10),standardCost.tail(10)]).sort_index()
    standardCostChart = alt.Chart(standardCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Standard:Q', title='Standard Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Standard:Q')
    ).properties(width=350)
    with col2:
        st.write(standardCostChart)
      
    # premium
    premiumCost = df.sort_values(['Cost Per Month - Premium ($)'], ascending=False)
    premiumCost = pd.concat([premiumCost.head(10),premiumCost.tail(10)]).sort_index()
    premiumCostChart = alt.Chart(premiumCost).mark_bar().encode(
    x=alt.X('Cost_Per_Month_Premium:Q', title='Premium Cost'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('Cost_Per_Month_Premium:Q')
    ).properties(width=350)
    with col1:
        st.write(premiumCostChart)
        
    with col2:
        st.write('Basic: Not HD and only one screen')
        st.write('Standard: HD and 2 screens')
        st.write('Premium: Ultra HD and 4 screens')

# findings
if st.sidebar.checkbox('Findings'):
    
    # basic
    basicCostPerDollar = df
    basicCostPerDollar['result'] = basicCostPerDollar['Total Library Size']/basicCostPerDollar['Cost Per Month - Basic ($)']
    basicCostPerDollar = basicCostPerDollar.sort_values(['result'], ascending=False)
    basicCostPerDollar = pd.concat([basicCostPerDollar.head(10),basicCostPerDollar.tail(10)]).sort_index()
    basicCostPerDollarChart = alt.Chart(basicCostPerDollar).mark_bar().encode(
    x=alt.X('result:Q', title='Basic Cost Per $'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('result:Q')
    ).properties(width=350)
    with col1:
        st.write(basicCostPerDollarChart)
    
    # standard
    standardCostPerDollar = df
    standardCostPerDollar['result'] = standardCostPerDollar['Total Library Size']/standardCostPerDollar['Cost Per Month - Standard ($)']
    standardCostPerDollar = standardCostPerDollar.sort_values(['result'], ascending=False)
    standardCostPerDollar = pd.concat([standardCostPerDollar.head(10),standardCostPerDollar.tail(10)]).sort_index()
    standardCostPerDollarChart = alt.Chart(standardCostPerDollar).mark_bar().encode(
    x=alt.X('result:Q', title='Standard Cost Per $'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('result:Q')
    ).properties(width=350)
    with col2:
        st.write(standardCostPerDollarChart)
        
    # premium
    premiumCostPerDollar = df
    premiumCostPerDollar['result'] = premiumCostPerDollar['Total Library Size']/premiumCostPerDollar['Cost Per Month - Premium ($)']
    premiumCostPerDollar = premiumCostPerDollar.sort_values(['result'], ascending=False)
    premiumCostPerDollar = pd.concat([premiumCostPerDollar.head(10),premiumCostPerDollar.tail(10)]).sort_index()
    premiumCostPerDollarChart = alt.Chart(premiumCostPerDollar).mark_bar().encode(
    x=alt.X('result:Q', title='Premium Cost Per $'),
    y=alt.Y('Country:N', sort='-x', title='Country'),
    color=alt.Color('result:Q')
    ).properties(width=350)
    with col1:
        st.write(premiumCostPerDollarChart)
        
    with col2:
        st.write('Basic Mean: ' + str(round(basicCostPerDollar['result'].mean(), 2)))
        st.write('Standard Mean: ' + str(round(standardCostPerDollar['result'].mean(), 2)))
        st.write('Premium Mean: ' + str(round(premiumCostPerDollar['result'].mean(), 2)))
if st.sidebar.checkbox('Solution'):
    st.write(df)


# In[ ]:




