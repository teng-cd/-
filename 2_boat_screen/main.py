import json
from flask import Flask, render_template, request
from pip import main
from MainBlock import MainBlock,Visualization    #主要的显示模块
from manager import Manager
from data_mysql import DataMysql
from flask import jsonify
from gevent import pywsgi
app = Flask(__name__,template_folder="templates")
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

#全局变量
class_list = [MainBlock(),Visualization()]
manager = Manager(class_list=class_list,
                data_mysql=DataMysql())  #只需要一行代码

#更新传感器参数
@app.route('/update', methods=['POST'])
def update():
    result = {}
    if request.method == 'POST':
        data = eval(request.get_data())
        result = manager.GetJson(int(data['flag']))   #调用接口
    return result
#更新逸夫楼传感器参数
@app.route('/update1', methods=['POST'])
def update1():
    result1 = {}
    if request.method == 'POST':
        data1 = eval(request.get_data())
        result1 = manager.GetJson1(int(data1['flag']))   #调用接口
    return result1

#获取前端页面
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__== '__main__':

    server = pywsgi.WSGIServer(('127.0.0.1',5006), app)
    server.serve_forever()

