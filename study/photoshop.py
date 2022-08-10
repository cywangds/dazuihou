# -*- coding:utf-8 -*-
import requests
import json
import unittest
import xlwt
import xlrd


workbook=xlwt.Workbook()#创建一个新的工作簿
sheet=workbook.add_sheet("no1")#在工作簿中添加一个新的工作表，如果不给名字的话就是默认的名字 这里的名字是no1
# sheet.write(0,0,'text3')#向第一个单元格写入text
# # sheet.write(0,1,'text1')#向第一个单元格写入text
# # sheet.write(0,2,'text2')#向第一个单元格写入text
# sheet.write(1,0,'text3')#向第一个单元格写入text
# sheet.write(2,0,'text3')#向第一个单元格写入text
#
# sheet.write(0,1,'text1')#向第一个单元格写入text
# sheet.write(1,1,'text1')#向第一个单元格写入text
# sheet.write(2,1,'text1')#向第一个单元格写入text
# # row2=sheet.row(1)#在第二行创建一个行对象
# # row2.write(0,'shu')#向第二行第一列写入 shu
# # row2.write(1,'shun')#向第二行第二列写入 shun
# workbook.save('example2.xls')



def ojbk():
    x = 0
    y=0
    filepath = r'C:\Users\wangchaoyue\Desktop\kkk.xls'
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    sheet1 = data.sheet_by_name("Sheet1")  # 按名获取该文件中的表格
    first_col_values = sheet1.col_values(0)  # 获取第1列的数据
    secont_col_values = sheet1.col_values(1)  # 获取第2列的数据
    #first_col_values=['1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0']

    sore=[0.50,0.4142,0.3660,0.3333,0.3090,0.2899,0.2743,0.2612,0.2500,0.2403,0.2317,0.2240]

    for e in first_col_values:
        for i in sore:
            print(i)

            url = 'http://101.200.36.164:80/image/get_single'
            header = {
                'content-type': 'application/json',
            }
            data = {
                'code': e,
                'project_id': -1,
                'score': i,
            }
            agentList = requests.get(url=url, params=data, headers=header, verify=False)
            # print(agentList.json())
            # print(len(agentList.json()))
            print(agentList.json().pop().pop())
            print(x)
            sheet.write(x, 1, i)
            sheet.write(x, 6, agentList.json().pop().pop())  # 向第一个单元格写入text
            sheet.write(x, 5, e)  # 向第一个单元格写入text
            sheet.write(x, 4, secont_col_values[y]) # 向第一个单元格写入text
            x = x + 1
        y=y+1


    workbook.save('example5.xls')
if __name__ == '__main__':
    ojbk()
