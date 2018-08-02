#!/usr/bin/env python3

import boto3
import os
from logs.log import logger
from wand.image import Image
from wand.color import Color

class Worker:
    s3_bucket = None
    s3_key = None
    def __init__(self, options):
        self.options = options
        self.s3_bucket = os.environ["S3_BUCKET"]
        self.s3_key = os.environ["S3_KEY"]


    def convert(self):
        with Image(filename='glyph.pdf') as img:
            img.format = 'jpeg'
            img.background_color = Color('white')
            img.alpha_channel = 'remove'
            img.save(filename='/output_dir/glyph.jpg')

    def run(self):
        logger.info("bucket: {} key: {}".format(self.s3_bucket, self.s3_key))
        self.convert()


Worker({}).run()
