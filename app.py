
import streamlit as st
import numpy as np
import pandas as pd
import geemap.foliumap as geemap

#OpenStreetMap API for geocoding
import geopy
from geopy.geocoders import Nominatim 
#To avoid time out in API
from geopy.extra.rate_limiter import RateLimiter

#------------------
# config
st.set_page_config(page_title='Demo App - Bachelor',
                    #page_icon=":shark:",
                    layout='wide')
                    #menu_items: Get help, Report a Bug, About



#------------------
# functions

@st.cache
def read_csv(path):
    return pd.read_csv(path)





#------------------
#get data
df = read_csv("~/code/data_app/immo3.csv")
coeff = read_csv("~/code/data_app/coefficient.csv")



#------------------
#title
st.title("Demo App - Geo Exploration")
st.dataframe(coeff)
st.button("Re-run")


#------------------
# side bar
#st.sidebar.radio("Choose a feature", 'app 1', 'app 2', 'app 3'))




#------------------
# get input
st.header("please enter address and parameters")
# street, housenumber, city, zip code
col1, col2, col3, col4 = st.columns([4, 1, 3, 2])

with col1:
    street = col1.text_input('Street')

with col2:
    housenr = col2.text_input('House Nr.')

with col3:
    zip = st.text_input('Zip Code')
    
with col4:
    city = st.text_input('City')

st.write('address: ', street, " ", housenr, ", ", zip, " ", city)

# square meter, balcony etc.
col5, col6, col7 = st.columns([3, 2, 1])

with col5:
    livingSpace = st.slider("Living Space - Square meter", 
                            max_value=150, 
                            value = 75)
with col6:
    floor = st.number_input("Floor", 
                            min_value=-1, 
                            max_value=30, 
                            value=0)

with col7:
    balcony = st.checkbox("Balcony")
    hasKitchen = st.checkbox("Kitchen")
    lift = st.checkbox("Lift")




#------------------
# chart
    
# import plotly.figure_factory as ff

# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#          hist_data, group_labels, bin_size=[.1, .25, .5])

# st.plotly_chart(fig, use_container_width=True)
    
import plotly.graph_objects as go


fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            marker_color='skyblue',
            orientation='h'))
st.plotly_chart(fig, use_container_width=True)

fig2 = go.Figure(go.Bar(
            x=coeff['Coefficient'],
            y=coeff['attributes'],
            marker_color='skyblue',
            orientation='h'))
st.plotly_chart(fig2, use_container_width=True)




#------------------
# standard streamlit map
# df = pd.DataFrame(data = {'lat': [50.126, 50.13],
#                             'lon': [8.707, 8.8]})
# st.map(df, zoom=12)


#------------------
# geemap
m = geemap.Map(center=[50.130, 8.692], zoom=16)


geolocator = Nominatim(user_agent="my_user_agent")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)

address = street + " " + housenr + ", " + city + " " + zip

if len(address) > 5:
    
    location = geolocator.geocode(address)

    lat = location.latitude
    lon = location.longitude

    st.write(location.address)
    st.write(lat, lon)
    #st.write(f"Lat, Lon: {lat}, {lon}")
    #st.write(location.raw)
    popup = f"lat, lon: {lat}, {lon}"
    
    m.add_marker(location=(lat, lon), popup=popup)
    m.setCenter(lon=lon,lat=lat, zoom=16)
    m.to_streamlit(height=600)
else:
    m.to_streamlit(height=600)