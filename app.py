import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO



#------------------
# config
st.set_page_config(page_title='my app',
                    #page_icon=":shark:",
                    layout='wide')
                    #menu_items: Get help, Report a Bug, About



st.title("a simple demo app")

df = pd.DataFrame()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    # todo: if not csv

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

    #data overview
    st.header("Overview")
    st.write("rows: ", df.shape[0], "cols: ", df.shape[1])
    st.write(df.columns)


    #show available columns
    st.subheader("Column names")
    column_names = ""
    for column in pd.Series(df.columns):
        column_names = column_names + ", " + column

    st.write(column_names)




