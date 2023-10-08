from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_novel_base_model import NovelBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from CNNClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data_Ingestion_stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Novel base model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    novel_base_model = NovelBaseModelTrainingPipeline()
    novel_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e