from datetime import datetime, date
from time import localtime

# 获得生日/相爱时间
# 时间函数 获得当前时间
def getTime():
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() - 1]
    return today, week


# 时间函数   获得生日时间差
def getbirthDay(birthday, temp):
    if temp == "user":
        return birthday
    else:
        year = localtime().tm_year
        month = localtime().tm_mon
        day = localtime().tm_mday
        today = datetime.date(datetime(year=year, month=month, day=day))
        # 获取生日的月和日
        birthday_month = int(birthday.split("-")[1])
        birthday_day = int(birthday.split("-")[2])
        # 今年生日
        year_date = date(year, birthday_month, birthday_day)
        # 计算生日年份，如果还没过，按当年减，如果过了需要+1
        if today > year_date:
            birth_date = date((year + 1), birthday_month, birthday_day)
            birth_day = str(birth_date.__sub__(today)).split(" ")[0]
        elif today == year_date:
            birth_day = 0
        else:
            birth_date = year_date
            birth_day = str(birth_date.__sub__(today)).split(" ")[0]
        return birth_day


# 时间函数   获得相爱时间差
def getlove_day(love_date, temp):
    if temp == "user":
        return love_date
    else:
        year = localtime().tm_year
        month = localtime().tm_mon
        day = localtime().tm_mday
        today = datetime.date(datetime(year=year, month=month, day=day))
        # 获取在一起的日子的日期格式
        love_year = int(love_date.split("-")[0])
        love_month = int(love_date.split("-")[1])
        love_day = int(love_date.split("-")[2])
        love_date = date(love_year, love_month, love_day)
        # 获取在一起的日期差
        love_days = str(today.__sub__(love_date)).split(" ")[0]
        return love_days
