# -*- coding:utf-8 -*-
import requests
import json
print('登录')
url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/user/passwordLogin'
data = {
    'phone': '13426321208',
    'password': 'qwer1234'}
header = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
searchList = requests.post(url=url, data=data, headers=header, verify=False)

searchList = searchList.json()
header = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'csoSaaSToken': searchList['data']['token']
        }

# print('项目人员列表')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/agentManager/agentList'
# data = {
#             'pageNo': 1,
#             'pageSize': 10,
#             'allianceUserType': 1
#         }
# agentList = requests.post(url=url, data=data, headers=header, verify=False)
# if agentList.encoding==200:
#     agentList = agentList.json()
#     print(json.dumps(agentList, sort_keys=True, indent=2, ensure_ascii=False))
#
# print('历史参与项目-查看')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/agentManager/projectInfoJoined'
# data = {
#             'userId': agentList['data']['list'][0]['userId'],
#             'source': 1,
#         }
# projectInfoJoined = requests.post(url=url, data=data, headers=header, verify=False)
# if projectInfoJoined==200:
#     projectInfoJoined = projectInfoJoined.json()
#     print(json.dumps(projectInfoJoined, sort_keys=True, indent=2, ensure_ascii=False))

# print('预采购-下载列表数据 -模板')
# url='https://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/downLoadTemplate/projectTaskPlanTemplate?projectId=17983'
# def urldownload(url,filename=None):
#     """
#     下载文件到指定目录
#     :param url: 文件下载的url
#     :param filename: 要存放的目录及文件名，例如：./test.xls
#     :return:
#     """
#     down_res = requests.get(url=url)
#     with open(filename,'wb') as file:
#         file.write(down_res.content)
# urldownload(url,'./test1.xls')

#
# print('项目结算单列表(项目结算单管理)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/settlementList'
# data = {
#             'pageNo': 1,
#             'pageSize': 5,
#
#         }
# agentList = requests.post(url=url, data=data, headers=header, verify=False)
#
# if agentList.status_code==200:
#     agentList = agentList.json()
#     print(json.dumps(agentList, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(agentList.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
#
# print('生成订单-项目列表(项目结算管理-结算列表)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/getSelectProjectList'
# data = {
#             'pageNo': 1,
#             'pageSize': 5,
#         }
# getSelectProjectList = requests.post(url=url, data=data, headers=header, verify=False)
#
# if getSelectProjectList.status_code==200:
#     getSelectProjectList = getSelectProjectList.json()
#     print(json.dumps(getSelectProjectList, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(getSelectProjectList.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
# print('生成订单-供应商列表(项目结算管理-结算列表)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/getSelectSupplierList'
# data = {
#             'pageNo': 1,
#             'pageSize': 5,
#         }
# getSelectSupplierList= requests.post(url=url, data=data, headers=header, verify=False)
#
# if getSelectSupplierList.status_code==200:
#     getSelectSupplierList = getSelectSupplierList.json()
#     print(json.dumps(getSelectSupplierList, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(getSelectSupplierList.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
#
# print('生成订单-结算人员列表(项目结算管理-结算列表)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/getOrderPeopleList'
# data = {
#             'pageNo': 1,
#             'pageSize': 5,
#         }
# getOrderPeopleList = requests.post(url=url, data=data, headers=header, verify=False)
#
# if getOrderPeopleList.status_code==200:
#     getOrderPeopleList = getOrderPeopleList.json()
#     print(json.dumps(getOrderPeopleList, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(getOrderPeopleList.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
#
#
# print('生成订单-勾选人员结算信息（项目结算管理-结算列表）')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/isCheck'
# data = {
#     'batchJson': '[{"customizeNum":"20","id":"34296","isChecked":"1"}]',
#     "cacheKey": "123456" #缓存唯一key 必填
#         }
# isCheck = requests.post(url=url, data=data, headers=header, verify=False)
#
# if isCheck.status_code==200:
#     isCheck = isCheck.json()
#     print(json.dumps(isCheck, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(isCheck.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
#
# print('生成订单-【确认笔数、订单信息确认】 列表(项目结算管理-结算列表)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/getConfirmOrderPeopleList'
# data = {
#     'cacheKey': '123456',#缓存唯一key 必填
#     'pageNo':1,
#     'pageSize':10
#
#         }
# getConfirmOrderPeopleList= requests.post(url=url, data=data, headers=header, verify=False)
# if getConfirmOrderPeopleList.status_code==200:
#     getConfirmOrderPeopleList = getConfirmOrderPeopleList.json()
#     print(json.dumps(getConfirmOrderPeopleList, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(getConfirmOrderPeopleList.json(), sort_keys=True, indent=2, ensure_ascii=False))
#
# print('生成订单- 统计已选笔数、项目支付总计金额、项目统计(项目结算管理-结算列表))')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/countSelectBill'
# data = {
#     'cacheKey': '123456',#缓存唯一key 必填
#         }
# countSelectBill= requests.post(url=url, data=data, headers=header, verify=False)
# if countSelectBill.status_code==200:
#     countSelectBill = countSelectBill.json()
#     print(json.dumps(countSelectBill, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(countSelectBill.json(), sort_keys=True, indent=2, ensure_ascii=False))
#

