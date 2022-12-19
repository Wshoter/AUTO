# coding: UTF-8

# from xuanhuanwu_pashu import driver
import time
from selenium.webdriver.common.by import By
# for i in range(2-1):
#     print(i)


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
# def text_create(name, msg):
#     desktop_path = "C:\\Users\\Wshor\\Desktop\\"  # 新创建的txt文件的存放路径
#     full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
#     file = open(full_path, 'w')
#     file.write(msg)  # msg也就是下面的Hello world!
#     # file.close()
# text_create('九星毒奶', '他来了！他来了！他带着一阵风来了！')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!

# python 读写txt
# txt = "C:\\Users\\Wshor\\Desktop\\jiuxing2.txt"
# # r只读 r+可读可写 w只写 w+可读可写 a只追写 a+可读可写
# txt2 = open(txt, 'a', encoding='utf-8')
# # txt2.write('九星毒奶江小皮3'+'\n')
# # red = open("C:\\Users\\Wshor\\Desktop\\jiuxing2.txt", 'r',  encoding='utf-8')
# # print(txt2.read())
# for i in range(5):
#     txt2.write('九星毒奶江小皮%s'%(4-i) + '\n')

# python 读写excel
import xlrd, xlwt, math
# excel = xlwt.Workbook(encoding='utf-8')
# sheet = excel.add_sheet("sheet名")
# # sheet.write(0, 0, '第一行第一列')
# # sheet.write(0, 1, '第一行第二列')
# a = ['Abc', 136783678, '635453364535435', 'aBc', 14353242423, '4633454535657']
# for i in range(len(a)):
#     if i + 1 < 4:
#         sheet.write(0, i, a[i])
#     else:
#         sheet.write(1, i - 3, a[i])
# excel.save("C:\\Users\\Wshor\\Desktop\\exce.xls")
# excel2 = xlrd.open_workbook("C:\\Users\\Wshor\\Desktop\\exce.xls")
# print(excel2.sheets())  # [Sheet  0:<sheet名>]
# print(excel2.sheet_names()) # ['sheet名']
# sheet1 = excel2.sheets()[0] # 获取第一张sheet
# print(sheet1.ncols, sheet1.nrows)   # 获取列数行数3 2    ncols列数 nrows行数
# print(sheet1.row_values(1)) #获取第二行数据['aBc', 14353242423.0, '4633454535657']
# print(sheet1.col_values(1)) #获取第二列数据[136783678.0, 14353242423.0]
# print(sheet1.row(1)[1].value)   # 获取第2行第2列数据14353242423.0
# print(sheet1.cell_value(1, 1))  # 获取第2行第2列数据14353242423.0

# datalist = [['1', 2], ['a', 'b', 'c'], ['B', 'A', 'C', 'D']]
# execl = xlwt.Workbook() # 实例化一个Workbook()对象(即excel文件)
# for i in range(len(datalist)):
#     sheet_every = execl.add_sheet(datalist[i][0])   # 命名各sheet的name
#     for j in range(len(datalist[i])):
#         sheet_every.write(0, j, datalist[i][j]) # 遍历写入数据
# execl.save("C:\\Users\\Wshor\\Desktop\\excel.xls")

execl2 = xlrd.open_workbook("C:\\Users\\Wshor\\Desktop\\excel.xls")
# print(execl2.sheet_names()) # 获取各sheet的名字
# print(len(execl2.sheet_names()))    # 获取有几个sheet
# print(execl2.sheets()[0].ncols, execl2.sheets()[0].nrows)   # 获取第一个sheet的行数、列数
# # list1, list2 = [], []
# for i in range(len(execl2.sheet_names())):
#     for j in range(execl2.sheets()[i].nrows):
#         for k in range(execl2.sheets()[i].ncols):
#             cell_value = execl2.sheets()[i].cell_value(j, k)
#             print(cell_value, end='\t')
#             list1.append(cell_value)
# list2.append(list1)
# print(list1)
# print(list2)

import xlrd
from xlutils.copy import copy
file_name = 'C:\\Users\\Wshor\\Desktop\\excel.xls'
readbook = xlrd.open_workbook(file_name)
sheet = readbook.sheets()[1]
nrows, ncols = sheet.nrows, sheet.ncols # 获取excel的行数、列数
book2 = copy(readbook) # 由于xlrd只能读不能写，xlwt只能写不能读，所以如果通过xlrd读出的表格内容是没办法进行操作的，因此需要拷贝一份原来的excel
sheet1 = book2.get_sheet(1) # 获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
a = ['15345345', '624423525', '3464324235', 'gegegeg', '隔热如果个人']
# for i in range(len(a)): # 在已有行数的下面追加数据
#     for j in range(10):
#         sheet1.write(nrows + i, j, '要写的内容%s' % i)
for i in range(len(a)): # 在已有行数（至少10行）的第X列补充内容
    sheet1.write(nrows - 10 + i, 10, a[i])
book2.save(file_name)










