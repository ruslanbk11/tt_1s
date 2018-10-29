from flask import request, abort, jsonify

from app import app

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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

def do_the_login():
    pass

def show_the_login_form():
    pass

@app.route('/search_users/', methods=['GET'])
def search_user():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            query = str(args['query'])
            limit = int(args['limit'])
        
        user1 = {
                'user_id': 22,
                'nick': 'the.good',
                'name': 'Clint Eastwood',
                'avatar': 'avatars/cea.png'
                }

        user2 = {
                'user_id': 13,
                'nick': 'i_am_iron_man',
                'name': 'Tony Stark',
                'avatar': 'avatars/tsa.png'
                }

        resp = jsonify({'users': [user1, user2]})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp

@app.route('/search_chats/', methods=['GET'])
def search_chat():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            query = str(args['query'])
            limit = int(args['limit'])

        chat1 = {
                "chat_id": 33,
                "is_group_chat": False,
                "topic": "Chuck Norris",
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
                }
        chat2 = {
                "chat_id": 2,
                "is_group_chat": True,
                "topic": "Huck Dorris",
                "last_message": "hgra!",
                "new_messages": 3,
                "last_read_message_id": 14
                } 

        resp = jsonify({'chats': [chat1, chat2]})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp

@app.route('/list_chats/', methods=['GET'])
def list():
    if request.method == 'GET':
        chat1 = {
                "chat_id": 33,
                "is_group_chat": False,
                "topic": "Chuck Norris",
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
                }
        chat2 = {   
                "chat_id": 2,
                "is_group_chat": True,
                "topic": "Huck Dorris",
                "last_message": "hgra!",
                "new_messages": 3,
                "last_read_message_id": 14
                }
        resp = jsonify({'chats': [chat1, chat2]})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp

@app.route('/create_pers_chat/', methods=['GET', 'POST'])
def create_pers_chat():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            user_id = int(args['user_id'])
        chat = {
                "chat_id": 33,
                "is_group_chat": False,
                "topic": "Chuck Norris",
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
                }
        resp = jsonify({'chat': chat})
        resp.status_code = 200
        resp.content_type = 'application/json'
        return resp

    if request.method == 'POST':
        chat = {
                "chat_id": 33,
                "is_group_chat": False,
                "topic": "Chuck Norris",
                "last_message": "argh!",
                "new_messages": 30,
                "last_read_message_id": 214
                }
        resp = jsonify({'chat': chat})
        resp.status_code = 200
        resp.content_type = 'application/json'
        return resp
    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp

@app.route('/create_group_chat/', methods=['GET', 'POST'])
def create_group_chat():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            topic = str(args['topic'])
        chat = {
                "chat_id": 17,
                "is_group_chat": True,
                "topic": "Chuch Hobbis",
                "last_message": "Booom!",
                "new_messages": 2,
                "last_read_message_id": 4
                }

        resp = jsonify({'chat': chat})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

    if request.method == 'POST':
        chat = {
                "chat_id": 17,
                "is_group_chat": True,
                "topic": "Chuch Hobbis",
                "last_message": "Booom!",
                "new_messages": 2,
                "last_read_message_id": 4
                }
    
        resp = jsonify({'chat': chat})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp

@app.route('/add_members_to_group_chat/', methods=['GET', 'POST'])
def add_member_to_group_chat():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            chat_id = int(args['chat_id'])
            user_ids = args['user_ids']
        resp = jsonify({})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

    if request.method == 'POST':
        resp = jsonify({})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

@app.route('/leave_group_chat/', methods=['GET', 'POST'])
def leave_group_chat():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            chat_id = int(args['chat_id'])
        resp = jsonify({})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

    if request.method == 'POST':
        resp = jsonify({})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

@app.route('/send_message/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            chat_id = int(args['chat_id'])
            content = str(args['content'])
            attach_id = int(args['attach_id'])
        message = {
                   "message_id": 200,
                   "chat_id": 33,
                   "user_id": 22,
                   "content": "Hmmm, @chuck.norris",
                   "added_at": 1540198594
                  }
        resp = jsonify({'message': message})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    if request.method == 'POST':
        message = {
                   "message_id": 200,
                   "chat_id": 33,
                   "user_id": 22,
                   "content": "Hmmm, @chuck.norris",
                   "added_at": 1540198594
                  }
        resp = jsonify({'message': message})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
@app.route('/read_message/', methods=['GET'])
def read_message():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            message_id = int(args['message_id'])
        chat = {
                "chat_id": 17,
                "is_group_chat": True,
                "topic": "Chuch Hobbis",
                "last_message": "Booom!",
                "new_messages": 2,
                "last_read_message_id": 4
                }
        resp = jsonify({'chat': chat})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({})
        resp.status_code = 404
        return resp
@app.route('/upload_file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        args = request.args.to_dict()
        if args:
            chat_id = int(args['chat_id'])
            content = str(args['content'])
        attach = {
                  "attach_id": 1,
                  "message_id": 200,
                  "chat_id": 33,
                  "user_id": 22,
                  "type": "image",
                  "url": "attach/e7ed63c5f815d5b308c9a3720dd1949d.png"
                 }
        resp = jsonify({'attach': attach})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp
    if request.method == 'POST':
        attach = {
                  "attach_id": 1,
                  "message_id": 200,
                  "chat_id": 33,
                  "user_id": 22,
                  "type": "image",
                  "url": "attach/e7ed63c5f815d5b308c9a3720dd1949d.png"
                 }
        resp = jsonify({'attach': attach})
        resp.content_type = 'application/json'
        resp.status_code = 200
        return resp

