import streamlit as st
from model import predict_img
from PIL import Image

st.set_page_config(page_title="Image Recognition App", layout="centered")

st.title("🖼️ Image Recognition App")
st.write("Upload an image and let AI tell you what it is!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.write("🔍 Classifying...")
    predictions = predict_img(uploaded_file)

    st.subheader("✅ Results:")
    for p in predictions:
        st.write(p)
