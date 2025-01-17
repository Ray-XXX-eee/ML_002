import os
import sys
import logging

logging_str = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s]'
logging_dir = 'logs'
log_filepath = os.path.join(logging_dir, 'ml_002-wine_pred.log')
os.makedirs(logging_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)])

logger = logging.getLogger('ml002_logger')



