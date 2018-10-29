from flask import Flask
from .instance.config import *


app = Flask(__name__)
app.config.from_object(TestingConfig)

from .views import *
