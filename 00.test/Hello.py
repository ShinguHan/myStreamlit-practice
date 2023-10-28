import streamlit as st
import pandas as pd
import time as tm
from matplotlib import pyplot as plt
import numpy as np

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc3
{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

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
state = st.checkbox("Statement")
if state:
    st.write("Good")
else:
    st.write("Night")


def callback():
    print(st.session_state.checker)

st.checkbox("Callback", on_change=callback, key="checker")

radio_btn = st.radio("which company?", options=["CNS", "SDI"])
print(radio_btn)

def Hi():
    print("Hi~~!!!")

btn = st.button("Click Me!!", on_click=Hi)

select = st.selectbox("When will you sleep?", options=("right now", "10 min later"))
print(select)

multi_select = st.multiselect("How many days?", options=(1,2,3,4))
print(multi_select)

uploader = st.file_uploader("select files")
if uploader is not None:
    st.image(uploader)

uploaders = st.file_uploader("select files", accept_multiple_files=True)
if uploaders is not None:
    st.image(uploaders)

slider = st.slider("select value")
mul_slider = st.select_slider("curious slider", options=(1,2,3,4,))

text = st.text_input("input dream")
st.write(text)

text_area = st.text_area("Input Dreams")
st.write(text_area)

date = st.date_input("When do you retire??")
st.write(date)

time = st.time_input("When??", step=60)
st.write(time)

pb = st.progress(0)

# for i in range(10):
#     pb.progress((i+1)*10)
#     tm.sleep(1)

st.markdown("<h1 style='text-align:center;'>User Registration</h1>",unsafe_allow_html=True)
with st.form('form1', clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    s_name = col2.text_input("Second Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    state = st.form_submit_button("Submit")

    if state:
        if f_name == "" or s_name == "":
            st.warning("Please fill above fileds")
        else:
            st.success("Submitted Successfully")

st.sidebar.write("Hello this is my sidebar")

opt = st.sidebar.radio("Select Any Graph", options=("Line","Bar", "H-Bar"))

x = np.linspace(0,10,100)

if opt == "Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    st.write(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(x, x*10)
    st.write(fig)
elif opt == "H-Bar":
    st.markdown("<h1 style='text-align:center;'>H-Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(x, x*10)
    st.write(fig)