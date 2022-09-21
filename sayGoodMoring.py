# 发早安消息的主运行文件
import config
import getApi
import getJson
import getSomeDay
import sendMessage

if __name__ == '__main__':
    access_token = getApi.get_access_token()
    # 接收的所有用户信息
    user = config.user
    for i in range(len(user)):
        # 单个用户信息列表
        user_dict = user[i]
        # 用户id
        touser = user_dict.get("userid")
        # 用户类别
        kind = user_dict.get("kind")
        # 传入省份和市获取天气信息
        province, city = user_dict.get("province"), user_dict.get("city")
        weather, max_temperature, min_temperature = getApi.get_weather(province, city)
        # 获得时间
        today, week = getSomeDay.getTime()
        # birthday
        birth_day = getSomeDay.getbirthDay(user_dict.get("birthday"), kind)
        # love_birthday
        love_birthday = getSomeDay.getbirthDay(user_dict.get("love_birthday"), kind)
        # love_day
        love_day = getSomeDay.getlove_day(user_dict.get("love_date"), kind)
        # 数据列表
        data_list = [touser, today, week, weather, birth_day,love_birthday,love_day, city, kind, max_temperature, min_temperature]
        data = getJson.getmoring_json(data_list)
        sendMessage.send_message(access_token, data)
