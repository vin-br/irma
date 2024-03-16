# from roboflow import Roboflow
# import supervision as sv
# import cv2

# rf = Roboflow(api_key="VmGIn8r71MJ4pizshqjH")
# project = rf.workspace().project("gauss-3")
# model = project.version(1).model

# result = model.predict("./media/G_0057.jpg", confidence=40, overlap=30).json()

# labels = [item["class"] for item in result["predictions"]]

# detections = sv.Detections.from_inference(result)

# label_annotator = sv.LabelAnnotator()
# bounding_box_annotator = sv.BoundingBoxAnnotator()

# image = cv2.imread("./media/G_0057.jpg")

# annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
# annotated_image = label_annotator.annotate(
#     scene=annotated_image, detections=detections, labels=labels
# )

# sv.plot_image(image=annotated_image)


# import cv2
# import io
# import supervision as sv
# from roboflow import Roboflow


# def annotate_image(image_path):
#     rf = Roboflow(api_key="VmGIn8r71MJ4pizshqjH")
#     project = rf.workspace().project("gauss-3")
#     model = project.version(1).model

#     result = model.predict(image_path, confidence=40, overlap=30).json()

#     labels = [item["class"] for item in result["predictions"]]

#     detections = sv.Detections.from_inference(result)

#     label_annotator = sv.LabelAnnotator()
#     bounding_box_annotator = sv.BoundingBoxAnnotator()

#     image = cv2.imread(image_path)

#     annotated_image = bounding_box_annotator.annotate(
#         scene=image, detections=detections
#     )
#     annotated_image = label_annotator.annotate(
#         scene=annotated_image, detections=detections, labels=labels
#     )

#     # Convertir l'image en données binaires pour la renvoyer via HTTP
#     buffer = io.BytesIO()
#     buffer.write(cv2.imencode(".jpg", annotated_image)[1])
#     annotated_image_data = buffer.getvalue()

#     return annotated_image_data

import os
import cv2
import supervision as sv
from roboflow import Roboflow


def annotate_image(image_path):
    rf = Roboflow(api_key="VmGIn8r71MJ4pizshqjH")
    project = rf.workspace().project("gauss-3")
    model = project.version(1).model

    result = model.predict(image_path, confidence=40, overlap=30).json()

    labels = [item["class"] for item in result["predictions"]]

    detections = sv.Detections.from_inference(result)

    label_annotator = sv.LabelAnnotator()
    bounding_box_annotator = sv.BoundingBoxAnnotator()

    image = cv2.imread(image_path)

    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections
    )
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections, labels=labels
    )

    # Enregistrer l'image annotée sur disque
    annotated_image_path = os.path.splitext(image_path)[0] + "_annotated.jpg"
    cv2.imwrite(annotated_image_path, annotated_image)

    return annotated_image_path
