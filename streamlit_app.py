# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rS6TU7q1lYG3zxpszetQBeEvEHMgYq-6
"""

import streamlit as st
st.write('Find Largest of 3 number')
a=st.number_input('insert 1st integer number')
b=st.number_input('insert 2nd integer number')
c=st.number_input('insert 3rd integer number')
if (a>b and a>c):
  st.write("1st number is largest")

if (b>a and b>c):
  st.write("2nd number is largest")

if (c>b and c>a):
  st.write("3rd number is largest")