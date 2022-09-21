# 发晚安消息的主运行文件
import config
import getApi
import getJson
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
        data = getJson.getNight_json(touser, kind)
        sendMessage.send_message(access_token, data)
