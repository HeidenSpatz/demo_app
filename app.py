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

#get data
df = pd.read_csv("immo.csv.zip")

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






