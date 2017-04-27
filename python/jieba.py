#coding:utf-8
"""
将获得数据用jieba库进行分词
"""

import jieba;
class jiebaclass(object):
    def __str__(self):
        return "jieba分词模块"
    def __init__(self):
        self.jieguo=[]
    def fenci(self,list):
        for x in list:
            q=jieba.lcut(s,cut_all=True)

        self.jieguo.append(q)
