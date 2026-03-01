from pathlib import Path
from ..utils.helpers import ensure_dir


def run(settings):
    ensure_dir(settings.input_dir)
    ensure_dir(settings.output_dir)
    ensure_dir(settings.logs_dir)

    print("Project structure initialized.")
    return 0