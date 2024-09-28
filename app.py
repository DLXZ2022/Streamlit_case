import streamlit as st
from PIL import Image
image = Image.open('Ms.jpg')
image1 = Image.open('rock.jpg')
sidebar_title = st.sidebar.title("Navigation")
sidebar_slider = st.sidebar.slider("请选择一个数值", 0, 100, 50)
st.write("孟子饭有",sidebar_slider,"女朋友")
st.image(image, caption='孟子饭')
st.image(image1, caption='石头')