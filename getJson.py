import config
import getApi

# 早安的json数据
def getmoring_json(data_list):
    # 数据整合
    to_user = data_list[0]
    day = data_list[1]
    wek = data_list[2]
    wea = data_list[3]
    birthday = data_list[4]
    love_birthday=data_list[5]
    lovedays = data_list[6]
    city_name = data_list[7]
    type = data_list[8]
    max = data_list[9]
    min = data_list[10]
    content = getApi.getEvDayZaoAn()
    data_baby = {
        "touser": to_user,
        "template_id": config.template_id.get("id_forBaby"),
        "url": "https://m.tianqi.com/",
        "topcolor": "#FF0000",
        "data": {
            "content":
                {
                    "value": content,
                    "color": "#000000"
                },
            "date":
                {
                    "value": "今天是" + "{} {}".format(day, wek),
                    "color": "#8470FF"
                },
            "city": {
                "value": "城市:" + city_name,
                "color": "#808A87"
            },
            "weather": {
                "value": "天气:" + wea,
                "color": "#ED9121"
            },
            "min_temperature": {
                "value": "最低气温:" + min,
                "color": "#00FF00"
            },
            "max_temperature": {
                "value": "最高气温" + max,
                "color": "#FF6100"
            },
            "love_day": {
                "value": "今天是我们恋爱的第" + lovedays + "天",
                "color": "#FFC0CB"
            },
            "birthday": {
                "value": "距离我的生日还有" + birthday + "天",
                "color": "#FF8000"
            },
            "birthday": {
                "value": "距离宝贝的生日还有" + love_birthday + "天",
                "color": "#FF8000"
            }

        }
    }
    data_user = {
        "touser": to_user,
        "template_id": config.template_id.get("id_forUser"),
        "url": "https://m.tianqi.com/",
        "topcolor": "#FF0000",
        "data": {
            "content":
                {
                    "value": content,
                    "color": "#000000"
                },
            "date": {
                "value": "今天是" + "{} {}".format(day, wek),
                "color": "#8470FF"
            },
            "city": {
                "value": "城市:" + city_name,
                "color": "#808A87"
            },
            "weather": {
                "value": "天气:" + wea,
                "color": "#ED9121"
            },
            "min_temperature": {
                "value": "最低气温:" + min,
                "color": "#00FF00"
            },
            "max_temperature": {
                "value": "最高气温" + max,
                "color": "#FF6100"
            },"birthday": {
                "value": "距离我的生日还有" + birthday + "天",
                "color": "#FF8000"
            },
        }
    }
    if type == "baby":
        return data_baby
    else:
        return data_user


# 晚安的json数据
def getNight_json(to_user, type):
    content = getApi.getEvDayWanAn()
    data_baby = {
        "touser": to_user,
        "template_id": config.template_id_n.get("id_forBaby"),
        "url": "https://music.163.com/",
        "topcolor": "#FF0000",
        "data": {
            "content":
                {
                    "value": content,
                    "color": "#000000"
                },
            "like":
                {
                    "value": "时间过得真快 我们在一起的时间又多了一天,晚安宝贝",
                    "color": "#000000"
                }
        }
    }
    data_user = {
        "touser": to_user,
        "template_id": config.template_id_n.get("id_forUser"),
        "url": "https://music.163.com/",
        "topcolor": "#FF0000",
        "data": {
            "content":
                {
                    "value": content,
                    "color": "#000000"
                },
        }
    }
    if type == "baby":
        return data_baby
    else:
        return data_user
