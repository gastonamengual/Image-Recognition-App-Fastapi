const submitButton = document.getElementById("submit-button");

submitButton.addEventListener("click", () => {
    const image = document.getElementById("image-upload").files[0];
    if (typeof image === 'undefined') {
        throw new Error('image is undefined');
    }

    const formData = new FormData();
    formData.append("image", image);

    fetch("https://image-recognition-app-fastapi.vercel.app/detect_objects", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.blob())
        .then((blob) => {
            const resultImage = document.getElementById("result-image");
            resultImage.src = URL.createObjectURL(blob);
            console.log(blob)
            console.log(resultImage.src)
            $('#object_detection_modal').modal("show");
        });
});
