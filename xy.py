import requests


import json
from pyquery import PyQuery as pq
import http.client
# http.client.HTTPConnection._http_vsn = 10
# http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

# def get_json():
#     headers = {
#         'Host': 'toupiao.jyqnet.com',
#         'Origin': 'http://toupiao.jyqnet.com',
#         'Cookie': 'PHPSESSID=89819e479dcafd567f0bb026bb77e4d9',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
#     }
#     url = 'http://toupiao.jyqnet.com/front/MyActivity/listplayer'
#     data = {'aid': '33',
#             'page': '2',
#             'page_size': '10',
#             }
#     print(url)
#     response = requests.post(url, data=data, headers=headers)
#     print(response.text)
#     resp_json = json.loads(response.text)
#     print(resp_json)


def get_detail():
    url = 'https://www.toutiao.com/group/6841764539009073667'
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
        "cookies": "SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; tt_webid=6841732822202975751; tt_webid=6841732822202975751; __tasessionId=ux5xozmie1592977446034; __ac_nonce=05ef2e82a00855b57c674; __ac_signature=_02B4Z6wo00f01.qVyewAAIBBuWvDQ8uoIZv6kM1AAKBhcaYO0Fqjv8WtiBxjFTE3HA4puRMNVrSPO-sFILnX317ytzUmsotGlVGUSFhGuuVp77vwNLlcKDnOWJVpjKp3cMmJbMRjZvyspqzLcd; tt_scid=Jfnsvvtv0TkQa85wPNC--i2mSHnx0usDGaJ495A7-S4OC9rCfUTPMWfJP8.8ohn-be75"

        # "cookie": "SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; tt_webid=6841732822202975751; tt_webid=6841732822202975751; __ac_nonce=05ef2b9e1001b0abd27b8; __ac_signature=_02B4Z6wo00f01R1.HXAAAIBDXoEX3cdlEYEdexnAABmv91rgbby.hXUnmdyHSj2CmiGD5dOJ5VMtiIsjq704jN6eJlMxCmrvqZnhzUubTkROYTs1HEfVcUKwnrngUPIxk-u7EDcif70UR.oSca; __tasessionId=tej6y67n91592967012778; tt_scid=4Np8oRj5oJ1Djq4Os.xlaeaXvXs1amTHkJ3DvtdCrXUGFO2Gl9HL0vtFpZXTfP8.3670",
        # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "zh-CN,zh;q=0.9",
        # "cache-control": "max-age=0",
        # "upgrade-insecure-requests": "1",
        # "sec-fetch-dest": "document",
        # "sec-fetch-mode": "navigate",
        # "sec-fetch-site": "same-origin",
        # "sec-fetch-user": "?1",
    }
    cookies = "SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; tt_webid=6841732822202975751; tt_webid=6841732822202975751; __tasessionId=ux5xozmie1592977446034; __ac_nonce=05ef2e82a00855b57c674; __ac_signature=_02B4Z6wo00f01.qVyewAAIBBuWvDQ8uoIZv6kM1AAKBhcaYO0Fqjv8WtiBxjFTE3HA4puRMNVrSPO-sFILnX317ytzUmsotGlVGUSFhGuuVp77vwNLlcKDnOWJVpjKp3cMmJbMRjZvyspqzLcd; tt_scid=Jfnsvvtv0TkQa85wPNC--i2mSHnx0usDGaJ495A7-S4OC9rCfUTPMWfJP8.8ohn-be75"
    try:
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError:
        return 'No response'


# get_json()
get_detail()
