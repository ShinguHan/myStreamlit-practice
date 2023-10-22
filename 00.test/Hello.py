import streamlit as st
import pandas as pd

st.title("안녕 뿌꾸")
st.header("이제 잘까??")
st.subheader("좋아요.. 자요")
st.text("쫗아.. 자는거야")
st.markdown("[google](https://google.com)")
st.caption("Why are you so serious??")

dd = {"a":"11,11,11","b":"sadf"}
st.json(dd)

code = """
print(ff)
def hello():
    return "good"
"""

st.code(code)
st.metric(label="wind speed",value="120ms⁻¹",delta="-1ms⁻¹")


table = pd.DataFrame({"col 1":[1,2,3,4,], "col 2":[5,6,7,8,]})
st.table(table)
st.dataframe(table)
st.image("My.jpg", "Is it me??")
st.audio("wobble.mp3")
st.video("first.mp4")