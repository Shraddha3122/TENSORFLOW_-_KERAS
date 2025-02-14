#Using TensorFlow, add two numbers and display their sum

from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    # add the two numbers
    sum_result = tf.add(num1, num2).numpy()  
    
    # Convert the result 
    return jsonify({'sum': int(sum_result)})

if __name__ == '__main__':
    app.run(debug=True)