from authlib.flask.client import OAuth
from flask import Flask
from .instance.config import *
from flask_jsonrpc import JSONRPC
#import boto3

app = Flask(__name__)
app.config.from_object(TestingConfig)
jsonrpc = JSONRPC( app, '/')

oauth = OAuth(app)
oauth.register('vk',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token_url='https://oauth.vk.com/access_token',
        access_token_method='POST',
        refresh_token_url=None,
        authorize_url='https://oauth.vk.com/authorize',
        api_base_url='https://api.vk.com/method/',
        client_kwargs={'scope': 'user_id email', 'response_type': 'code',
                       'v': 5.87, 'display': 'page'
                      },
    )

#s3_session = boto3.session.Session()
#s3_client = s3_session.client(service_name='s3',
#                              endpoint_url=S3_ENDPOINT_URL,
#                              aws_access_key_id=S3_ACCESS_KEY_ID,
#                              aws_secret_access_key=S3_SECRET_ACCESS_KEY)

from .views import *
