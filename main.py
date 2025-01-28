from ml_wine_pred import logger
logger.info('Log test main')

from ml_wine_pred.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = 'Data ingestion stage'
try:
    logger.info(f"<<< Stage {STAGE_NAME} started >>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"<<< Stage {STAGE_NAME} ended >>>")    
except Exception as e:
    raise e