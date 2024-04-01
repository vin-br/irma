# ARC

AI Radiology Copilot (ARC) is a web-based app to detect brain tumors from MRI images using a Convolutional Neural Network (CNN) model. 

## Installation Instructions

```pyenv install 3.11.6```

2. Set the Python version as either local or global: ```pyenv local 3.11.6``` or ```pyenv global 3.11.6```

3. `cd` to move to the project's root directory.

4. Create a virtual environment: ```python -m venv .venv```

5. Activate the virtual environment on linux or macOS: ```source .venv/bin/activate```

6. Upgrade pip to the latest version: ```python -m pip install --upgrade pip```

7. Install the packages with either the requirements or the individual list provided if the requirements fail to install: ```pip install -r requirements.txt``` or ```pip install ipykernel numpy pandas plotly torch torchvision django```

## Starting the app

- Use Django's runserver command to start the project once it has been installed: ```python manage.py runserver```.

- You should not need to makemigration using ```python manage.py makemigrations``` or migrate with ```python manage.py migrate``` since the project does not currently use a database. 

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