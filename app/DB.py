#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio
# Wrapper Database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class Database:

    def __init__(self,host='localhost',port=3306,db='mysql',user='root',pw='',charset='utf-8'):
        self._host = host
        self._port = port
        self._db = db
        self._user = user
        self._pw = pw
        self._charset = charset
        self._db_url = self._gen_db_conf()


    def _gen_db_conf(self):
        db_url = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' % \
                 (self._user,self._pw,self._host,self._port,self._db,self._charset)
        return db_url


    def db_session(self):
        self.db_engine = create_engine(self._db_url, encoding=self._charset, echo=False)
        return scoped_session(sessionmaker(bind=self.db_engine))
