# config work wich needs updation in src configuration.py
from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories, save_json
from CNN_Classifier.entity.config_entity import (DataIngestionConfig,
                                                 NovelBaseModelConfig,
                                                 TrainingConfig,
                                                 EvaluationConfig)
import os

os.environ["MLFLOW_TRACKING_URI"]= "https://dagshub.com/slackroo/kidney_disease_classification_deeplearning.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="slackroo"
os.environ["MLFLOW_TRACKING_PASSWORD"]="e383057a1f050e672c874aef175d897f88ad2ea2"

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
            updated_base_model_path=Path(config.updated_base_model_path),
            param_image_size=self.params.IMAGE_SIZE,
            param_learning_rate=self.params.LEARNING_RATE,
            param_include_top=self.params.INCLUDE_TOP,
            param_weights=self.params.WEIGHTS,
            param_classes=self.params.CLASSES
        )

        return novel_base_model_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.novel_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/kidney-ct-scan-image",
            mlflow_uri="https://dagshub.com/slackroo/kidney_disease_classification_deeplearning.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
