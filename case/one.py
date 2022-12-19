# coding: UTF-8

import time

# 字符串包含筛选（直接move会报错-超出范围-因为for循环的长度变更）
# filterlist = ['[MAX]', '[MIN]', '[max]', '[min]']
# cols = ['WTUR_Temp_Ra_F32_TowerBase[MAX]', 'WGEN_Temp_Ra_F32_4[AVG]', 'WTPS_Temp_Ra_F32_Pcap3[MAX]', 'WTPS_Temp_Ra_F32_gen3[MIN]',
#         'WGEN_Temp_Ra_F32_1[MAX]', 'WNAC_Temp_Ra_F32[MIN]', 'WYAW_CTim_Rt_F32_Ygen[min]', 'WGEN_Spd_Ra_F32_overspblade1[AVG]']
# re = []
# for i in range(len(cols)):
#     for j in range(len(filterlist)):
#         if filterlist[j] in cols[i]:
#             re.append(cols[i])
# cols = list(set(cols) - set(re))
# print(cols)

# 冒泡
# a = [1, 34, 52, 64, 65, 10]
# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#         print(a)
# print(a)

num = '共 6 条'
num_list = [i for i in num if str.isdigit(i)]  # Python isdigit() 方法检测字符串是否只由数字组成。返回True or False.
print(num_list)

if len(num_list) > 1:
    number = int(num_list[0]) * 10 + int(num_list[1])
else:
    number = int(num_list[0])
print(number)