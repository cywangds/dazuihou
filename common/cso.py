# -*- coding:utf-8 -*-
import requests
import json
import unittest



class TestStringMethods(unittest.TestCase):


    def setUp(self):
        print('登录')
        url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/user/passwordLogin'
        data = {
            'phone': '13000003398',
            'password': 'qwer1234'
        }
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
        searchList = requests.post(url=url, data=data, headers=self.header, verify=False)
        searchList = searchList.json()
        self.header = {
            #'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'csoSaaSToken': searchList['data']['token']
        }

    def test_01(self):

        url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/importProjectPeople/importExcelNew'
        file={'file':open('E:/预采购模板2.xls','rb')}
        print(file)
        data = {
            'projectId': '23795',
            'taskShowType': 1,
            'secondaryConfirmation': 0,
            'taskDt':'2022-03-31'
            #'file': 'filename="预采购模板2.xls"'

        }
        agentList = requests.post(url=url, data=data,files=file,headers=self.header, verify=False)
        #agentList =requests.request(url=url, method='post', files=file, headers=self.header,allow_redirects=False)
        agentList = agentList.json()
        print(agentList)
        #print(json.dumps(agentList, sort_keys=True, indent=2, ensure_ascii=False))


    def tearDown(self):
        print('结束')


if __name__ == '__main__':
    unittest.main()

#
#
# import threading  # 创建一个线程
# import socket
#
# server = socket.socket()
# server.bind(('0.0.0.0', 8888))
# server.listen() # 监听
#
# def workon(conn):
#     while True:
#         data = conn.recv(1024)
#
#         if data == b'':
#             conn.close()
#             break
#         else:
#             print("接收到的消息: {}".format(data.decode()))
#             conn.send(data)
#
# # 主线程
# while True:
#     conn, addr = server.accept()
#     print("{}正在连接".format(addr))
#
#     # 线程去处理消息
#     p = threading.Thread(target=workon, args=(conn,))
#     p.start()


import multiprocessing  # 引用进程模块
# import threading    # 引用线程模块
# import time
#
# def func(data):
#     while True:
#         time.sleep(1)
#         data += 1
#         print(data)
#
# # mult = multiprocessing.Process(target=func, args=(1314,))
# # mult.start()  # 运行进程
#
# thre = threading.Thread(target=func, args=(500,))   # 创建一个线程
# thre.start()  # 运行线程
#
# print("这是主进程")

# from concurrent.futures import ThreadPoolExecutor
# import time
# def wait_on_b():
#     time.sleep(5)
#     print(b.result())  # b will never complete because it is waiting on a.
#     return 5
#
# def wait_on_a():
#     time.sleep(5)
#     print(a.result())  # a will never complete because it is waiting on b.
#     return 6
#
#
# executor = ThreadPoolExecutor(max_workers=2)
# a = executor.submit(wait_on_b)
# b = executor.submit(wait_on_a)
# def setUpp():
#     print('登录')
#     url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/user/passwordLogin'
#     data = {
#         'phone': '13000003398',
#         'password': 'qwer1234'
#     }
#     header = {
#         'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#     }
#     searchList = requests.post(url=url, data=data, headers=header, verify=False)
#     searchList = searchList.json()
#     header = {
#         #'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#         'csoSaaSToken': searchList['data']['token']
#     }
#     url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/importProjectPeople/importExcelNew'
#     file={'file':open('E:/预采购模板2.xls','rb')}
#
#     print(file)
#
#     data = {
#         'projectId':'23795',
#         'taskShowType': 1,
#         'secondaryConfirmation': 0,
#         'taskDt':'2022-03-31'
#
#     }
#     agentList = requests.post(url=url, data=data,files=file,headers=header, verify=False)
#     #agentList =requests.request(url=url, method='post', files=file, headers=self.header,allow_redirects=False)
#     agentList = agentList.json()
#     print(agentList)
#     #print(json.dumps(agentList, sort_keys=True, indent=2, ensure_ascii=False))
#
#
#
# if __name__ == '__main__':
#     setUpp()