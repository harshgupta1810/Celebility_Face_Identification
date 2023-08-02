# Project Name: Face Recognition App

## Project Description:
This project is a simple Face Recognition App that uses a machine learning model to identify faces with two eyes in an image. The app takes an image as input, detects faces in the image, and then checks if each detected face has two eyes. If a face with two eyes is found, it classifies the image based on the trained model and displays the result. The purpose of this project is to provide a basic demonstration of face recognition using a machine learning model.

## Table of Contents:
1. Project Demo
2. Badges
3. Installation
4. Usage
5. Configuration
6. Contributing
7. License
8. Acknowledgments

## Project Demo:
Unfortunately, this README file format does not allow the inclusion of live demos. However, you can run the code provided in the code section to experience the Face Recognition App.

## Badges:
Add any relevant badges, such as build status or version, to showcase the project's status or achievements.

## Installation:
To use this project, you'll need the following dependencies:
- Python (version 3.7 or higher)
- joblib
- json
- numpy
- base64
- cv2 (OpenCV)
- streamlit
- PIL (Python Imaging Library)

You can install these dependencies using pip with the following command:

```
pip install joblib json numpy opencv-python streamlit pillow
```

## Usage:
Follow the steps below to use the Face Recognition App:

1. Download the trained machine learning model and place it in the same directory as the code. The model file should be named 'saved_model.pkl'.

2. Create a 'class_dictionary.json' file that maps class names to numbers. The JSON file should be in the format:
```json
{
    "class_name_1": 0,
    "class_name_2": 1,
    ...
}
```
Replace "class_name_1", "class_name_2", etc., with the names of classes used for training the model.

3. Import the necessary libraries and functions from the code:

```python
import joblib
import json
import numpy as np
import base64
import cv2
import streamlit as st
from PIL.Image import Image
from wavelet import w2d
```

4. Load the saved artifacts (model and class dictionary):

```python
load_saved_artifacts()
```

5. Run the Streamlit app:

```python
app()
```

6. Use the app by uploading an image and checking the predictions.

## Configuration:
No additional configuration is required for this project.

## Contributing:
If you want to contribute to this project, you can follow these steps:
1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your changes.
3. Make your desired changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the original repository, explaining your changes and the purpose of the pull request.

## License:
Add the license information here. Choose an appropriate license for your project.

## Acknowledgments:
Give credit to any external libraries, tools, or contributors that have helped with the development of your project.
