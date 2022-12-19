# coding: UTF-8
import random
import time
import string
class RandomUtil(object):
    #生成以test+日期开头的字符串
    def getRandom(self):
        date = time.strftime("%Y%m%d")
        ran_str = ''.join(random.sample(string.digits, 8))
        return date + ran_str

cs = RandomUtil()
yes = cs.getRandom()
print(yes)