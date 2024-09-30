import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
from random import *
df=pd.read_excel('list.xlsx')
st.title('天命人挑选系统')
st.write('欢迎使用天命人挑选系统！')
if st.button('就决定是你了！') :
    pf=pd.DataFrame(df,index=range(1,len(df)))
    chose=df.loc[randint(1,len(df))]
  
    st.write({'姓名':chose['姓名'],'学号':chose['学号'],'班级':chose['班级']})