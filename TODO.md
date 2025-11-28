# FastAPI Migration To-Do List

## Backend implementation

- [ ] Install base dependencies
  - [ ] `pip install --upgrade pip`
  - [ ] `pip install "fastapi[standard]" uvicorn python-multipart jinja2`
  - [ ] `pip install keras tensorflow numpy pillow`

- [ ] Set up a FastAPI app
    - [ ] Create a legacy folder, move Django app into it and rename current Django folder `app/` to `django_app/`
	- [ ] Create `fastapi_app/main.py` with a FastAPI `app`
	- [ ] Add `GET /` that renders `app/templates/index.html`
	- [ ] Add a run command: `uvicorn fastapi_app.main:app --reload`

- [ ] Move the prediction logic
	- [ ] Load the Keras model once on startup from `models/ResNet50V2-32.keras`
	- [ ] Load classes from `models/classes.json`
	- [ ] Accept image upload on `POST /` (or `/predict`) using `UploadFile`
	- [ ] Read image bytes in memory, run prediction, compute class + probability
	- [ ] If tumor, call `models/yolo.py:annotate_image` and base64 the result
	- [ ] Return the template with: `prediction`, `probability`, `prediction_made`, `annotated_image`, `yolo`

- [ ] Make the template work with Jinja2
	- [ ] Remove `{% load static %}` and `{% csrf_token %}` from `index.html`
	- [ ] Replace static link with `/static/assets/css/style.css`
	- [ ] Drop Django messages; show a simple error text when no file

- [ ] Serve static files
	- [ ] Mount `/static` to `app/static`

- [ ] Simplify settings/paths
	- [ ] Stop using Django settings
	- [ ] Keep paths as simple constants or read from `.env`
	- [ ] Use project-root relative paths for models and media

- [ ] Update dependencies
	- [ ] Freeze current packages: `pip freeze > requirements.txt`
	- [ ] Check that there is at least: `fastapi`, `uvicorn[standard]`, `python-multipart`, `jinja2`, `keras`, `tensorflow`, `numpy`, `pillow`

- [ ] Clean up and docs
	- [ ] Update `README.md` with new run commands
	- [ ] After FastAPI works, remove Django files: `manage.py`, `irma/`, `app/admin.py`, `app/apps.py`, `app/urls.py`, old Django tests
	- [ ] Keep `app/templates/` and `app/static/` as-is

## Testing

- [ ] Rewrite tests
	- [ ] Use `pytest` + `fastapi.testclient`
	- [ ] Test: `GET /` returns 200; unknown path returns 404
	- [ ] Test: `POST` without file shows an error
	- [ ] (Optional) Mock the model for a fast prediction test
