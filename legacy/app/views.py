import base64
import os
import json
from django.shortcuts import render
from django.conf import settings
from django.urls import path
from django.contrib import messages
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
from models.yolo import annotate_image


# Load the pre-trained model and the prediction classes
model = load_model("./models/ResNet50V2-32.keras")
classes_file_path = os.path.join(os.getcwd(), "models", "classes.json")


def index(request):
    class_pred, class_prob, tumor = None, None, None
    prediction_made = False
    annotated_image_base64 = None

    if request.method == "POST":
        if "file1" not in request.FILES:
            messages.error(
                request,
                "Select an image before asking ARC",
            )
        else:
            file1 = request.FILES["file1"]
            path = os.path.join(settings.MEDIA_ROOT, file1.name)

            # Reading the file contents and writing them to disk
            with open(path, "wb+") as f:
                file1.seek(0)  # Reset the file pointer to the beginning
                contents = file1.read()  # Read the entire file into memory
                f.write(contents)  # Write the contents to disk

            with open(classes_file_path, "r") as f:
                classes_data = json.load(f)

            # Path to the user's file
            image_path = os.path.join(os.getcwd(), "media", str(file1.name))

            # Load the user's image
            user_image = image.load_img(image_path, target_size=(224, 224))

            # Convertir l'image en tableau et redimensionner les pixels
            user_image = image.img_to_array(user_image)
            user_image /= 255.0
            user_image = np.expand_dims(user_image, axis=0)

            # Predict using pre-trained model
            prediction = model.predict(user_image)
            class_index = np.argmax(prediction)
            class_pred = classes_data[str(class_index)]
            class_prob = (np.max(prediction)) * 100

            if class_pred == "no_tumor":
                tumor = False
            else:
                # Annotate image using YOLO model
                annotated_image_path = annotate_image(image_path)
                with open(annotated_image_path, "rb") as f:
                    annotated_image_data = f.read()
                annotated_image_base64 = base64.b64encode(annotated_image_data).decode()
                tumor = True

            prediction_made = True

    else:
        pass

    context = {
        "prediction": class_pred,
        "probability": class_prob,
        "prediction_made": prediction_made,
        "annotated_image": annotated_image_base64,
        "yolo": tumor,
    }

    return render(request, "index.html", context)


urlpatterns = [
    path("", index),
]
