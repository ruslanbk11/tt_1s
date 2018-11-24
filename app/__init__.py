from flask import Flask
from .instance.config import *
from flask_jsonrpc import JSONRPC
#import boto3

app = Flask(__name__)
app.config.from_object(TestingConfig)
jsonrpc = JSONRPC( app, '/api')

#s3_session = boto3.session.Session()
#s3_client = s3_session.client(service_name='s3',
#                              endpoint_url=config.S3_ENDPOINT_URL,
#                              aws_access_key_id=config.S3_ACCESS_KEY_ID,
#                              aws_secret_access_key=config.S3_SECRET_ACCESS_KEY)

from .views import *
