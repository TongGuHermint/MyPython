import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs
import pandas as pd


def get_detail_json_data(page):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=2317340019&luicode=10000011&lfid=2317120001&page='+str(page)
    print(url)
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
        # "cookies": "SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; tt_webid=6841732822202975751; tt_webid=6841732822202975751; __tasessionId=ux5xozmie1592977446034; __ac_nonce=05ef2e82a00855b57c674; __ac_signature=_02B4Z6wo00f01.qVyewAAIBBuWvDQ8uoIZv6kM1AAKBhcaYO0Fqjv8WtiBxjFTE3HA4puRMNVrSPO-sFILnX317ytzUmsotGlVGUSFhGuuVp77vwNLlcKDnOWJVpjKp3cMmJbMRjZvyspqzLcd; tt_scid=Jfnsvvtv0TkQa85wPNC--i2mSHnx0usDGaJ495A7-S4OC9rCfUTPMWfJP8.8ohn-be75"
    }
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        print(response.text)
        json_data = json.loads(response.text)
        # if len(json_data['data']['cards']) > 0:
        #     for n, item in enumerate(json_data['data']['cards'], 0):
        #         user_item = json_data['data']['cards'][n]['card_group'][0]['user']
        #         print(item)
        #         print(user_item)
        #         user_id.append(json_data['data']['cards'][n]['card_group'][0]['user']['id'])
        #         user_name.append(json_data['data']['cards'][n]['card_group'][0]['user']['screen_name'])
        #         user_img.append(json_data['data']['cards'][n]['card_group'][0]['user']['profile_image_url'])
        #         user_url.append(json_data['data']['cards'][n]['card_group'][0]['user']['profile_url'])
        return json_data


# 热门人物榜
def get_start():
    is_go_on = True
    page = 0
    user_id = []
    user_name = []
    user_img = []
    user_url = []
    while is_go_on:
        page = page + 1
        print("*****************No."+str(page)+"*****************")
        jsons_data = get_detail_json_data(page)
        try:
            if len(jsons_data['data']['cards']) > 0:
                for n, item in enumerate(jsons_data['data']['cards'], 0):
                    user_item = jsons_data['data']['cards'][n]['card_group'][0]['user']
                    print(item)
                    print(user_item)
                    user_id.append(jsons_data['data']['cards'][n]['card_group'][0]['user']['id'])
                    user_name.append(jsons_data['data']['cards'][n]['card_group'][0]['user']['screen_name'])
                    user_img.append(jsons_data['data']['cards'][n]['card_group'][0]['user']['profile_image_url'])
                    user_url.append(jsons_data['data']['cards'][n]['card_group'][0]['user']['profile_url'])
            else:
                is_go_on = False
                # 输入
                writer = pd.ExcelWriter('D:/pachong/weibo/weibo.xlsx')
                j_data = {'user_id': user_id,
                          'user_name': user_name,
                          'user_img': user_img,
                          'user_url': user_url}
                df2 = pd.DataFrame(data=j_data,
                                   columns=['user_id', 'user_name', 'user_img', 'user_url'])
                #  不写index会输出索引
                df2.to_excel(writer, 'Sheet2', index=False)
                writer.save()
        except Exception as e:
            break


get_start()

