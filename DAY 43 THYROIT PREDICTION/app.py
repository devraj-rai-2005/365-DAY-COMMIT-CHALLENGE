import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision import models
from PIL import Image
import numpy as np
from efficientnet_pytorch import EfficientNet


import torch
import torch.nn as nn
from efficientnet_pytorch import EfficientNet
import streamlit as st

@st.cache_resource
def load_model():

    model = EfficientNet.from_name("efficientnet-b0")

    # classifier must match training architecture
    model._fc = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(model._fc.in_features, 3)
    )

    state_dict = torch.load("best_model.pth", map_location="cpu")

    model.load_state_dict(state_dict)

    model.eval()

    return model

model = load_model()

# ---------------------------
# Class Names (3 classes)
# ---------------------------
class_names = [
    "Benign",
    "Malignant",
    "Normal"
]

IMG_SIZE = 224

# ---------------------------
# Image Transform
# ---------------------------
from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Thyroid Classifier", layout="centered")

st.title("🧠 Thyroid Disease Classifier")
st.write("Upload an image to classify Thyroid condition.")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------------------
# Prediction
# ---------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = transform(image)
    img = img.unsqueeze(0)

    if st.button("Predict"):

        with st.spinner("Predicting..."):

            with torch.no_grad():
                outputs = model(img)
                probs = torch.softmax(outputs, dim=1)

                confidence, predicted = torch.max(probs, 1)

                predicted_class = class_names[predicted.item()]

        st.success(f"Prediction: **{predicted_class}**")
        st.info(f"Confidence: **{confidence.item():.2f}**")