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

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    # todo: if not csv

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write("row, cols: ", dataframe.shape)