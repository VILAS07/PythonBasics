import streamlit as st
from streamlit import button

st.title('Demo title')
name=st.text_input('ENTER YOUR NAME')
age=int(st.number_input('ENTER THE NUMBER'))
gender=st.selectbox('gender',['Male','Female'])
button=st.button('click')

if button:
    st.success(f"hello {name} how are you.You are {age} years old")
    st.balloons()