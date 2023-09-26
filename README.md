# Image-Recognition-App

This app is an example of a pure MLOps probelm solving. The purpose of the app is to input an image and via a MobileNet predict the objects in it. Originally it consisted on two separate components:
* A standalone Python package with the OpenCV model.
* A server side API developed with FastAPI that consumes de model package, deployed in Vercel
* A dummy client side developed with HTML, CSS and Javascript deployed in GitHub Pages.

However, Vercel supports until 250MB of app size, and the model package, which uses OpenCV and another ML libraries, exceeded that number. Then, another solution had to be found. The model package was transformed into another API developed in Gradio and hosted in the free service Hugging Face. Then, the first API now consumes from this second API. Moreover, the image sending handling had to be changed, consisting in several transformations between lists, JSON strings and byte objects.

The resulting architecture is as follows:
1. A dummy client side developed with HTML, CSS and Javascript deployed in GitHub Pages that calls API_1.
2. An API_1 developed with FastAPI hosted in Vercel that calls API_2.
3. An API_2 that hosts the model, developed with Gradio and hosted in Hugging Face.
4. A Python package with the model, unused and replaced by API_2 because of hardware limitations.

API_1 supports automated CI/CD in GitHub Actions. Building includes installing of dependencies,  testing in Pytest, formatting with black and linter. Deployment includes both GitHub Pages and Vercel.

The model Python package supports automated CI/CD in GitHub Actions. Building inludes installing of dependencies, testing in Pytest, formatting with black and linter and package building with setuptools. Deployment includes publishing to PyPI with Twine.

#### FULL TECHNOLOGIES STACK

[API]
* FastAPI
* Uvicorn
* Gradio

[Machine Learning]
* Numpy
* matplotlib
* Pillow
* OpenCV

[Services]
* GitHub Actions
* Vercel
* Hugging Face
* PyPI

[Testing, formatting and building]
* Pytest
* Flake8
* Black
* Pre-commit
* setuptools
* Twine