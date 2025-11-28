# ARC

AI Radiology Copilot (ARC) 

Web-based app to detect brain tumors from MRI images using a Convolutional Neural Network (CNN) model. 

## Overview

### Demo

Check out this [video](path/to/demo.mp4) for a demonstration on how to start and use the app.

### Visuals

<img src="path/to/screenshot_1.png" style="width: 100%; height: auto;">

<img src="path/to/screenshot_3.png" style="width: 100%; height: auto;">

## Installation

This installation uses PyEnv to manage the Python version on your local machine. If you do not wish to install PyEnv, you can download and install Python directly and skip steps 1 and 2.

Please follow these steps to install the project with PyEnv:

1. Install Python with Pyenv: ```pyenv install 3.14.0```

2. Set the Python version as either local or global: ```pyenv local 3.14.0``` or ```pyenv global 3.14.0```

3. Then, use cd to move to the project's folder.

4. Create a virtual environment: ```python -m venv .venv```

5. Activate the virtual environment on linux or macOS: ```source .venv/bin/activate```

6. Upgrade pip to the latest version: ```python -m pip install --upgrade pip```

7. Install the project in editable mode: ```python -m pip install -e .```

8. Install the packages with either the requirements or the individual list provided if the requirements fail to install: ```pip install -r requirements.txt``` or ```pip install "fastapi[standard]" pillow torch torchvision ipykernel plotly```

## Run FastAPI app

- Use FastAPI's uvicorn command to start the project from root: ```uvicorn backend.app.main:app --reload```.

## Unit testing

- Run the following command to automatically test the app: ```./manage.py test --pattern="tests_*.py" ```

## Resources

### Datasets

A combination of these datasets:
- [dataset 1](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
- [dataset 2](https://www.kaggle.com/datasets/thomasdubail/brain-tumors-256x256/data)
- [dataset 3](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset?rvi=1)

Steps taken to clean the dataset:
1. Duplicates were removed. 
2. Files automatically renamed. 
3. Images were shuffled.
4. Images were split between training and testing (0.80/0.20).

## Disclamer

This project is built for training and learning purposes, do not use it for real use cases.