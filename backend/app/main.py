"""FastAPI Back-end Migration."""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .paths import STATIC_DIR, TEMPLATES_DIR, verify_paths

verify_paths()

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

app = FastAPI(title="ARC FastAPI")

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request) -> HTMLResponse:
    """Render the landing page with placeholder context."""
    context = {
        "request": request,
        "prediction": None,
        "probability": None,
        "prediction_made": False,
        "annotated_image": None,
        "yolo": False,
        "messages": [],
    }
    return templates.TemplateResponse("index.html", context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
