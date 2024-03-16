# ARC

AI Radiology Copilot (ARC) is a web-based app to detect brain tumors from MRI images using a Convolutional Neural Network (CNN) model. 

## Installation Instructions

```pyenv install 3.11.6```

```pyenv global 3.11.6```

- cd to the project directory.

```python -m venv .venv```

```source /bin/activate/.venv (for Windows)```

```source .venv/bin/activate (for macOS)```

```pip install -r requirements.txt```

If the requirements file does not work or is unavailable:

```pip install pandas matplotlib seaborn django scikit-learn keras tensorflow scipy Cython Pillow opencv-python torch torchvision pytest mock tqdm imageai```

## Django Server Setup

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```

## Testing Instructions

### Unit Tests

```./manage.py test --pattern="tests_*.py" ```

## Resources

### Datasets

Combined these datasets:
- [dataset 1](https://www.kaggle.com/datasets/thomasdubail/brain-tumors-256x256)
- [dataset 2](https://www.kaggle.com/datasets/thomasdubail/brain-tumors-256x256/data)
- [dataset 3](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset?rvi=1)

Steps taken to clean the dataset:
1. Duplicates were removed. 
2. Files automatically renamed. 
3. Images were shuffled.
4. Images were split between training and testing (0.80/0.20).
