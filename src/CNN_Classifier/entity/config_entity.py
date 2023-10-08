# entity is return type of a function
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class NovelBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    update_base_model_path: Path
    param_image_size: list
    param_learning_rate: float
    param_include_top: bool
    param_weights: str
    param_classes: int