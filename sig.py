# -*- coding: UTF-8 -*-
from blinker import Namespace    #导入模块

my_signals=Namespace()           #创建命名空间，作用是可创建并存储多个信号发射对象
model_saved=my_signals.signal('model_saved')    #创建一个信号发射对象，并赋予它一个<strong>独一无二</strong>的名字


from flask import Flask
app=Flask(__name__)          #建立一个应用对象：app
model_saved.send(app,data1='A Signal',data2={1:1})   #发送信号。第一个参数app，代表发送者    

                                                    #后面的参数data1，data2 为发送的数据
#发送信号
@app.route('/')
def index():
    model_saved.send(app,data1='A Signal',data2={1:1})    #发送了信号
    return '信号已经发送'


#接收信号
@model_saved.connect_via(app)           #装饰器，接收app通过model_saved发送而来的信号
def signal_recv(app,data1,data2):       #第一个参数app代表发送者，后面的参数为接收到的数据的键所对应的值
    print('信号接收函数:{0}，{1}'.format(data1,data2))
    pass

if __name__=="__main__":
    app.debug = True
    app.run(host = '192.168.101.61')
