import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs
import pandas as pd
import threading


# https://m.weibo.cn/

def get_detail_json_data():
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=cate%3D10103%26pos%3D0_0%26mi_cid%3D100103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time%3D1593396839&luicode=10000011&lfid=231583'
    print(url)
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
        # "cookies": "_T_WM=65200200671; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=lfid%3D2317340019%26luicode%3D20000174; XSRF-TOKEN=64d7a5"
    }
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        print(response.text)
        json_data = json.loads(response.text)
        return json_data


# 电影微博
def get_start():
    now = int(time.time())  # 1533952277
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray)
    print(otherStyleTime)
    jsons_data = get_detail_json_data()
    try:
        for n, item in enumerate(jsons_data['data']['cards'][0]['card_group'], 0):
            print(item)
            desc = jsons_data['data']['cards'][0]['card_group'][n]['desc']
            print(desc)
            scheme = jsons_data['data']['cards'][0]['card_group'][n]['scheme']
            print(scheme)
            if n > 0:
                desc_extr = str(jsons_data['data']['cards'][0]['card_group'][n]['desc_extr'])
                print(desc_extr)
            else:
                desc_extr = ""
            f = open('D://pachong//weibo//'+'wb_top_'+otherStyleTime+'.txt', 'a', encoding="utf-8")
            f.write("\n----------------------------------------------------"
                    + "\n"+desc
                    + "\n"+scheme
                    + "\n热度:"+desc_extr)
            f.close()
    except Exception as e:
        print(e)


# 真正要执行的函数
def t1():
    get_start()


# 每隔10秒钟执行
def t2():
    while 1:
        t1()
        time.sleep(30)


if __name__ == '__main__':
    t = threading.Thread(target=t2)
    t.start()
    print("主线程")
    t.join()




