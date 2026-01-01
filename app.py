import streamlit as st
from helmet_detection import detect_helmet
from PIL import Image
import numpy as np

st.title("Helmet Detection System")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="Original Image")

    result_img, helmet_found = detect_helmet(img_array)

    st.image(result_img, caption="Helmet Detection Result")

    st.warning(
    "⚠️ Helmet detection completed. "
    "Helmet presence could not be verified accurately. "
    "Please ensure helmet usage for rider safety."
)

