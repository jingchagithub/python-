#coding:utf-8
"""
配合爬虫脚本写的mysql读写脚本
"""
import pymysql,logging
class mysql(object):
    def __init__(self,user,passwd,db,host="127.0.0.1",port=3306,):
        self.coon=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset="utf8")
        self.db=self.coon.cursor()
    def insert(self,datalist):
      try:
       for q in datalist:
         for text in q:
            sql="insert into text(url,text) values('{text}')".format(text=text)
            print sql
            self.db.execute(sql)
            self.coon.commit()
      except Exception as e:
          print e
          return

    def select(self):
        try:
            sql="select text from text"
            self.db.execute(sql)
            a=self.db.fetchall()
            q=[ g for g in a]
            t=[]
            for s in q:
               t.append(s[0])
               print s[0]
        except AssertionError as e:
            logging.info("错误")
            return None
    def __del__(self):
        self.coon.close()
logging.basicConfig(level=logging.INFO)
mysql=mysql(user="root",passwd="root",db="html")
mysql.select()