from conf import settings
import json

def conn_db():
    db_path = settings.DB_PATH
    dic = json.load(open(db_path, 'r', encoding='utf-8'))
    return dic

def save_db(dic):
    db_path = settings.DB_PATH
    json.dump(dic, open(db_path, 'w', encoding='utf-8'))