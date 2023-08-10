import streamlit as st
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

import pandas as p
# Passing txt file in a variable
my_fruit_list = p.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
# Let's put a pick list here so they can pick the fruit they want to include
st.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page
st.dataframe(my_fruit_list)
