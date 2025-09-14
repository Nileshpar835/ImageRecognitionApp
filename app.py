# app.py
import streamlit as st
from PIL import Image
import os
from model import predict_image  # ✅ correct import

st.set_page_config(page_title="Image Recognition App", layout="centered")
st.title("🔍 Image Recognition App")
st.write("Upload an image, and I'll try to identify the object!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img_path = "uploaded_image.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    img = Image.open(img_path)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    st.write("Analyzing image...")
    predictions = predict_image(img_path)

    st.subheader("Top Predictions:")
    for i, (_, label, confidence) in enumerate(predictions, start=1):
        st.write(f"{i}. **{label}** - {confidence:.2%}")
