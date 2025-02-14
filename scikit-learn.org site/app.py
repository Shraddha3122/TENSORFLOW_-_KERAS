# app.py
from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras

# Load the trained model
model = keras.models.load_model('iris_model.h5')

# Create a Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(features)
    predicted_class = np.argmax(prediction, axis=1)

    # Map the predicted class back to the original labels
    iris_labels = ['setosa', 'versicolor', 'virginica']
    result = iris_labels[predicted_class[0]]

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)