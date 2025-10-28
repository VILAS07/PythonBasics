import streamlit as st
from streamlit import button

st.title('Celsius to Farenheit')
c=st.number_input('Temprature in celsius : ')
button=st.button('Convert to Faherenheat')

if button:
    f=c*(9/5)+32
    st.success(f" {c} in Farenheat is : {f}")
    st.snow()