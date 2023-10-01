"""
This module contains the main entry point for the Cogniezer backend application.
"""

from Cogniezer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cogniezer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Cogniezer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Cogniezer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from Cogniezer.logging import logger
from Cogniezer.pipeline.stage_05_model_evaluaution import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")


STAGE_NAME = "Data Validation State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")


STAGE_NAME = "Data Transformation State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")


STAGE_NAME = "Model Training State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")


STAGE_NAME = "Model Evaluation State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")