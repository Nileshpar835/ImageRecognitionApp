import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load pre-trained model once
model = MobileNetV2(weights='imagenet')

def predict_img(img_file):
    # Load image
    img = image.load_img(img_file, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict
    preds = model.predict(x)
    results = decode_predictions(preds, top=3)[0]

    # Format predictions
    output = []
    for (_, label, prob) in results:
        output.append(f"{label} ({prob*100:.2f}%)")
    return output
