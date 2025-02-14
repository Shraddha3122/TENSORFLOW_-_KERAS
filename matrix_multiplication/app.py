 #Take two matrices and perform matrix multiplication in TensorFlow using placeholders

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def multiply_matrices():
    # Get the matrices from the request
    data = request.get_json()
    matrix_a = np.array(data['matrix_a'])
    matrix_b = np.array(data['matrix_b'])
    
    # Check if the matrices can be multiplied
    if matrix_a.shape[1] != matrix_b.shape[0]:
        return jsonify({'error': 'Incompatible matrix dimensions for multiplication'}), 400
    
    # Perform matrix multiplication using TensorFlow
    result = tf.matmul(matrix_a, matrix_b).numpy()  
    
    return jsonify(result.tolist())

if __name__ == '__main__':
    app.run(debug=True)