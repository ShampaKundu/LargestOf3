import streamlit as st
st.write('Find Largest of 3 number')
a=int(input())
b=int(input())
c=int(input())
if (a>b and a>c):
  st.write("a is largest")

if (b>a and b>c):
  st.write("b is largest")

if (c>b and c>a):
  st.write("c is largest")
