# coding: UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 选择浏览器
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.91haoka.cn/91haoka_platform/#/login')    # 进入敢探号
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/input').send_keys('NB流量卡')    # 账户
# time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/input').send_keys('whw15093363135')   # 密码
# time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/button').click()     # 登录
time.sleep(2)
driver.find_elements(By.CLASS_NAME, 'el-collapse-item__header')[0].click()     # 产品管理中心
time.sleep(1)
driver.find_elements(By.CLASS_NAME, 'navli2')[1].click()   # 在售商品
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[5]/div[1]/button[3]/span').click()      # 添加供应商提供的套餐
time.sleep(1)
num1 = driver.find_elements(By.CLASS_NAME, 'cell')

# driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[3]/a[2]').click()     # 查看供应商已下架商品
# time.sleep(1)
# num = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[5]/div[2]/span').text     # 获取下架条数
# num_list = [i for i in num if str.isdigit(i)]  # Python isdigit() 方法检测字符串是否只由数字组成。返回True or False.
# if len(num_list) > 1:           # 判断下架条数是个位还是十位
#     number = int(num_list[0]) * 10 + int(num_list[1])
# else:
#     number = int(num_list[0])
# for i in range(number):            # 下架
#     xia1 = 'document.querySelector("#app > div > div.center > div.right.productionDelivery > div.con > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_2_column_13.is-center > div > button:nth-child(3) > span").click()'
#     driver.execute_script(xia1)
#     time.sleep(0.5)
#     xia2 = 'document.querySelector("body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span").click()'
#     driver.execute_script(xia2)
#     time.sleep(0.5)
# driver.find_elements(By.CLASS_NAME, 'navli2')[1].click()   # 在售商品
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[5]/div[1]/button[3]/span').click()      # 添加供应商提供的套餐
# time.sleep(1)

