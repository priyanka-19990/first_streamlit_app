import streamlit as st

st.title('My Parents New Healthy Diner')

# Add a title
st.title("My Streamlit App")

# Add text
st.write("Welcome to my Streamlit app!")

# Add an interactive widget (e.g., a slider)
slider_value = st.slider("Select a value", 0, 100)

# Display the selected value
st.write("You selected:", slider_value)
