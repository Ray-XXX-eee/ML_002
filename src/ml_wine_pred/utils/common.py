import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ml_wine_pred import logger
from ensure import ensure_annotations
import os
from pathlib import Path


@ensure_annotations
def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return ConfigBox(data)
    except BoxValueError:
        raise('Error in reading yaml file : empty')
    except Exception as e:
        raise e
        
    return data

@ensure_annotations
def create_dir(path_list: list):
    '''
    Create list of dirs
    Args : 
        path_list (list): 
        verbos (bool, optional):
    '''
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        # if verbose:
        #     logger.info(f'created dir at path: {path}')
    

def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path))
    return f"(size is {size_in_kb} kb)"