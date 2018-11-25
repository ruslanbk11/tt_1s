from flask import request, abort, jsonify, render_template
import app.model as model
from app import app, jsonrpc

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

@jsonrpc.method('list_chats(user_id=Number) -> Object', validate=True)
def chats(user_id):
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