# print('确认生成订单(项目结算管理-结算列表)')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/orderManagement/generateOrder'
# data = {
#     'cacheKey': '123456',#缓存唯一key 必填
#         }
# generateOrder= requests.post(url=url, data=data, headers=header, verify=False)
# if generateOrder.status_code==200:
#     generateOrder = generateOrder.json()
#     print(json.dumps(generateOrder, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(generateOrder.json(), sort_keys=True, indent=2, ensure_ascii=False))


# print('项目人员列表')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/ProjectPersonnelManagement/personnelListNew'
# data = {
#     'projectId': '17983',
#     'type': 1,
#     'pageNo': 1,
#     'pageSize': 10,
#     #'fullName':'吕秀章',
#     'inStatus':'1'
#
#         }
# personnelListNew= requests.post(url=url, data=data, headers=header, verify=False)
# if personnelListNew.status_code==200:
#     personnelListNew = personnelListNew.json()
#     print(json.dumps(personnelListNew, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(personnelListNew.json(), sort_keys=True, indent=2, ensure_ascii=False))


print('提交任务 - 待提交任务列表/手动提交')
url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/confirm/listTaskRecords'
data = {
    'projectId': '19181',
    'projectType': 20
        }
listTaskRecords= requests.post(url=url, data=data, headers=header, verify=False)
if listTaskRecords.status_code==200:
    listTaskRecords = listTaskRecords.json()
    print(json.dumps(listTaskRecords, sort_keys=True, indent=2, ensure_ascii=False))
else:
    print(json.dumps(listTaskRecords.json(), sort_keys=True, indent=2, ensure_ascii=False))


# print('提交任务 - 结算单生成')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/confirm/createStatement'
# data = {
#     'cacheKey': listTaskRecords['data']['cacheKey'],
#         }
# createStatement= requests.post(url=url, data=data, headers=header, verify=False)
# if createStatement.status_code==200:
#     createStatement = createStatement.json()
#     print(json.dumps(createStatement, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(createStatement.json(), sort_keys=True, indent=2, ensure_ascii=False))


# print('提交任务 - 结算单生成_二次确认')
# url = 'http://saas-cso-pc.jimijiayuan.cn/rest/cso/saas/confirm/saveStatement'
# data = {
#     #'cacheKey': listTaskRecords['data']['cacheKey'],
#     'cacheKey': listTaskRecords['data']['cacheKey'],
#     'projectId':'19181',
#     'contractScale':2,
#     'signType':2
#         }
# saveStatement= requests.post(url=url, data=data, headers=header, verify=False)
# if saveStatement.status_code==200:
#     saveStatement = saveStatement.json()
#     print(json.dumps(saveStatement, sort_keys=True, indent=2, ensure_ascii=False))
# else:
#     print(json.dumps(saveStatement.json(), sort_keys=True, indent=2, ensure_ascii=False))


print('提交任务 - 结算单生成_二次确认')
url = 'http://saas-cso-pc.jimijiayuan.cn/rest/gongye/saas/receive/signStatement'
data = {
    'statementId': 9400703,
    'signType':2}

saveStatement= requests.post(url=url, data=data, headers=header, verify=False)
if saveStatement.status_code==200:
    saveStatement = saveStatement.json()
    print(json.dumps(saveStatement, sort_keys=True, indent=2, ensure_ascii=False))
else:
    print(json.dumps(saveStatement.json(), sort_keys=True, indent=2, ensure_ascii=False))