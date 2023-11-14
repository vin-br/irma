import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import path

from imageai.Classification.Custom import CustomImageClassification


def index(request):
    if request.method == "POST":
        if "file1" not in request.FILES:
            return HttpResponse("There is no file1 in form!", status_code=400)
        file1 = request.FILES["file1"]
        path = os.path.join(settings.MEDIA_ROOT, file1.name)

        # Reading the file contents and writing them to disk
        with open(path, "wb+") as f:
            file1.seek(0)  # Reset the file pointer to the beginning
            contents = file1.read()  # Read the entire file into memory
            f.write(contents)  # Write the contents to disk

        prediction = CustomImageClassification()
        prediction.setModelTypeAsDenseNet121()
        prediction.setModelPath(os.getcwd() + "/model.pt")
        prediction.setJsonPath("archive_model_classes.json")
        prediction.loadModel()

        predictions, probabilities = prediction.classifyImage(
            (os.getcwd() + "/media/" + str(file1.name)), result_count=1
        )

        for i, j in zip(predictions, probabilities):
            x = i
            y = j
            print(x, y)
    else:
        i = 0
        j = 1

    return render(request, "index.html", {"i": i, "j": j})


urlpatterns = [
    path("", index),
]
