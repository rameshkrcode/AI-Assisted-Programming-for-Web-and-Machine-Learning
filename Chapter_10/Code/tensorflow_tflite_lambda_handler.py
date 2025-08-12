import tensorflow as tf
import numpy as np
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
def lambda_handler(event, context):
    input_data = np.array([[event['features']]], dtype=np.float32)
    interpreter.set_tensor(0, input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(1)
    return {'prediction': float(output_data[0][0])}
