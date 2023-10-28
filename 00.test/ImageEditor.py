import streamlit as st
from PIL import Image, ImageFilter

st.title("Image Editor")
st.markdown("---")

image = st.file_uploader("Upload Your Image",type=["jpg","jpeg","png"])

size = st.empty()
mode = st.empty()
format_ = st.empty()

if image:
    img = Image.open(image)
    size.markdown(f"<h6>Size : {img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode : {img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Format : {img.format}</h6>",unsafe_allow_html=True)

    st.subheader("Resize Image")
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)

    st.subheader("Rotate Image")
    degree = st.number_input("Degree")

    st.subheader("Filter")
    filters = st.selectbox("Filters", options=("None", "BLUR", "CONTOUR", "SHARPEN", "SMOOTH"))

    btn = st.button("Submit")

    if btn:
        edited = img.resize((width, height)).rotate(degree)

        filtered = edited

        if filters != "None":
            if filters == "BLUR":
                filtered = edited.filter(ImageFilter.BLUR)
            elif filters == "CONTOUR":
                filtered = edited.filter(ImageFilter.CONTOUR)
            elif filters == "SHARPEN":
                filtered = edited.filter(ImageFilter.SHARPEN)
            elif filters == "SMOOTH":
                filtered = edited.filter(ImageFilter.SMOOTH)


        st.image(filtered)