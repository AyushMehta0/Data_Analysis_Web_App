# -*- coding: utf-8 -*-
#imports 
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns

st.title("Data Analysis")
st.subheader("Data analysis using Python and Streamlit")

upload = st.file_uploader("Upload Your Dataset (In CSV Format)")

if upload is not None:
    data = pd.read_csv(upload)

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

if upload is not None:
    if st.checkbox("Datatype of Each Column"):
        st.text("Datatypes")
        st.text(data.dtypes)


if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?",('Rows',
                                                                'Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

import matplotlib.pyplot as plt

#6. Find Null Values in The Dataset
if upload is not None:
    has_null_values = data.isnull().values.any()

    if st.checkbox("Show Heatmap of Missing Values"):
      # Allow users to select columns (optional)
      selected_columns = st.multiselect("Select Columns", data.columns)
      if not selected_columns:
        selected_columns = data.columns  # Use all columns if none selected
      null_heatmap_data = data[selected_columns].isnull()
    
      if has_null_values:
        # Generate and display heatmap
        fig, ax = plt.subplots()  
        sns.heatmap(null_heatmap_data, ax=ax)
        st.pyplot(fig)
      else:
        st.write("No missing values found!")
            

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))



if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")


if st.checkbox("By"):
    st.success("Ayush Mehta")        
    
