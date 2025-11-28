from pathlib import Path

# Root and application directories
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Backend directories
BACKEND_DIR = PROJECT_ROOT / "backend"

# Frontend directories
FRONTEND_DIR = PROJECT_ROOT / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"

# Paths to model and classes files
MODEL_PATH = PROJECT_ROOT / "models" / "ResNet50V2-32.keras"
CLASSES_PATH = PROJECT_ROOT / "models" / "classes.json"


def verify_paths() -> None:
    """Ensure expected directories/files exist before the app starts."""
    required_dirs = {
        "PROJECT_ROOT": PROJECT_ROOT,
        "BACKEND_DIR": BACKEND_DIR,
        "FRONTEND_DIR": FRONTEND_DIR,
        "TEMPLATES_DIR": TEMPLATES_DIR,
        "STATIC_DIR": STATIC_DIR,
    }
    required_files = {
        "MODEL_PATH": MODEL_PATH,
        "CLASSES_PATH": CLASSES_PATH,
    }

    missing = []

    for name, path in required_dirs.items():
        if not path.is_dir():
            missing.append(f"{name} -> {path}")

    for name, path in required_files.items():
        if not path.is_file():
            missing.append(f"{name} -> {path}")

    if missing:
        details = "\n - ".join(missing)
        raise FileNotFoundError(
            "Missing required project paths. Create the expected structure before starting the server:\n"
            f" - {details}"
        )
