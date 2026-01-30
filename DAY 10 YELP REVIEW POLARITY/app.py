import streamlit as st
import joblib
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ---------------------------
# Load model & tokenizer
# ---------------------------
@st.cache_resource
def load_artifacts():
    model = load_model("day_10_yelp_polarity.keras")
    tokenizer = joblib.load("day_10_yelp_polarity_token.pkl")
    max_len = joblib.load("day_10_yelp_maxlen.pkl")
    return model, tokenizer, max_len   # ✅ return all 3

model, tokenizer, max_len = load_artifacts()   # ✅ unpack all 3

# ---------------------------
# App UI
# ---------------------------
st.title("🍔 Yelp Review Sentiment Analyzer")
st.write("Enter a restaurant review and predict sentiment.")

text = st.text_area("Enter your review:")

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Tokenize
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=max_len, padding="post")

        # Predict (multiclass)
        preds = model.predict(padded)
        class_id = np.argmax(preds)
        confidence = np.max(preds)

        # Label mapping
        label_map = {
            0: "⭐ Very Negative",
            1: "⭐⭐ Negative",
            2: "⭐⭐⭐ Neutral",
            3: "⭐⭐⭐⭐ Positive",
            4: "⭐⭐⭐⭐⭐ Very Positive"
        }

        st.success(
            f"Prediction: {label_map[class_id]} \n\nConfidence: {confidence:.2f}"
        )
