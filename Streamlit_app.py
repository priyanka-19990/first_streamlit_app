import streamlit as st
import pandas as p
import requests as r
import snowflake.connector
from urllib.error import URLError

#import streamlit as st
# Add a title
st.title('My Parents New Healthy Diner')
# Add a header
st.header('Breakfast Favorites')
# Add a text
st.text(' 🥣 Omega 3 & Blueberry Oatmeal')
# Add a text
st.text('🥗 Kale, Spinach & Rocket Smoothie')
# Add a text
st.text('🐔 Hard-Boiled Free-Range Egg')
# Add a text
st.text('🥑🍞 Avocado Toast')
# Add a new header
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas as p
# Passing txt file in a variable
my_fruit_list = p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
st.dataframe(fruits_to_show)

#st.header("Fruityvice Fruit Advice!")
#fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
#st.write('The user entered ', fruit_choice)
#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = p.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)

except URLError as e:
  st.error()

#import requests as r
fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json()) 
#just writes the data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = p.json_normalize(fruityvice_response.json())
#output it the screen as a table
st.dataframe(fruityvice_normalized)

#don't run anything past here while we troubleshoot
st.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

fruit_choice = st.text_input('What fruit would you like to add?')
st.write('Thanks for adding ', fruit_choice)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = p.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)

except URLError as e:
  st.error()
