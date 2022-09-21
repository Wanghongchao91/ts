# 通过api获取json数据
from time import time
from requests import get
import cityinfo
import config
import http.client
import urllib
import json


# 获得微信的access_token
def get_access_token():
    # appId
    app_id = config.app_id
    # appSecret
    app_secret = config.app_secret
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    access_token = get(post_url).json()['access_token']
    # print(access_token)
    return access_token


# 获得天气数据
def get_weather(province, city):
    # 城市id
    city_id = cityinfo.cityInfo[province][city]["AREAID"]
    # 毫秒级时间戳
    t = (int(round(time() * 1000)))
    headers = {
        "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
    response = get(url, headers=headers)
    response.encoding = "utf-8"
    response_data = response.text.split(";")[0].split("=")[-1]
    response_json = eval(response_data)
    # print(response_json)
    weatherinfo = response_json["weatherinfo"]
    # 天气
    weather = weatherinfo["weather"]
    # 最高气温
    temp = weatherinfo["temp"]
    # 最低气温
    tempn = weatherinfo["tempn"]
    return weather, temp, tempn


# 每日早安心语  天行数据：https://www.tianapi.com/apiview/143（免费）
# 需要填写自己的key
def getEvDayZaoAn():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    # --------------------------------这里填写----------------------------------------
    params = urllib.parse.urlencode({'key': 'your key'})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/zaoan/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    # 获得json数据
    data_json = data.decode('utf-8')
    # json数据>>>python dict 数据
    data_python = json.loads(data_json)
    # print(data_python)
    # python dict数据>>>需要的list数据
    newList = data_python.get('newslist')
    # list数据>>>dict数据
    newList_dict = newList[0]
    # 每日早安
    content = newList_dict.get('content')
    return content
    # print(content)


# 每日晚安心语   天行数据：https://www.tianapi.com/apiview/142（免费）
# 需要填写自己的key
def getEvDayWanAn():
    conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
    # --------------------------------这里填写----------------------------------------
    params = urllib.parse.urlencode({'key': ''})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    conn.request('POST', '/wanan/index', params, headers)
    res = conn.getresponse()
    data = res.read()
    # 获得json数据
    data_json = data.decode('utf-8')
    # json数据>>>python dict 数据
    data_python = json.loads(data_json)
    # print(data_python)
    # python dict数据>>>需要的list数据
    newList = data_python.get('newslist')
    # list数据>>>dict数据
    newList_dict = newList[0]
    # 每日晚安
    content = newList_dict.get('content')
    return content
    # print(content)
