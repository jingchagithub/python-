#coding:utf-8
"""
主文件
"""
import mysql,jieba,pymysql,requests,simplebayes,BeautifulSoup,re,_tkinter,Tkinter,matplotlib


import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
class jihe(requests.Request):#全部集成的类

    def __init__(self,name,*html):#全部初始化
        requests.Request(self)
        self.name=name
        self.htmls=[]
        self.htmls.extend(html)
        self.wangye=[]
        self.mysqldb=mysql.mysqldb("root","root","html")
        self.datalist={}
        self.newlist=[]

    def paquwangye(self,wangye):#爬取网页函数
     try:
            assert isinstance(wangye,basestring)
            a=requests.get(wangye)
            html=BeautifulSoup.BeautifulSoup(a.text)#转换成beau对象并返回
            return html
     except Exception as e:
        print e

    def wangyechuli(self, wangye):#处理网页信息
        try:
            for wangy in  wangye:

             wangyetext = self.paquwangye(wangy)

             b = wangyetext.findAll(["a","title"])  # 获取全部超链接
             for x in b:
                if x.string != None:
                 self.wangye.append(x.string) # 爬取内容添加到爬取内容
        except Ellipsis as e:
            print e
        except requests.HTTPError as e:
            logging.error("服务器错误")
        except requests.ConnectionError as e:
            logging.error("连接失败")
        except AssertionError:
            logging.error('没有找到超链接')
        except AttributeError:
            return
    def pachongkongzhiqi(self):#执行全部网页爬去
        for html in self.htmls:

            self.wangyechuli(html)

    def shouji(self,xunlianzu):#将全部数据写入数据库
        self.mysqldb.fenlei(self.wangye,self.name,xunlianzu)
    def fenxi(self,lei):
        data=self.mysqldb.paixu(self.name,lei)
        self.datalist=simplebayes.SimpleBayes.count_token_occurrences(data)

        self.newlist=(sorted(self.datalist.items(), key=lambda x: x[1]))


    def paiming(self):
        value=self.newlistlist[:-9:-1]
        for x in value:
            print "{name}  |  {sum} ".format(name=x[0].encode("utf-8"),sum=x[1])
    def get_paiming(self):
        return  self.datalist
    def get_list(self):
        return self.newlist
def file(name):
  try:

    return [x for x in open(name)]
  except Exception as e:
      raise "你文件名写错了"

def text(name):
    return name.split()







if __name__=="__main__":

    # 载入方法text(字符串，多个以空格隔开)或file（一行一个字符串）
    # 填写格式[名字，载入]
    xunlianzu = []
    htmls = []
    jihes=[]
    while True:
     text =raw_input("输入类别名和网址 直接回车结束\n")
     if text=="":
         break
     else:
         texts=text.split(" ")
         jihes.append(jihe(texts[0],texts[1:]))
    for jihe in jihes:
     jihe.pachongkongzhiqi()
     print "{name} 已经收集完毕".format(name=jihe.name)


     jihe.shouji(badxunlian)
     print "{name} 贝叶斯分类完毕并存入数据库".format(name=jihe.name)
     lei = raw_input("输入类别")
     jihe.fenxi(lei)

     print "{name} 排序完成".format(name=jihe.name)
    paimings=simplebayes.BayesCategories()
    paimings.add_category("list")

    for jihe in jihes:
        paimings.add_category(jihe.name)
        for str in jihe.get_list():
         paimings.get_category(jihe.name).train_token(str[0],str[1])
         paimings.get_category("list").train_token(str[0], str[1])

    list=sorted(paimings.get_category("list").tokens.items(),key=lambda x:x[1])
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问

    method = [data[0] for data in list[:-11:-1]]

    x_pos = np.arange(10)

    performance = [data[1] for data in list[:-11:-1]]
    plt.bar(x_pos, performance,alpha=0.4, color='r', label=u"全部排行")
    suns=[]
    plt.xticks(x_pos,method)
    bar_width = x_pos+0.35
    plt.title(u'热度前十排行')
    for jihe in jihes:

      sums=[x[1] for x in jihe.newlist]
      sums.reverse()


      plt.bar(bar_width, sums[0:10], bar_width,alpha=0.4, color='r', label=jihe.name)
      bar_width+=0.35
    plt.legend()
    plt.tight_layout()
    plt.show()
