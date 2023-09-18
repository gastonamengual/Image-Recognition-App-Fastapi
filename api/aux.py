# import importlib.resources

# import numpy as np
# from numpy.typing import ArrayLike
# from object_detection_model import model_files as model_files
# from object_detection_model.model import (
#     CONFIG_FILE_NAME,
#     FROZEN_MODEL_NAME,
#     LABELS_NAME,
#     ModelConfig,
# )

# ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


# def get_model_config() -> ModelConfig:
#     config_file_path = str(
#         next(importlib.resources.path(model_files, CONFIG_FILE_NAME).gen)
#     )
#     frozen_model_path = str(
#         next(importlib.resources.path(model_files, FROZEN_MODEL_NAME).gen)
#     )
#     labels_path = str(next(importlib.resources.path(model_files, LABELS_NAME).gen))

#     return ModelConfig(
#         config_file_path=config_file_path,
#         frozen_model_path=frozen_model_path,
#         labels_path=labels_path,
#     )


# def validate_image_filename(image_filename: str):
#     if image_filename == "":
#         raise ValueError("No image Selected")


# def validate_correct_extension(image_filename: str):
#     if (
#         "." not in image_filename
#         and image_filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
#     ):
#         raise ValueError("Wrong filename format")


# def process_image(image_file: bytes) -> ArrayLike:
#     processed_image = np.frombuffer(image_file, dtype=np.uint8)
#     return processed_image
