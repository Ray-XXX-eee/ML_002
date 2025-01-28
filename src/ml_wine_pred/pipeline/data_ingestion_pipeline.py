from ml_wine_pred.config.config import ConfiguratioManager
from ml_wine_pred.components.data_ingestion import DataIngestion
from ml_wine_pred import logger

STAGE_NAME = 'Data ingestion stage'
class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfiguratioManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        # data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f"<<< Stage {STAGE_NAME} started >>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"<<< Stage {STAGE_NAME} ended >>>")    
    except Exception as e:
        raise e
        