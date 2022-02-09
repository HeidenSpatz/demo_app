import streamlit as st
import numpy as np
import pandas as pd
from gsheetsdb import connect



#------------------
# config
st.set_page_config(page_title='Data Exploration',
                    #page_icon=":shark:",
                    layout='wide')
                    #menu_items: Get help, Report a Bug, About



st.title("Data Exploration - ImmoScout")



# Share the connector across all users connected to the app
@st.experimental_singleton()
def get_connector():
    return connect()

# Time to live: the maximum number of seconds to keep an entry in the cache
TTL = 24 * 60 * 60

# Using `experimental_memo()` to memoize function executions
@st.experimental_memo(ttl=TTL)
def query_to_dataframe(_connector, query: str) -> pd.DataFrame:
    rows = _connector.execute(query, headers=1)
    dataframe = pd.DataFrame(list(rows))
    return dataframe

@st.experimental_memo(ttl=600)
def get_data(_connector, gsheets_url) -> pd.DataFrame:
    return query_to_dataframe(_connector, f'SELECT * FROM "{gsheets_url}"')

st.markdown(f"## 📝 Connecting to a public Google Sheet")

gsheet_connector = get_connector()
gsheets_url = st.secrets["gsheets"]["public_gsheets_url"]

data = get_data(gsheet_connector, gsheets_url)

df = pd.DataFrame(data)

st.write(df.describe())


col_names = list(df.columns)



col_selected = st.selectbox("Select Column", col_names, 0)

st.write(col_selected)








