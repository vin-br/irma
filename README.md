# ARC

AI Radiology Copilot (ARC) is a web-based app to detect brain tumors from MRI images using a Convolutional Neural Network (CNN) model. 

## Installation Instructions

```pyenv install 3.11.6```

```pyenv global 3.11.6```

- cd to the project directory.

```python -m venv .venv```

```source /bin/activate/venv (for Windows)```

```source venv/bin/activate (for macOS)```

```pip install -r requirements.txt```

If the requirements file does not work or is unavailable:

```pip install Cython Pillow opencv-python torch torchvision pytest scipy matplotlib mock tqdm imageai django```
