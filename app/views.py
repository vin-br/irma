import os

from django.shortcuts import render
from django.conf import settings
from django.urls import path
from django.contrib import messages

from imageai.Classification.Custom import CustomImageClassification


def index(request):
    i, j = None, None
    prediction_made = False
    if request.method == "POST":
        choice = request.POST.get("choice")
        if "file1" not in request.FILES:
            messages.error(
                request,
                "Select an image before asking ARC",
            )
        else:
            file1 = request.FILES["file1"]
            path = os.path.join(settings.MEDIA_ROOT, file1.name)
            choice = request.POST.get("choice")

            # Reading the file contents and writing them to disk
            with open(path, "wb+") as f:
                file1.seek(0)  # Reset the file pointer to the beginning
                contents = file1.read()  # Read the entire file into memory
                f.write(contents)  # Write the contents to disk

            if choice == "Brain":
                # Do something for Brain
                prediction = CustomImageClassification()
                prediction.setModelTypeAsDenseNet121()
                prediction.setModelPath(os.getcwd() + "/model.pt")
                prediction.setJsonPath("archive_model_classes.json")
                prediction.loadModel()

                predictions, probabilities = prediction.classifyImage(
                    (os.getcwd() + "/media/" + str(file1.name)), result_count=1
                )

                for i, j in zip(predictions, probabilities):
                    if j >= 0.85:
                        prediction_made = True

            elif choice == "Eyes":
                pass

            else:
                pass

    else:
        pass

    return render(
        request,
        "index.html",
        {"prediction": i, "probability": j, "prediction_made": prediction_made},
    )


urlpatterns = [
    path("", index),
]
