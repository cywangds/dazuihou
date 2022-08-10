# -*- coding: utf-8 -*-
# import xlsxwriter as xw
#
#
# def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
#     workbook = xw.Workbook(fileName)  # 创建工作簿
#     worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
#     worksheet1.activate()  # 激活表
#     title = ['序号', '酒店', '价格']  # 设置表头
#     worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
#     i = 2  # 从第二行开始写入数据
#     for j in range(len(data)):
#         insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
#         row = 'A' + str(i)
#         worksheet1.write_row(row, insertData)
#         i += 1
#     workbook.close()  # 关闭表
#
#
# # "-------------数据用例-------------"
# testData = [
#     {"id": 1, "name": "立智", "price": 100},
#     {"id": 2, "name": "维纳", "price": 200},
#     {"id": 3, "name": "如家", "price": 300},
# ]
# fileName = '测试.xlsx'
# xw_toExcel(testData, fileName)

import xlwt
# workbook=xlwt.Workbook() # 初始化创建一个工作簿
# sheet1=workbook.add_sheet('sheet1',cell_overwrite_ok=True)#创建表单
# list1=[['id', '姓名', '国家'], [1.0, '曹操', '魏国'], [2.0, '刘备', '蜀国'], [3.0, '孙权', '吴国'], [4.0, '荀彧', '魏国'], [5.0, '诸葛亮', '蜀国'], [6.0, '周瑜', '吴国'], [7.0, '曹仁', '魏国'], [8.0, '关羽', '蜀国'], [9.0, '吕蒙', '吴国']]
# row=0
# for colours in list1:
#     for i in range(0, len(colours)):
#       #print(i, colours[i])
#       sheet1.write(row,i,colours[i])
#     row=row+1
#     #print(row)
# workbook.save('我的数据2.xlsx')
# print("Excel文件创建成功了")


# import xlwt
#
# workbook=xlwt.Workbook()#创建一个新的工作簿
#
# sheet=workbook.add_sheet("no1")#在工作簿中添加一个新的工作表，如果不给名字的话就是默认的名字 这里的名字是no1
#
# sheet.write(0,0,'text')#向第一个单元格写入text
#
# row2=sheet.row(1)#在第二行创建一个行对象
#
# row2.write(0,'shu')#向第二行第一列写入 shu
#
# row2.write(1,'shun')#向第二行第二列写入 shun
#
# workbook.save('example2.xls')


import xlrd
filepath=r'C:\Users\wangchaoyue\Desktop\kkk.xls'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
sheet1 = data.sheet_by_name("Sheet1")   # 按名获取该文件中的表格
first_col_values = sheet1.col_values(0) # 获取第1列的数据
print(first_col_values)