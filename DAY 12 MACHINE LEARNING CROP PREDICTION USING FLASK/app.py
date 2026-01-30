import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib 

flask_app = Flask(__name__)

model = joblib.load('day_12_ml_crop_model.pkl')
encoder = joblib.load('encoder.pkl')  

@flask_app.route('/')
def Home():
    return render_template('index.html')

@flask_app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    
    columns = ['Nitrogen', 'Phosphorous', 'Potatsium', 'temperature', 'humidity', 'ph', 'rainfall']
    input_df = pd.DataFrame([float_features], columns=columns)

    prediction_num = model.predict(input_df)[0]
    crop_name = encoder.inverse_transform([prediction_num])[0]

    return render_template(
        'index.html',
        prediction_text=f"The Predicted Crop is: {crop_name.upper()} 🌱"
    )

if __name__ == '__main__':
    flask_app.run(debug=True)
