"""
Convert image objects to JPG after uploading to s3
"""

import logging
import wand


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    """
    Lambda handler
    """
    logger.info("%s - %s", event, context)

    
    return event
