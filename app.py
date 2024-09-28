import streamlit as st
from PIL import Image
image = Image.open('pic1.jpg')
image1 = Image.open('pic2.jpg')
st.title("梦子梵大帅哥")
st.image(image, caption='孟子饭')
st.image(image1, caption='石头')