from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from keras.models import load_model
from PIL import Image
import numpy as np
import json
import io

app = FastAPI(title="Leaves Classifier API")

# -----------------------------
# Load model & class names
# -----------------------------

model = load_model("day_6_plant_village_model.keras")

with open("day_6_plant_village_names.json") as f:
    class_names = json.load(f)

IMG_SIZE = 255   # same as your Streamlit code

# -----------------------------
# Preprocessing (same logic)
# -----------------------------

def preprocess_image(img: Image.Image):

    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    return img


# -----------------------------
# Health
# -----------------------------

@app.get("/")
def home():
    return {"message": "Leaves image classification API is running"}


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

        predicted_class = class_names[class_id]

        return JSONResponse({
            "predicted_class": predicted_class,
            "class_id": class_id,
            "confidence": confidence
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
