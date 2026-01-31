# Making a Text Cleaning Preprocess

import nltk
import string 
import re
import contractions 

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_word = set(stopwords.words('english'))
lemma = WordNetLemmatizer()

def clean_text(text):
  text = contractions.fix(text)
  text = text.lower()
  text = re.sub(r'http\S+' , '' , text)
  text = re.sub(r'<.*?>'  , '' , text)
  text = text.translate(str.maketrans('' , '' , string.punctuation))
  token = word_tokenize(text)
  final = [lemma.lemmatize(word) for word in token if word not in stop_word]
  return ' '.join(final)


# Importing a Models 

import joblib

token = joblib.load('ag_token.pkl')

from keras.models import load_model

model = load_model('ag_new_model.keras')

max_len = 98

import numpy as np
from fastapi import FastAPI


# Making a Pydantic Model 

from pydantic import BaseModel
from tensorflow.keras.preprocessing.sequence import pad_sequences

class validate_model(BaseModel): 
  title : str
  description : str


app = FastAPI(title = 'AG News Classification')


@app.get("/")
def home():
  return {'Message' : "This a AG News Classification."}


@app.post("/predict")
def predict_data(data : validate_model):
  title = data.title
  description = data.description

  data = title + "  "  + description 

  cleaned_data = clean_text(data)

  token_data = token.texts_to_sequences([cleaned_data])

  padded_data = pad_sequences(token_data , maxlen = max_len , padding = 'post')
  
  y_pred = model.predict(padded_data)
  
  class_id = int(np.argmax(y_pred, axis=1)[0])
  
  map_data = {0:'World',1:'Sports',2:'Business',3:'Science and Technology'}.get(class_id)
  
  return {
    "Prediction": {
        "class_id": class_id,
        "Class name": map_data
    }
}
