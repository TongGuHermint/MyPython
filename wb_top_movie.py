import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs
import pandas as pd


# https://m.weibo.cn/
# containerid
# 榜单 102803_ctg1_8999_-_ctg1_8999_home
# 电影 102803_ctg1_3288_-_ctg1_3288
def get_detail_json_data():
    url = 'https://m.weibo.cn/api/feed/trendtop?containerid=102803_ctg1_8999_-_ctg1_8999'
    print(url)
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
        "cookies": "_T_WM=65200200671; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=lfid%3D2317340019%26luicode%3D20000174; XSRF-TOKEN=64d7a5"
    }
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        print(response.text)
        json_data = json.loads(response.text)
        return json_data


# 电影微博
def get_start():
    jsons_data = get_detail_json_data()
    try:
        if len(jsons_data['data']['statuses']) > 0:
            for n, item in enumerate(jsons_data['data']['statuses'], 0):
                print(item)
                user_name = jsons_data['data']['statuses'][n]['user']['screen_name']
                print(user_name)
                content = jsons_data['data']['statuses'][n]['text']
                # c = str(content).replace(u'\xa0', u'')
                c = str(content)
                print(content)
                f = open('D://pachong//weibo//wb.json', 'a', encoding="utf-8")
                f.write("\n昵称：" + user_name
                        + "\n内容：" + c
                        + "\n")

        else:
            is_go_on = False
    except Exception as e:
        print(e)


get_start()
