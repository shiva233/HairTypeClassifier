import numpy as np
import cv2
import tensorflow as tf

# Define the categories
categories = ['Curly', 'Straight', 'Wavy']

# Load the model
model = tf.keras.models.load_model('hair_classification_model.keras')

# Predict on a new image
def predict_hair_type(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to read image: {image_path}")
        return None
    img = cv2.resize(img, (128, 128))
    img = np.expand_dims(img, axis=0) / 255.0
    prediction = model.predict(img)
    hair_type_index = np.argmax(prediction)
    hair_type = categories[hair_type_index]
    confidence = prediction[0][hair_type_index] * 100
    return hair_type, confidence

# Example usage
image_path = 'C:\\Users\\Shiva\\Desktop\\HairTypeClassifer\\markus.png'  # REPLACE THIS WITH YOUR PATH TO THE IMAGE. Use forward slashes (/) or double backslashes (\\)
result = predict_hair_type(image_path)
if result is not None:
    hair_type, confidence = result
    print(f"The predicted hair type is: {hair_type} with a confidence of {confidence:.2f}%")