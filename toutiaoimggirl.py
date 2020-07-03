import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs
import urllib.parse
import os


def getTouTiaoGossip():
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"}
    url = "https://www.toutiao.com/ch/gossip/"
    req = requests.get(url, headers=kv)
    req.encoding = 'utf-8'
    html = req.text
    doc = pq(html)
    print(doc.text())


def getHoney():
    e = math.floor(int(str(time.time() * 1000).split('.')[0]) / 1e3)  # 获取13位毫秒数然后除于1e3再向下取整
    i = str('%X' % e)  # 转换e为16进制
    m5 = hashlib.md5()
    m5.update(str(e).encode('utf-8'))
    t = str(m5.hexdigest()).upper()  # 进行md5加密
    if 8 != len(i):
        return {'as': '479BB4B7254C150', 'cp': '7E0AC8874BB0985'}
    o = t[0:5]
    n = t[-5:]
    a = ""
    r = ""
    for x in range(5):  # 交换字符串
        a += o[x] + i[x]
        r += i[x + 3] + n[x]
    return {'as': "A1" + a + i[-3:], 'cp': i[0:3] + r + "E1"}


def get_json(offset, keyword):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'cookie': 'SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; __tasessionId=n5fbbfr9o1592980843327; __ac_nonce=05ef2fa14002f9a198955; __ac_signature=_02B4Z6wo00f01egEvgwAAIBDq.q0o.TH4yXoALqAACT2c6S02TEtwaANIKuAj58MfYkNcG01G51wvvZ3W.bs5sLKi1xwq49Mj8YH8J3kl0bGbz2t5xFvnbAx-os6-eL.4FVEaD464JVMEv.Z56; tt_webid=6841805780213270029; tt_webid=6841805780213270029; tt_scid=ZEkhjBCLNiVVF4J8pzbWNYBY01dQBsAG4.v6ARTZr---MekEj1HBoi0uKTIaLobOfc62'
    }
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={offset}&format=json&keyword={keyword}&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'.format(
         offset=offset, keyword=keyword)
    print(url)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)

    resp_json = json.loads(response.text)
    return resp_json

def get_js():
    f = open('D://pachong//toutiao//sign.js', 'r', encoding='utf-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def get_signature(user_id,max_behot_time):
    jsData = get_js()
    node = execjs.get(execjs.runtime_names.Node)
    ctx = node.compile(jsData).call('test', str(user_id) + str(max_behot_time))  #复原TAC.sign(userInfo.id + "" + i.param.max_behot_time)
    return ctx


def get_detail(urlpath):
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.162 Safari/537.36"}
    req = requests.get(urlpath, headers=kv)
    html = req.text
    doc = pq(html)
    item = doc(".article-box h1")
    print(item.text())


if __name__ == '__main__':
    url = 'https://www.toutiao.com/api/search/content'  # url为用户文章和视频的源
    key = urllib.parse.quote(input("请输入要搜的图片："))
    user_id = ""
    # user_id = url.split('/')[-2]  # 获取用户user_id，等同于js中的userInfo.id
    max_behot_time = 0  # _signature参数生成需要，并且赖加载时也需要此参数
    isDown = True  # 一直获取数据
    page_type = 1  # 0为视频，1为文章
    offset = 0
    while isDown:  # 解决懒加载问题
        as_cp = getHoney()
        print(getHoney())
        print(user_id)
        print(max_behot_time)
        signature = get_signature(user_id, max_behot_time)
        print("sign", signature)
        timestamp = int(round(time.time() * 1000))
        print("timestamp", timestamp)
        toutiao_json = get_json(offset, key)
        print(toutiao_json)
        if page_type:
            try:
                for n, item in enumerate(toutiao_json['data'], 0):
                    print("n", n)
                    print("item", item)
                    try:
                        appinfo = toutiao_json['data'][n]['app_info']
                        if 'VIDEO' not in toutiao_json['data'][n]['app_info']['db_name']:
                            try:
                                imgList = toutiao_json['data'][n]['image_list']
                                print("imgList", imgList)
                                file_box = "D://pachong//toutiao//img_type//" + toutiao_json['data'][n]['title'] + "//"
                                os.mkdir(file_box)
                                for j, imgurl in enumerate(imgList, 0):
                                    url = toutiao_json['data'][n]['image_list'][j]['url']
                                    print("j", j)
                                    print("imgurl", imgurl)
                                    if 'http' in url:
                                        if '190x124' in url:
                                            new_url = str(url).replace("list/190x124", "large")
                                        else:
                                            new_url = str(url).replace("list", "large")
                                        print("url", new_url)
                                    else:
                                        url = "http:" + url
                                        if '190x124' in url:
                                            new_url = str(url).replace("list/190x124", "large")
                                        else:
                                            new_url = str(url).replace("list", "large")
                                        print("url", new_url)
                                    img_req = requests.get(new_url, allow_redirects=True)
                                    print(img_req.headers.get("Content-Type"))
                                    file_data = img_req.content
                                    file_name = url.split("/")[-1]
                                    path = ""
                                    if img_req.headers.get("Content-Type") == "image/jpeg":
                                        path = file_box + file_name + ".jpeg"
                                    elif img_req.headers.get("Content-Type") == "image/gif":
                                        path = file_box + file_name + ".gif"
                                    with open(path, 'wb') as handler:
                                        handler.write(file_data)
                            except Exception as e:
                                continue
                        else:
                            print('这是视频')
                    except Exception as e:
                        continue
                # has_more = toutiao_json['has_more']  # 获取是否还有下一页数据
                has_more = True
                if not has_more:  # 用来判断是否没有下一页了
                    isDown = False
                    break
                else:
                    offset = offset + 20
            except Exception as e:
                isDown = False
                print(e)
                break
        else:
            try:
                max_behot_time = toutiao_json['next']['max_behot_time']  # 数据为空就没有这个选项从而引发try
                print('视频数据：%s' % str(toutiao_json))
                has_more = toutiao_json['has_more']  # 获取是否还有下一页数据
                if not has_more:  # 用来判断是否没有下一页了
                    isDown = False
                    break
            except Exception as e:
                break

# if __name__ == '__main__':
# 	print(getHoney())

