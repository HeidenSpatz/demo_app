import streamlit as st
import numpy as np
import pandas as pd

from gsheetsdb import connect



#------------------
# config
st.set_page_config(page_title='my app',
                    #page_icon=":shark:",
                    layout='wide')
                    #menu_items: Get help, Report a Bug, About



st.title("a simple demo app")



# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")








