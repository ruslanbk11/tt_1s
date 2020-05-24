import flask
import psycopg2, psycopg2.extras
import app.instance.config as config
from app import app

def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            database=config.DB_NAME, host=config.DB_HOST,
            user=config.DB_USER, password=config.DB_PASS
        )
    return flask.g.dbconn

def get_cursor():
    return get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)

def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return dict(cur.fetchone())

def query_all(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        answer = {}
        result = cur.fetchall()
        for index, el in enumerate(result):
            answer.update({index: dict(el)})
        return answer

def _rollback_db(sender, exception, *extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')

flask.got_request_exception.connect(_rollback_db, app)

def _commit_db(sender, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.commit()
        conn.close()
        delattr(flask.g, 'dbconn')

flask.request_finished.connect(_commit_db, app)

def insert(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return True

def create(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        new_id = cur.fetchone()[0]
        return new_id

