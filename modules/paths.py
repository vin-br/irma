"""Project-wide path constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Backend directories
BACKEND_DIR = PROJECT_ROOT / "backend"

# Frontend directories
FRONTEND_DIR = PROJECT_ROOT / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"

# Models and metadata
MODELS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODELS_DIR / "ResNet50V2-32.keras"
CLASSES_PATH = MODELS_DIR / "classes.json"

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
BRAIN_DATASET_DIR = DATA_DIR / "brain_dataset"
COMBINED_DIR = DATA_DIR / "combined"

TRAINING_DATASET = BRAIN_DATASET_DIR / "training"
TESTING_DATASET = BRAIN_DATASET_DIR / "testing"
COMBINED_TRAINING_DATASET = COMBINED_DIR / "training"
COMBINED_TESTING_DATASET = COMBINED_DIR / "testing"


def verify_paths() -> None:
    """Ensure core directories/files exist before depending on them."""
    required_dirs = {
        "PROJECT_ROOT": PROJECT_ROOT,
        "BACKEND_DIR": BACKEND_DIR,
        "FRONTEND_DIR": FRONTEND_DIR,
        "TEMPLATES_DIR": TEMPLATES_DIR,
        "STATIC_DIR": STATIC_DIR,
        "BRAIN_DATASET_DIR": BRAIN_DATASET_DIR,
        "COMBINED_DIR": COMBINED_DIR,
        "TRAINING_DATASET": TRAINING_DATASET,
        "TESTING_DATASET": TESTING_DATASET,
        "COMBINED_TRAINING_DATASET": COMBINED_TRAINING_DATASET,
        "COMBINED_TESTING_DATASET": COMBINED_TESTING_DATASET,
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
            "Missing required project paths. Create the expected structure before continuing:\n"
            f" - {details}"
        )


__all__ = [
    "PROJECT_ROOT",
    "BACKEND_DIR",
    "FRONTEND_DIR",
    "TEMPLATES_DIR",
    "STATIC_DIR",
    "MODELS_DIR",
    "MODEL_PATH",
    "CLASSES_PATH",
    "DATA_DIR",
    "BRAIN_DATASET_DIR",
    "COMBINED_DIR",
    "TRAINING_DATASET",
    "TESTING_DATASET",
    "COMBINED_TRAINING_DATASET",
    "COMBINED_TESTING_DATASET",
    "verify_paths",
]
