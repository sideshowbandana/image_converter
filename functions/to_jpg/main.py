"""
Convert image objects to JPG after uploading to s3
"""

import logging
import boto3


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    """
    Lambda handler
    """
    logger.info("%s - %s", event, context)
    client = boto3.client('ecs')

    s3 = event['Records'][0]['s3']
    src_bucket = s3['bucket']['name']
    src_key = s3['object']['key']
    logger.info("%s - %s", src_bucket, src_key)

    response = client.run_task(
        cluster='image-converter-cluster', # name of the cluster
        launchType = 'FARGATE',
        taskDefinition='image-converter-task:2', # replace with your task definition name and revision
        count = 1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-0f22a76b', # replace with your public subnet or a private with NAT
                    'subnet-4c82b740' # Second is optional, but good idea to have two
                ],
                'securityGroups': [
                    'sg-0bd7f141' # security group assigned to the task
                ],
                'assignPublicIp': 'ENABLED'
            }
        })
    return str(response)
