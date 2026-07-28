import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model("potato_blight_model.h5")

st.title("Potato Blight Classifier: Early vs Late")
st.write("Upload a potato leaf image to classify it as Early Blight or Late Blight.")

uploaded = st.file_uploader("Upload a potato leaf image", type=["jpg", "png", "jpeg"])

if uploaded:
    img = Image.open(uploaded).convert("RGB").resize((224, 224))
    st.image(img, caption="Uploaded Image", use_container_width=True)

    arr = np.expand_dims(np.array(img) / 255.0, axis=0)
    pred = model.predict(arr)[0][0]

    label = "Late Blight" if pred > 0.5 else "Early Blight"
    confidence = pred if pred > 0.5 else 1 - pred

    st.write(f"### Prediction: **{label}**")
    st.write(f"Confidence: {confidence:.2%}")