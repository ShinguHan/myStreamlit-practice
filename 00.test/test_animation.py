import streamlit as st
import json
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

com.iframe("https://lottie.host/7177c8cd-ee13-4dcc-9670-8415b8ed1eac/6zPMaZV0XB.lottie")

com.html("""
         <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script><lottie-player src="https://lottie.host/686bbf25-0539-43b6-bd1b-167659367bb8/BumNjuLsvt.json" background="##FFFFFF" speed="1" style="width: 300px; height: 300px" loop controls autoplay direction="1" mode="normal"></lottie-player>
         """)

with open("CattleBell.json") as source:

    animation = json.load(source)
    st_lottie(animation)



