#Write program using TensorFlow to raises a number to a particular power value

from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

@app.route('/power', methods=['POST'])
def power():
    # Get the JSON data from the request
    data = request.get_json()

    # Validate input
    if not data or 'base' not in data or 'exponent' not in data:
        return jsonify({'error': 'Please provide both base and exponent.'}), 400

    base = data['base']
    exponent = data['exponent']

    # Check if base and exponent are numbers
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        return jsonify({'error': 'Base and exponent must be numbers.'}), 400

    try:
        # Convert base and exponent to TensorFlow tensors
        base_tensor = tf.constant(base, dtype=tf.float32)
        exponent_tensor = tf.constant(exponent, dtype=tf.float32)

        # Calculate the power using TensorFlow
        result_tensor = tf.pow(base_tensor, exponent_tensor)

        # Convert the result back to a Python number
        result = result_tensor.numpy().item()

        return jsonify({'base': base, 'exponent': exponent, 'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)