import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.write('This app builds a machine learning model!')

with st.expander('Data'):
    st.write('**Raw data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
    df