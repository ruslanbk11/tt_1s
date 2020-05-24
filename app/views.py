from flask import url_for, request, redirect, json, abort, jsonify, render_template
import app.model as model
import requests
from app import app, jsonrpc, oauth
from .instance.config import CLIENT_ID, CLIENT_SECRET
from .utils import is_authorized

session = {'user_id': None, 'access_token': None}

#@jsonrpc.method('api.upload_file')
#def upload_file(b64content, filename):
#    content = base64.b64decode(b64content).('utf-8')
#    s3_client.put_object(Bucket = config.S3_BUCKET_NAME, Key=filename, Body=content)
#    return b64content
#
#@jsonrpc.method('api.download_file')
#def download_file(filename):
#    response = s3_client.get_object(Bucket=config.S3_BUCKET_NAME, Key=filename)
#    print( response, dir(response))
#    return response
#

@app.route('/login/')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.vk.authorize_redirect(redirect_uri)

@app.route('/authorize/')
def authorize():
    redirect_uri = url_for('authorize', _external=True)
    code = request.args.get('code')
    cid = CLIENT_ID
    csecret = CLIENT_SECRET
    resp = requests.get(
            f'https://oauth.vk.com/access_token?client_id={cid}&client_secret={csecret}&redirect_uri={redirect_uri}&code={code}&access_type=offline')
    json_ = json.loads(resp.content)
    print(CLIENT_ID, CLIENT_SECRET)
    session['access_token'] = json_['access_token']
    print(json_)
    session['user_id'] = json_['user_id']
    new_user = model.create_user(str(json_['user_id']))
    return redirect('/')

@app.route('/profile/')
def profile():
    resp = oauth.vk.get('account/verify_credentials.json')
    profile = resp.json()
    return profile

@jsonrpc.method('list_chats(user_id=Number) -> Object', validate=True)
def chats(user_id):
#    import ipdb
#    ipdb.set_trace()
    chats = model.list_chats(user_id)
    return jsonify(chats)


@jsonrpc.method('search_users(word=String, limit=Number) -> Object', validate=True)
def search_users(word, limit):
    users = model.search_users(word, limit)
    return jsonify(users)


@jsonrpc.method('create_pers_chat(user_id=Number, companion_id=Number) -> Object', validate=True)
def create_pers_chat(user_id, companion_id):
    
    rv = model.create_pers_chat(user_id, companion_id)
    return jsonify(rv)


@jsonrpc.method('send_message(user_id=Number, chat_id=Number, content=String) -> Object', validate=True)
def send_message(user_id, chat_id, content):
    rv = model.send(user_id, chat_id, content)
    return jsonify(rv)


@jsonrpc.method('list_messages(chat_id=Number, limit=Number) -> Object', validate=True)
def list_messages(chat_id, limit):
    rv = model.list_messages_by_chat(chat_id, limit)
    return jsonify(rv)


@jsonrpc.method('read_message(user_id=Number, message_id=Number) -> Object', validate=True)
def read(user_id, message_id):
    rv = model.read(user_id, message_id)
    return jsonify(rv)
