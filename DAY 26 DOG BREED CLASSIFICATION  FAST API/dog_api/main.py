import json 
from keras.models import load_model

with open('class_names.json' , "r") as f:
    class_name = json.load(f)

model = load_model('dog_breed_model.keras')


from fastapi import FastAPI

app = FastAPI(title = 'Dog Breed Classification')

@app.get("/")
def home():
    return {"Message" : "This is a Dog Breed Clasification there are almost common and uncommon Dog Breed Classification"}

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from keras.models import load_model
from PIL import Image
import numpy as np
import json
import io
from keras.applications.inception_v3 import preprocess_input

IMG_SIZE = 299   # same as your Streamlit code

# -----------------------------
# Preprocessing (same logic)
# -----------------------------

def preprocess_image(img: Image.Image):

    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img).astype(np.float32)

    img = preprocess_input(img)

    img = np.expand_dims(img, axis=0)

    return img




@app.get("/")
def helath():
    return {"message": "Dog Breed image classification API is running"}


# -----------------------------
# Prediction
# -----------------------------

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):

    # basic file validation
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid image type")

    try:
        contents = await file.read()

        image = Image.open(io.BytesIO(contents)).convert("RGB")

        processed_img = preprocess_image(image)

        preds = model.predict(processed_img)

        class_id = int(np.argmax(preds[0]))
        confidence = float(np.max(preds[0]))

        predicted_class = class_name[class_id]

        return JSONResponse({
            "predicted_class": predicted_class,
            "confidence": confidence
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
