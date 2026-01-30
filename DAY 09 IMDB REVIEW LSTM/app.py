import streamlit as st
import numpy as np
import re
import string
import contractions
import joblib
import tensorflow 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ---------------- LOAD ASSETS ----------------
@st.cache_resource
def load_assets():
    model = load_model("day_9_imdb_lstm.keras")
    tokenizer = joblib.load("tokenizer.pkl")
    max_len = joblib.load("max_len.pkl")
    return model, tokenizer, max_len

model, tokenizer, max_len = load_assets()

# ---------------- NLP SETUP ----------------
stop_word = stopwords.words("english")
lemma = WordNetLemmatizer()

def clean_text(text):
    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    final = [lemma.lemmatize(word) for word in tokens if word not in stop_word]
    return " ".join(final)

def preprocess(text):
    cleaned = clean_text(text)
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=max_len, padding="post")
    return padded

# ---------------- UI ----------------
st.set_page_config(page_title="IMDB Sentiment Analyzer", layout="centered")
st.title("🎬 IMDB Sentiment Analyzer")
st.write("Enter a movie review and get sentiment prediction.")

user_text = st.text_area("✍️ Enter your review here:")

if st.button("Predict Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_data = preprocess(user_text)
        prediction = model.predict(input_data)[0][0]

        if prediction > 0.5:
            st.success(f"😊 Positive Review (Confidence: {prediction:.2f})")
        else:
            st.error(f"😞 Negative Review (Confidence: {1 - prediction:.2f})")

