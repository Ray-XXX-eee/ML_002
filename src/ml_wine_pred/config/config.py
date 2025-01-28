from ml_wine_pred.constants import *
from ml_wine_pred.utils.common import read_yaml, create_dir
from ml_wine_pred.entity.entity_config import DataIngestionConfig
class ConfiguratioManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):
        
        print(config_filepath, params_filepath, schema_filepath)
        
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(params_filepath)
        self.params = read_yaml(schema_filepath)
        
        create_dir([self.config.artifacts_root])
        
    def get_data_ingestion_config (self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
        
