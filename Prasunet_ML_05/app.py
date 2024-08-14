from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder where uploaded images are saved

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# Home route
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Load your .keras model
    model = load_model('best_model_10class.keras 22.keras')

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Preprocess the image for prediction
        img = Image.open(file_path)
        img = img.resize((224, 224))  # Resize as per your model input size
        img = img.convert('RGB')  # Ensure image is RGB

        # Make the prediction
        prediction = model.predict(img)

        return f"Predicted Class: {predicted_class[0]}"

if __name__ == '__main__':
    app.run(debug=True)
