import streamlit as st
from streamlit import button

import streamlit as st

gif_url = "https://www.icegif.com/wp-content/uploads/aesthetic-icegif-17.gif"

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("{gif_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ Aesthetic GIF Background Example")
st.write("Your Streamlit app now has a GIF background 💜")

st.title("HELLO")
n=st.text_input('enter the name')
a=st.number_input("Enter the age")
button=st.button('Click here')

if button:
    st.success(f"Congradulations {n}")
    st.toast('hello')

# from streamlit_extras.let_it_rain import rain
# import streamlit as st
#
# st.title("Emoji Rain Demo")
#
# rain(
#     emoji="💖",
#     font_size=54,
#     falling_speed=5,
#     animation_length="infinite"
# )
from streamlit_extras.colored_header import colored_header



