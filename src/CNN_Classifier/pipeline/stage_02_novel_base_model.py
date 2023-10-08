from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.novel_base_model import NovelBaseModel
from CNN_Classifier import logger

STAGE_NAME = "Novel base model"

class NovelBaseModelTrainingPipeline:
    def __int__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        novel_base_model_config = config.get_novel_base_model_config()
        novel_base_model = NovelBaseModel(config=novel_base_model_config)
        novel_base_model.get_base_model()
        novel_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = NovelBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e