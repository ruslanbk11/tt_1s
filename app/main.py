import json
import datetime


def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-Type', 'application/json') ]
    time = str(datetime.datetime.now().time())
    url = environ['RAW_URI']
    body = (json.dumps({'time': time, 'url': url})).encode('utf-8')
    start_response(status, headers)
    return [ body ]

