import sqlite3
import requests
import json
import time


class UsersDB:
    name = 'users.db'

    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = sqlite3.connect(self.name)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        self._db_cur.execute(query)
        self._db_connection.commit()
        return

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


def createTable():
    db = UsersDB()
    db.query('CREATE TABLE Users(user_id INTEGER PRIMARY KEY UNIQUE NOT NULL, first_name TEXT, last_name TEXT, sex INTEGER, bdate TEXT, country INTEGER, city INTEGER, home_town INTEGER, followers_count INTEGER, relation INTEGER, last_update INTEGER NOT NULL);')


def getInfoList(vk_ip):
    t = requests.get(
        "https://api.vk.com/api.php?oauth=1&method=users.get&user_ids=%s&fields=sex,bdate,country,city,home_town,followers_count,relation" % vk_ip).text

    dic = json.loads(t)
    dic = dic['response']
    return dic


def addInfo(dicAll):
    for dic in dicAll:
        db = UsersDB()

        if len(db.fetch('Select * from Users where user_id = %d' % dic['uid'])) == 0:
            db.query('INSERT INTO Users(user_id, last_update) values(%d, %d)' % (dic['uid'], time.time()))

        res = {'sex': None, 'city': None, 'first_name': None, 'last_name': None, 'bdate': None, 'country': None,
               'uid': None, 'followers_count': None, 'home_town': None, 'relation': None}
        for key in dic:
            res[key] = dic[key]

        uid = res['uid']
        del res['uid']

        for key in res.keys():
            db.query('UPDATE users SET \'%s\'=\'%s\' WHERE user_id=\'%s\'' % (key, res[key], uid))
        db.query('UPDATE users SET last_update=\'%s\' WHERE user_id=\'%s\'' % (time.time(), uid))

    return


addInfo(getInfoList('kotelnikova_photo,dashanesuralmasha'))  # Вводить Id через запятую, например (id880055,id53535)
