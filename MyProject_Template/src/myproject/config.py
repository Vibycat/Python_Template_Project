from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    project_root: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = project_root / "data"
    input_dir: Path = data_dir / "input"
    output_dir: Path = data_dir / "output"
    logs_dir: Path = project_root / "logs"