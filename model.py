# model.py
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights="imagenet")

def predict_image(img_path: str):
    """
    Predict the top 3 objects in the given image.
    """
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)
    decoded = decode_predictions(predictions, top=3)[0]
    return decoded
