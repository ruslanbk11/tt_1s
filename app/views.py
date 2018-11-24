from flask import request, abort, jsonify, render_template
import app.model as model
from app import app

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
@app.route('/')
def index(name='world'):
    return "Hello, {}!".format( name )

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return """<html><head></head><body>
        <form method="POST" action="/form/">
            <input name="first_name">
            <input name="last_name">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        rv = jsonify( request.form )
        return rv
        abort(404)

@app.route('/messages/')
def messages():
    chat_id = int(request.args.get('chat_id'))
    if type(request.args.get('limit')) == type(str):
        limit = int(request.args.get('limit'))
        messages = model.list_messages_by_chat(chat_id, limit)
    else:
        messages = model.list_messages_by_chat(chat_id)
    return jsonify(messages)

@app.route('/search_users/', methods=['GET'])
def search_user():    
    word = request.args.get('word')
    users = model.search_users(word)
    return jsonify(users)

@app.route('/list_chats/', methods=['GET'])
def list():
    user_id = request.args.get('user_id')
    list_of_chats = model.list_chats(user_id)
    return jsonify(list_of_chats)

@app.route('/create_pers_chat/', methods=['GET', 'POST'])
def create_pers_chat():
    user_id = 2
    if request.method == 'GET':
        return render_template('create_pers_chat.html')
    if request.method == 'POST':
        print(request.form)
        companion_id = int(request.form['companion_id'])
        rv = model.create_pers_chat(user_id, companion_id)
        return jsonify(rv)
    
