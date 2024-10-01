import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
from random import *
df=pd.read_excel('list.xlsx')
st.title('天命人挑选系统')
st.write('欢迎使用天命人挑选系统！')
pf=pd.DataFrame(df,index=range(1,len(df)),columns=['姓名','学号','班级'])
sider_change=pd.DataFrame({'姓名':[st.sidebar.text_input('要加入的人的姓名')],'学号':[st.sidebar.text_input('要加入的人的学号')],'班级':[st.sidebar.text_input('要加入的人的班级')]})
if st.sidebar.button('加入or删除') :
    if sider_change['学号'].values not in pf['学号'].values:
        pf=pd.concat([pf,sider_change],ignore_index=True)
        st.success('成功加入！')
        pf.to_excel('list.xlsx',index=False)
    else:
        pf = pf[pf['学号'] != sider_change['学号'].values[0]]
        st.success('成功删除！')
        pf.to_excel('list.xlsx',index=False)
    
if st.button(':red[就决定是你了！]') :
    chose=pf.loc[randint(1,len(df))]
    st.write('姓名:',chose['姓名'])
    tab1,tab2=st.tabs(['班级:','学号:'])
    with tab1:
        st.header(chose['班级'])
        if st.button('删除'):
            del pf[chose['姓名']]
    with tab2:
        st.header(chose['学号'])