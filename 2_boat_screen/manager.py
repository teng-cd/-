
import pandas as pd
import numpy as np
from data_mysql import DataMysql
import time
from gevent import pywsgi
from mysql import Mysql



class Manager():

    '''初始化'''
    def __init__(self,class_list=[],data_mysql=None):
        super(Manager, self).__init__()

        # 1.初始化变量
        self.mysql = data_mysql   #数据库管理
        self.class_list = class_list

    '''前端交互'''
    def GetJson(self,flag):
        if 0 == flag:  #全部数据
            return self.__GetAllJson()

    """all数据"""
    def __GetAllJson(self):
        # res = self.mysql.FindVisData()
        res = {}
        print(res)
        res['sensor'] = self.mysql.FindMaxData()
        res['sensor2'] = self.mysql.FindMaxData2()
        print("*"*25 + "传感器数据" + "*"*25)
        print(res['sensor'])
        print(res['sensor2'])
        # res['main'] = self.class_list[0].GetJson(self.mysql.FindMainData())
        return res


if __name__== '__main__':
    pass
