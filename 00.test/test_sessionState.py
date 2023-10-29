import streamlit as st

text = "🤷‍♂️"

print(st.session_state)

if "click" not in st.session_state:
    st.session_state.click=False
else:
    if st.session_state.click == False:
        text = "💕"
        st.session_state.click = True 
    else:
        text = "🤷‍♂️"
        st.session_state.click = False 


btn = st.button(text)


