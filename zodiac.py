

zodiacName = (u"魔羯座", u"水瓶座", u"双鱼座", u"白羊座", u"金牛座", u"双子座",
              u"巨蟹座", u"狮子座", u"处女座", u"天秤座", u"天蝎座", u"射手座")
zodiacDays = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
             (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (5, 15)

zodiacDay = list(filter(lambda x: x <= (month, day), zodiacDays))

print(zodiacDay)

zodiacLen = (len(zodiacDay)) % 12

print(zodiacName[zodiacLen])
