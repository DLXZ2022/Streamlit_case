import streamlit as st
sidebar_title = st.sidebar.title("Navigation")
sidebar_slider = st.sidebar.slider("Select a value", 0, 100, 50)
st.title("Welcome to Streamlit")
st.write("The value you selected is:", sidebar_slider)