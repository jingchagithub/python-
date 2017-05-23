#coding:utf-8
"""
配合爬虫脚本写的mysql读写脚本
"""
import pymysql,logging,re,simplebayes,jieba
class mysqldb(object):
    def __init__(self,user,passwd,db,host="127.0.0.1",port=3306,):
        self.coon=pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset="utf8")
        self.db=self.coon.cursor()

    def insert(self,data,name):
      try:
            for text in data:
             string = re.sub("[\s+\.\!\/_,$%^*(+\"\'|]+|[+——！，。？、~@#￥%……&*（）|]+".decode("utf8"), "".decode("utf8"),text)
             sql="insert into shouji(text,name) values('{text}','{name}')".format(name=name,text=string.encode("utf-8"))


             self.db.execute(sql)
             self.coon.commit()
      except Exception as e:

          return

    def select(self,text,name):
        try:
            sql="select {text} from shouji where name={name}".format(text=text,name=name)
            self.db.execute(sql)
            a=self.db.fetchall()
            return a
        except AssertionError as e:
            return None
    def selects(self,name,lei):
        try:
            sql="select text from shouji WHERE NAME={name} AND lei={lei}".format(name=name,lei=lei)
            self.db.execute(sql)
            a=self.db.fetchall()
            return a
        except AssertionError as e:
            return None
    def __del__(self):
        self.coon.close()
    def fenlei(self,leiname,datas,xunlianzu):


        beiye=simplebayes.SimpleBayes(tokenizer=None,cache_path='C:\Documents and Settings\Administrator\PycharmProjects\python-\.idea\\tmp\\')
        beiye.cache_file="simplebayes.pickle"

        for t in xunlianzu :
            for x in  t[2]:
               beiye.train(t[1] ,x)



        for data in datas:

             data=''.join(re.findall(u'[\u4e00-\u9fff]+', data))
             name=beiye.classify(data)
             sql="insert into shouji(text,name,lei) values('{text}','{name}','{class}')".format(name=leiname,text=data.encode("utf-8"),lei=name \
                                                                                                )
             self.db.execute(sql)
             self.coon.commit()
    def paixu(self,text,lei):
        list=[]
        texts=self.selects(text,lei)
        for x in texts:
          for q in x:
           if   re.match('^[0-9a-z]+$', q):
               continue

           else:
                if q != None:
                 list.extend(jieba.cut(q))
        return list





