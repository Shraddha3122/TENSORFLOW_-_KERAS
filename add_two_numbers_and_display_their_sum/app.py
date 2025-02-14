#With the help of placeholders in TensorFlow, add two numbers and display their sum

from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    # Get JSON data 
    data = request.get_json()
    
    # Extract numbers
    num1 = data.get('num1')
    num2 = data.get('num2')

    # Check if both numbers are provided
    if num1 is not None and num2 is not None:
        # Use TensorFlow to add the numbers
        a = tf.constant(num1)
        b = tf.constant(num2)
        sum_result = tf.add(a, b).numpy() 

        # Convert the result
        sum_result = int(sum_result)

        # Return the result as JSON
        return jsonify({'sum': sum_result})
    else:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400

if __name__ == '__main__':
    app.run(debug=True)