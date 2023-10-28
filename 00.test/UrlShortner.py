import streamlit as st
import pyshorteners as pyst
import pyperclip as clip

shortner = pyst.Shortener()

def Copying():
    clip.copy(shortened)

btn = st.empty()

st.title("Shortner")
with st.form("name"):
    url = st.text_input("Input URL")
    btn = st.form_submit_button("Short")

if btn:
    shortened = shortner.tinyurl.short(url)
    st.write(shortened)
    st.button("Copy", on_click=Copying)


