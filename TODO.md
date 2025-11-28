# FastAPI Migration To-Do List

---

## Backend implementation

- [x] Install base dependencies
  - [x] Install Python 3.13.9 with pyenv instead of 3.14.0 to have better package support for TensorFlow
  - [x] Update pip and install base packages

- [x] Set up a basic FastAPI app
    - [x] Create a legacy folder, move Django app into it and rename current Django folder `app/` to `django_app/`
	- [x] Create `backend/app/main.py` with a FastAPI `app`
	- [x] Add `GET /` that renders `frontend/templates/index.html`
	- [x] Add a run command: `uvicorn backend.app.main:app --reload`

- [x] Serve static files
	- [x] Mount `/static` to `app/static`

- [x] Simplify settings/paths
	- [x] Stop using Django settings
	- [x] Keep paths as simple constants in a separate `paths.py` file
	- [x] Use project-root relative paths for model files, templates, static files, datasets

- [x] Update dependencies
	- [x] Freeze current packages: `pip freeze > requirements.txt`
	- [x] Check that there is at least: `fastapi`, `uvicorn[standard]`, `python-multipart`, `jinja2`, `torch`, `torchvision`, `pillow`

- [ ] Move the prediction logic once the move to PyTorch is done since Keras 2.15 is not compatible with Python 3.14 and latest Keras/TensorFlow requires a major code rewrite too
	- [ ] Load the PyTorch model once on startup
	- [ ] Load classes from `models/classes.json`
	- [ ] Accept image upload on `POST /` (or `/predict`) using `UploadFile`
	- [ ] Read image bytes in memory, run prediction, compute class + probability
	- [ ] If tumor, call `models/yolo.py:annotate_image` and base64 the result
	- [ ] Return the template with: `prediction`, `probability`, `prediction_made`, `annotated_image`, `yolo`

- [ ] Clean up and docs
	- [ ] Update `README.md` with new run commands
	- [ ] After FastAPI works, remove Django files: `manage.py`, `irma/`, `app/admin.py`, `app/apps.py`, `app/urls.py`, old Django tests

---

## Frontend basic improvements

- [x] Create a `frontend` folder for the Jinja2 templates and static files
- [x] Configure Jinja2 templates
	- [x] Remove `{% load static %}` and `{% csrf_token %}` from `index.html`
	- [x] Replace static links with `/static/` paths
	- [x] Drop Django messages; show a simple error text when no file

---

## Testing

- [ ] Rewrite tests
	- [ ] Use `pytest` + `fastapi.testclient`
	- [ ] Test: `GET /` returns 200; unknown path returns 404
	- [ ] Test: `POST` without file shows an error
	- [ ] (Optional) Mock the model for a fast prediction test
