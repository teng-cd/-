
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
        '''前端交互'''
    def GetJson1(self,flag):
        if 0 == flag:  #全部数据
            return self.__GetAllJson1()

    """all数据"""
    def __GetAllJson(self):
        res = {}
        print(res)
        data2=self.mysql.FindMaxData()
        res['sensor']=(data2[0:12])
        res['sensor1']=(data2[12:24])
        res['state']=(data2[24])
        # res['sensor'] = self.mysql.FindMaxData()
        # res['sensor1'] = self.mysql.FindMaxData1()
        # res['state'] = self.mysql.FindMaxData3()

        print("*"*25 + "传感器数据" + "*"*25)
        print(res['sensor'])
        print(res['sensor1'])
        print(res['state'])
        return res
    """逸夫楼数据"""
    def __GetAllJson1(self):
        res1 = {}
        print(res1)
        res1['sensor2'] = self.mysql.FindMaxData2()
        print("*"*25 + "逸夫楼传感器数据" + "*"*25)
        print(res1['sensor2'])
        return res1


if __name__== '__main__':
    pass
