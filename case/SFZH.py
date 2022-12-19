# coding: utf-8

from id_validator import validator

print(validator.is_valid('440308199901101512')) # 大陆居民身份证 18 位
print(validator.is_valid('610104620927690'))    # 大陆居民身份证 15 位
print(validator.is_valid('810000199408230021')) # 港澳居民居住证 18 位
print(validator.is_valid('830000199201300022')) # 台湾居民居住证 18 位

from id_validator import validator

print(validator.get_info('440308199901101512')) # 18 位
print(validator.get_info('610104620927690'))   # 15 位
print(validator.get_info('440308199901101512'))

from id_validator import validator

validator.fake_id()                                      # 18 位
validator.fake_id(False)                                 # 15 位
# validator.fake_id(True, '上海市', '2000', 1)              # 生成出生于 2000 年上海市的男性居民身份证
# validator.fake_id(True, '南山区', '1999', 0)              # 生成出生于 1999 年广东省深圳市南山区的女性居民身份证
# validator.fake_id(True, '江苏省', '200001', 1)            # 生成出生于 2000 年 1 月江苏省的男性居民身份证
# validator.fake_id(True, '厦门市', '199701', 0)            # 生成出生于 2000 年 1 月福建省厦门市的女性居民身份证
print(validator.fake_id(True, '台湾省', '19960815', 0))          # 生成出生于 2013 年 10 月 10 日台湾省的女性居民居住证
print(validator.fake_id(True, '香港特别行政区', '19970701', 0))    # 生成出生于 1997 年 7 月 1 日香港特别行政区的女性居民居住证
print(validator.fake_id(True, '澳门特别行政区', '19951001', 0))    # 生成出生于 1997 年 7 月 1 日香港特别行政区的女性居民居住证