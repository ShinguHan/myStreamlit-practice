import streamlit as st
import time

@st.cache_data
def printa():
    st.write("Running....")
    time.sleep(3)
    return "Keep Going"

st.write(printa())