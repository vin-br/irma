from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.urls import path
import os


# Define a custom image classification model
class CustomImageClassification:
    def __init__(self):
        # Load the model
        self.model = None

    def set_model_type_as_densenet121(self):
        # Set the model type to DenseNet121
        pass

    def set_model_path(self, path):
        # Set the model path
        pass

    def set_json_path(self, path):
        # Set the JSON path
        pass

    def load_model(self):
        # Load the model
        pass

    def classify_image(self, image_path, result_count=1):
        # Classify the image
        pass


def main(request):
    if request.method == "POST":
        file1 = request.FILES["file1"]
        path = default_storage.save(file1, "/upload/" + file1.name)
        custom_image_classification = CustomImageClassification()
        custom_image_classification.set_model_type_as_densenet121()
        custom_image_classification.set_model_path(os.getcwd() + "modele.pt")
        custom_image_classification.set_json_path("archive_model_classes.json")
        custom_image_classification.load_model()
        predictions, probabilities = custom_image_classification.classify_image(
            path, result_count=1
        )
        for i, j in zip(predictions, probabilities):
            x = i
            y = j
            print(x, y)
        return HttpResponse("File uploaded successfully!")
    else:
        return render(request, "home.html")


urlpatterns = [
    path("", main),
]
