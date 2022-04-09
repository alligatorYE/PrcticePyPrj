# -*- coding = UTF-8 -*-
# @Time: 2020/6/29 15:44
# @Author: sudo
# @Site: 
# @File: test001.py
# @Software: PyCharm

score = -78
if 90 <= score <= 100:
    print("优")
elif 80 <= score < 90:
    print("良")
elif 60 <= score < 80:
    print("中")
elif 0 <= score < 60:
    print("差")
else:
    print("分数有误，请检查！")
