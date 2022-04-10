# 记录生肖，根据年份来判断生肖
chineseZodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

print(chineseZodiac[0:12])

year = 2022

print(chineseZodiac[year % 12])
