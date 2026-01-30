import streamlit as st
import joblib
import re
import contractions
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="NLP Text Classifier",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_models():
    model = joblib.load("DAY_8_NEWSPAPER_NLTK_model.pkl")
    vectorizer = joblib.load("day_8_NEWSPAPER_TFIDF.pkl")
    return model, vectorizer

model, vectorizer = load_models()

# -----------------------------
# NLP Preprocessing
# -----------------------------
stop_word = set(stopwords.words('english'))
lemma = WordNetLemmatizer()

def clean_text(text):
    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    token = word_tokenize(text)
    final = [lemma.lemmatize(word) for word in token if word not in stop_word]
    return " ".join(final)

# -----------------------------
# UI
# -----------------------------
st.title("🧠 NLP Text Classification App")
st.write("Baseline model using **TF-IDF + Machine Learning**")

user_text = st.text_area(
    "Enter your text below:",
    height=180,
    placeholder="Type or paste your sentence here..."
)

LABEL_MAP = {
    0: "alt.atheism",
    1: "comp.graphics",
    2: "comp.os.ms-windows.misc",
    3: "comp.sys.ibm.pc.hardware",
    4: "comp.sys.mac.hardware",
    5: "comp.windows.x",
    6: "misc.forsale",
    7: "rec.autos",
    8: "rec.motorcycles",
    9: "rec.sport.baseball",
    10: "rec.sport.hockey",
    11: "sci.crypt",
    12: "sci.electronics",
    13: "sci.med",
    14: "sci.space",
    15: "soc.religion.christian",
    16: "talk.politics.guns",
    17: "talk.politics.mideast",
    18: "talk.politics.misc",
    19: "talk.religion.misc"
}



if st.button("Predict 🚀"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Preprocess
        cleaned = clean_text(user_text)

        # Vectorize
        vectorized = vectorizer.transform([cleaned])
        
        

        # Prediction
        prediction = model.predict(vectorized)[0]
        proba = model.predict_proba(vectorized).max()
        
        predicted_label = LABEL_MAP[prediction]
        

        # Output
        st.success(f"Predicted Label: **{predicted_label}**")
        st.info(f"Confidence: **{proba:.2f}**")




        # Debug info (optional)
        with st.expander("Show processed text"):
            st.write(cleaned)
