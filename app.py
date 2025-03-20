import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("🚀 My First Streamlit App")
st.write("Welcome to my interactive Streamlit app!")

# Text Input
name = st.text_input("Enter your name:", "Shreya")

# Button Interaction
if st.button("Say Hello"):
    st.write(f"Hello, {name}! 🎉")

# Number Input
age = st.number_input("Enter your age:", min_value=1, max_value=100, value=21)

# Select Box
favorite_color = st.selectbox("Pick your favorite color:", ["Red", "Blue", "Green", "Yellow"])

# Display Selections
st.write(f"Your favorite color is {favorite_color} and you are {age} years old!")

# Display a Random Chart
st.write("📊 Random Data Visualization:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)
