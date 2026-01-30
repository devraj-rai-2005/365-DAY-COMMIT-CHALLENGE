import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json

# ---------------------------
# Load model and class names
# ---------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(
        "day_6_plant_village_model.keras",
        compile=False
    )
    return model


@st.cache_data
def load_class_names():
    with open("day_6_plant_village_names.json", "r") as f:
        return json.load(f)

model = load_model()
class_names = load_class_names()

IMG_SIZE = 255

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Food-101 Classifier", layout="centered")
st.title("🌿 Plant Leaves Image Classifier")
st.write("Upload a food image and let the CNN predict the dish.")

uploaded_file = st.file_uploader(
    "Upload Leaves Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------------------
# Preprocessing function
# ---------------------------
def preprocess_image(img):
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0      # same normalization you used
    img = np.expand_dims(img, axis=0)
    return img

# ---------------------------
# Prediction
# ---------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    processed_img = preprocess_image(image)

    if st.button("Predict"):
        with st.spinner("Predicting..."):
            preds = model.predict(processed_img)
            class_id = np.argmax(preds)
            confidence = np.max(preds)

            predicted_class = class_names[class_id]

        st.success(f"🌿 Prediction: **{predicted_class}**")
        st.info(f"🎯 Confidence: **{confidence:.2f}**")


