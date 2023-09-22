"""
This module contains the main entry point for the Cogniezer backend application.
"""

from Cogniezer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cogniezer.logging import logger

STAGE_NAME = "Data Ingestion State"

try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> Stage : {STAGE_NAME} completed <<<<<\n\n>>>>>>>  <<<<<<<")
except Exception as error:
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<")
    logger.error(error)
    logger.error(f">>>>> Stage : {STAGE_NAME} failed <<<<<\n\n>>>>>>>  <<<<<<<")    
