import streamlit as st
from PIL import Image
image = Image.open('pic1.jpg')
image1 = Image.open('pic2.jpg')
st.title("作者：梦子梵大帅哥")
st.image(image)
st.image(image1)