import app.db as db
import json
import datetime

def list_messages_by_chat(chat_id, limit):
    return db.query_all("""
            SELECT user_id, nick, name, message_id, content, added_at
            FROM messages
            JOIN users USING (user_id)
            WHERE chat_id = %(chat_id)s
            ORDER BY added_at DESC
            LIMIT %(limit)s
            """, chat_id = int(chat_id), limit = int(limit))

def search_users(word, limit):    
    return db.query_all("""
            SELECT nick, name, avatar
            FROM users
            WHERE nick=%(word)s OR name=%(word)s
            LIMIT %(limit)s
            """, word = word, limit = int(limit))

def get_chat_ids(user_id):
    ids = []
    chats_where_member = db.query_all('''
        select chat_id from members
        where user_id = %(user_id)s
        ''', user_id = int(user_id))
    print(chats_where_member)
    for key, value in chats_where_member.items():
        ids.append(value['chat_id'])
    print('ids:', ids)
    return ids
    
def list_chats(user_id):
    chats = []
    ids = get_chat_ids(user_id)
#    import ipdb; ipdb.set_trace()
    for chat_id in ids:
        chats.append(db.query_one('''
            select * from chats
            where chat_id = %(chat_id)s
            ''', chat_id=chat_id))
    print(chats)
    return chats

def create_new_chat():
    return db.create('''
        insert into chats (is_group_chat, topic, last_message)
        values ( 0, '', NULL)
        returning chat_id
        ''')

def create_pers_chat(user_id1, user_id2):
    chat_ids1 = set(get_chat_ids(user_id1))
    chat_ids2 = set(get_chat_ids(user_id2))
    matches = list(chat_ids1 & chat_ids2)
    if not matches:
        last_id = create_new_chat()
        db.insert('''
            insert into members (user_id, chat_id, new_messages, last_read_message_id)
            values (%(user_id1)s, %(last_id)s, 0, NULL)
            ''', user_id1 = user_id1, last_id = last_id)
        db.insert('''
            insert into members (user_id, chat_id, new_messages, last_read_message_id)
            values (%(user_id2)s, %(last_id)s, 0, NULL)
            ''', user_id2 = user_id2, last_id = last_id)
        return 'OK'
    else:
        id = matches[0]
        return db.query_one('''
            select * from chats
            where chat_id=%(chat_id)s
            and is_group_chat=0
            ''', chat_id = id)

def create_new_message(user_id, chat_id, content):
    return db.create('''
        insert into messages (user_id, content, chat_id)
        values (%(user_id)s, %(content)s, %(chat_id)s)
        returning message_id
        ''', user_id = user_id, chat_id = chat_id, content = content)

def send(user_id, chat_id, content):
    last_message_id = create_new_message(user_id, chat_id, content)
    db.insert('''
        update chats
        set last_message=%(content)s
        where chat_id=%(chat_id)s
        ''', content=content, chat_id=chat_id)
    db.insert('''
        update members
        set new_messages=new_messages+1
        where chat_id=%(chat_id)s
        and user_id<>%(user_id)s
        ''', chat_id=chat_id, user_id=user_id)
#    db.insert('''
#        update chats
#        set new_messages=new_messages+1
#        where chat_id=%(chat_id)s
#        ''', chat_id=chat_id, user_id=user_id)
    message = {
            'message_id': last_message_id,
            'user_id': user_id,
            'content': content,
            'added_at': str(datetime.datetime.time(datetime.datetime.now())),
            'chat_id': chat_id
    }
    return message

def read(user_id, message_id):
    target_chat = db.query_one("""
        SELECT chat_id FROM messages
        WHERE message_id = %(message_id)s
        """, message_id = message_id)
    chat_id = target_chat['chat_id']

    db.insert("""
        UPDATE members
        SET new_messages = new_messages - 1,
        last_read_message_id = %(message_id)s
        WHERE user_id = %(user_id)s
        AND chat_id = %(chat_id)s
        """, user_id = user_id, chat_id = chat_id, message_id = message_id)

    return db.query_one("""
        SELECT * FROM chats
        WHERE chat_id = %(chat_id)s
        """, chat_id = chat_id)

