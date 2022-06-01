
import requests
import json
import time

# url = 'https://saas-oss.jimijiayuan.cn/rest/crm/oss/login/auth'
# data = {
#     'username': 'admin',
#     'password': '123456'
# }
#
# osstoken=requests.post(url=url, data=data,verify=False).json()
# header={
#     'authorization':osstoken['returnData']['usermodel']['sessionid'],
#
# }
#
# url1 = 'https://saas-oss.jimijiayuan.cn/rest/crm/oss/quickAudit/getDisplayInfo'
# data1 = {
#     'projectId': '22299'
# }
# kpzlist=requests.post(url=url1, data=data1,headers=header,verify=False).json()
# print(json.dumps(kpzlist, sort_keys=True, indent=2, ensure_ascii=False))
#
# headers={
#     'authorization':osstoken['returnData']['usermodel']['sessionid'],
#     'content-type':'application/json'
# }
#
# url2 = 'https://saas-oss.jimijiayuan.cn/rest/crm/oss/quickAudit/list'
# data2 = {
#     'projectId':15900,
#     'firstEnter':0,
#     'conditions':[{'key':'submitDt','value':'','isTopic':0,'topicType':''}]
# }
#
#
# kpzlist2=requests.post(url=url2, data=json.dumps(data2),headers=headers,verify=False).json()
# print(json.dumps(kpzlist2, sort_keys=True, indent=2, ensure_ascii=False))






url1 = 'https://saas-crm-wx.jimijiayuan.cn/rest/saas/crm/xcx/questionnaire/answerQuestionnaireEncryption'
data1 = {
    'c':'VeBshZGklZopsBOmtK4rzqum0Ip+a06isjtp0A1G7XbBgtdD2NhUYGns9PhTfXKlE36oZMQGK4XwKbOSQrLy8BMtq8l6qyWya/Ggl6GbvGNKPzxl8zL2BRLq4VTcyWKU4Zsk7QZiqEMPyTc9IOJfTTZLYbMAbv1WwMsN1DlylhulX7/yO7M/FuMB/LH219hnTvaXSmA+5lpiDQY3HN99XGwQEoXHB5MwAXEB4i2KjHNXmJbX7xMqYMNMT4FuGaD9jYWfuELNxwrdo0LC9f5tVTZaUg9T4f54livtvVLMJXEYNQY94OWJuvWKDl/8LXcq+ptQo9GCJ1lOw4Yu9E5sSQ=='
}
header={
        'Appversion':'2.14.5',
        'SaasCrmXcxToken':'ac7fd34ccfa87927394d155f9c16a2e5'

    }
# kpzlist=requests.post(url=url1, data=data1,headers=header,verify=False).json()
# print(json.dumps(kpzlist, sort_keys=True, indent=2, ensure_ascii=False))


import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def main(name):
#     print('线程%s 开始' % name)
#
#     for i in range(1,2):
#         # kpzlist=requests.post(url=url1, data=data1,headers=header,verify=False).json()
#         # print(json.dumps(kpzlist, sort_keys=True, indent=2, ensure_ascii=False))
#         print(i)
#     print('线程%s 结束' % name)
#
#
# if __name__ == '__main__':
#     thread_name = ['1','2','3','4','5','6','7','8','9','10']
#     with ThreadPoolExecutor(5) as executor:
#         executor.map(main, thread_name)
# print(1 or 0)





