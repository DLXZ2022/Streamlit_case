import streamlit as st
sidebar_title = st.sidebar.title("Navigation")
sidebar_slider = st.sidebar.slider("请选择一个数值", 0, 100, 50)
sidebar_pic=st.sidebar.image("https://pixnio.com/zh/media/zh-3162592",width=50)
st.title("欢迎来到AlphaYin的空间")
st.write("你导入的数值是:", sidebar_slider)