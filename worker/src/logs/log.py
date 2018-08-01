import logging
import os


def setup_logging():
    """Set up logging for both app and sqs consumer"""
    log_level = os.environ['LOG_LEVEL'] if os.environ.get('LOG_LEVEL') else 'INFO'
    logging.basicConfig(level=log_level, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
    return logging

logger = setup_logging()
