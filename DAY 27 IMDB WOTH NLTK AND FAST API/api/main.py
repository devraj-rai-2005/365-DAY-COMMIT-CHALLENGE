# Importing the Model

import joblib

vector = joblib.load('imdb_vector.pkl')
model = joblib.load('imdb_model.pkl')

# Making a Preprocess Input 

import re
import string
import nltk
import contractions

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemma = WordNetLemmatizer()
stop_word = set(stopwords.words('english'))

def clean_text(text):
  text = contractions.fix(text)
  text = text.lower()
  text = re.sub(r'http\S+' , '' , text)
  text = re.sub(r'<.*?>' , '',text)
  text = text.translate(str.maketrans('' , '' , string.punctuation))
  token = word_tokenize(text)
  final = [lemma.lemmatize(word) for word in token if word not in stop_word]
  return ' '.join(final)


# Making a Fast API app 

from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI(title = 'IMDB Dataset Sentiment Analysis')


@app.get("/")
def home():
  return {'message' : "This is a IMDB Dataset Sentiment Analysis"}


class validate_model(BaseModel):
  text : str


@app.post("/predict")
def predict_sentiment(data : validate_model):
  
  text = data.text

  cleaned_text = clean_text(text)

  text_vector = vector.transform([cleaned_text])

  prediction = model.predict(text_vector)

  y_pred = int(prediction[0])

  sentiment_mapping = { 0 : "Negative" , 1 : "Positive"}.get(y_pred)

  return {'Prediction' : f"The review is {sentiment_mapping}"}
