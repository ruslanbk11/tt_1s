import app.db as db
import json

def list_messages_by_chat(chat_id, limit = 10):
    return db.query_all("""
            SELECT user_id, nick, name, message_id, content, added_at
            FROM messages
            JOIN users USING (user_id)
            WHERE chat_id = %(chat_id)s
            ORDER BY added_at DESC
            LIMIT %(limit)s
            """, chat_id = int(chat_id), limit = int(limit))

def search_users(word, limit = 10):
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
    for key, value in chats_where_member.items():
        ids.append(value['chat_id'])
    return ids
    
def list_chats(user_id):
    chats = {}
    ids = get_chat_ids(user_id)
    for index, chat_id in enumerate(ids):
        chats.update({index: db.query_one('''
            select * from chats
            where chat_id = %(chat_id)s
            ''', chat_id=int(chat_id))})
    return chats

def create_new_chat():
    return db.create('''
        insert into chats (is_group_chat, topic, last_message)
        values (false, '', '')
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
            values (%(user_id1)s, %(last_id)s, 0, 0)
            ''', user_id1 = user_id1, last_id = last_id)
        db.insert('''
            insert into members (user_id, chat_id, new_messages, last_read_message_id)
            values (%(user_id2)s, %(last_id)s, 0, 0)
            ''', user_id2 = user_id2, last_id = last_id)
        return 'OK'
    else:
        id = matches[0]
        return db.query_one('''
            select * from chats
            where chat_id = %(chat_id)s
            and is_group_chat = false
            ''', chat_id = id)

