# config work wich needs updation in src configuration.py
from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories
from CNN_Classifier.entity.config_entity import DataIngestionConfig, NovelBaseModelConfig


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_PATH,
            params_filepath=PARAMS_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_novel_base_model_config(self) -> NovelBaseModelConfig:
        config = self.config.novel_base_model

        create_directories([config.root_dir])

        novel_base_model_config = NovelBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            update_base_model_path=Path(config.updated_base_model_path),
            param_image_size=self.params.IMAGE_SIZE,
            param_learning_rate=self.params.LEARNING_RATE,
            param_include_top=self.params.INCLUDE_TOP,
            param_weights=self.params.WEIGHTS,
            param_classes=self.params.CLASSES
        )

        return novel_base_model_config
