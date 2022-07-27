# -*- coding:utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from application.views.manage import app

if __name__ == '__main__':


    #本机地址
    #app.run(host='10.0.20.237',port=9009)

    #上线地址
    app.run(host='10.0.30.239',port=9009)
    sys.path.append(os.path.dirname(sys.path[0]))

