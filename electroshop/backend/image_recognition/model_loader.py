import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('backend/image_recognition/laptop_model.h5')
label_names = ['asus', 'dell', 'hp', 'lenovo', 'macbook'] 

def identify_laptop(image_path, threshold=0.7):
    image = cv2.imread(image_path)
    if image is None:
        return "Error: Could not read image"
    image = cv2.resize(image, (224, 224))
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    predicted_idx = np.argmax(predictions)
    confidence = predictions[0][predicted_idx]

    if confidence < threshold:
        return "Unknown laptop model (low confidence)"
    else:
        return f"Predicted: {label_names[predicted_idx]} (confidence: {confidence:.2f})"