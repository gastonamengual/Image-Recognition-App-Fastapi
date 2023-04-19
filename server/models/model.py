from dataclasses import dataclass
import io

import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")  # Solves some error


class ModelConfig:
    config_file_path: str = "server/models/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    frozen_model_path: str = (
        "server/models/object_detection/frozen_inference_graph.pb"
    )
    labels_path: str = "server/models/object_detection/coco.names"
    output_filename: str = "prediction.png"


@dataclass
class Model:
    config: ModelConfig

    def __init__(self, config: ModelConfig):
        self.config = config

    def detect_object(self, data) -> io.BytesIO:
        img = cv2.imdecode(buf=data, flags=1)

        model = cv2.dnn_DetectionModel(
            model=self.config.frozen_model_path, config=self.config.config_file_path
        )

        classLabels = []
        with open(self.config.labels_path, "rt") as fpt:
            classLabels = fpt.read().rstrip("\n").split("\n")

        model.setInputSize(320, 320)
        model.setInputScale(1.0 / 127.5)  # 255/2
        model.setInputMean((127.5, 127.5, 127.5))  # movilenet -> [-1,1]
        model.setInputSwapRB(True)

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)

        ClassIndex = ClassIndex - 1
        classLabels[ClassIndex[0]], classLabels[ClassIndex[-1]]

        for ClassInd, conf, boxes in zip(
            ClassIndex.flatten(), confidence.flatten(), bbox
        ):
            cv2.rectangle(img, boxes, (255, 0, 0), 6)
            cv2.putText(
                img=img,
                text=classLabels[ClassInd],
                org=(boxes[0] + 10, boxes[1] + 40),
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=12,
                color=(0, 0, 255),
                thickness=8,
            )

        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])

        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, bbox_inches="tight", format="png")
        img_bytes.seek(0)

        return img_bytes
