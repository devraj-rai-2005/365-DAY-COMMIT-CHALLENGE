import streamlit as st
from transformers import pipeline
import torch

# ---------------- Page Config ----------------
st.set_page_config(page_title="Multi NLP App", layout="centered")
st.title("🧠 Multi-Task NLP App")

# ---------------- Device ----------------
device = 0 if torch.cuda.is_available() else -1

# ---------------- Tasks ----------------
TASKS = {
    "Sentiment Analysis": "sentiment-analysis",
    "Text Generation": "text-generation",
    "Summarization": "summarization",
    "Named Entity Recognition": "ner",
    "Translation (ENGLISH → GERMAN)": "translation"
}

task_name = st.selectbox("Select NLP Task", list(TASKS.keys()))
user_text = st.text_area("Enter your text")

# ---------------- Model Loader ----------------
@st.cache_resource
def load_model(task):
    # Explicit model for translation
    if task == "translation":
        return pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-de",
            device=device
        )
    else:
        return pipeline(task, device=device)

# ---------------- Run Button ----------------
if st.button("Run Model"):

    if user_text.strip() == "":
        st.warning("Please enter text")
    else:
        task_key = TASKS[task_name]
        model = load_model(task_key)

        with st.spinner("Running model..."):

            # -------- SENTIMENT --------
            if task_name == "Sentiment Analysis":
                output = model(user_text)[0]
                st.success(f"Label: {output['label']}")
                st.info(f"Confidence: {round(output['score']*100, 2)}%")

            # -------- TEXT GENERATION --------
            elif task_name == "Text Generation":
                output = model(
                    user_text,
                    max_length=120,
                    do_sample=True,
                    temperature=0.7,
                    top_k=50
                )[0]["generated_text"]

                st.subheader("Generated Text")
                st.write(output)

            # -------- SUMMARIZATION --------
            elif task_name == "Summarization":
                output = model(
                    user_text,
                    max_length=120,
                    min_length=30
                )[0]["summary_text"]

                st.subheader("Summary")
                st.write(output)

            # -------- TRANSLATION --------
            elif task_name == "Translation (ENGLISH → GERMAN)":
                output = model(
                    user_text,
                    max_length=80
                )[0]["translation_text"]

                st.subheader("Translated Text")
                st.write(output)

            # -------- NER --------
            elif task_name == "Named Entity Recognition":
                entities = model(user_text)

                if len(entities) == 0:
                    st.warning("No entities detected.")
                else:
                    st.subheader("Entities Found")
                    for ent in entities:
                        st.write(
                            f"🟢 **{ent['word']}** → {ent['entity']} "
                            f"(confidence: {round(ent['score']*100,2)}%)"
                        )
