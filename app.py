import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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


gsheet_connector = get_connector()
gsheets_url = st.secrets["gsheets"]["public_gsheets_url"]
data = get_data(gsheet_connector, gsheets_url)
df = pd.DataFrame(data)


# overiew
st.header("Overview")
st.write(df.describe())

share_of_na = df.isna().sum().sort_values(ascending=False)/len(df)
st.write(share_of_na)


# select a column
st.header("Select a column")
col_names = list(df.columns)
col_selected = st.selectbox("Select Column", col_names, 0)





#------------------
# chart
    
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True)


















# import plotly.graph_objects as go


# fig = go.Figure(go.Bar(
#             x=[20, 14, 23],
#             y=['giraffes', 'orangutans', 'monkeys'],
#             marker_color='skyblue',
#             orientation='h'))
# st.plotly_chart(fig, use_container_width=True)

# fig2 = go.Figure(go.Bar(
#             x=coeff['Coefficient'],
#             y=coeff['attributes'],
#             marker_color='skyblue',
#             orientation='h'))
# st.plotly_chart(fig2, use_container_width=True)





