import streamlit as st
import pandas as pd

st.set_page_config(page_title = 'Uploade your Dataset')

df = st.file_uploader(label = 'Please load a csv dataset:')

if df :
     df = pd.read_csv(df)
     st.write(df.head())

