import streamlit as st
from PIL import Image
image = Image.open('Ms.jpg')
sidebar_title = st.sidebar.title("Navigation")
sidebar_slider = st.sidebar.slider("请选择一个数值", 0, 100, 50)
st.write("你导入的数值是:", sidebar_slider)
st.image(image, caption='孟子饭')
