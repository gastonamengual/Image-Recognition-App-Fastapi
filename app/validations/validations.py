ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


def validate_filename(filename: str):
    if filename == "":
        raise ValueError("filename is empty")

    if (
        "." not in filename
        or filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS
    ):
        raise ValueError("Wrong filename format")
