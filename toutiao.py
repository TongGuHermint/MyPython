import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs


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


def get_json(user_id, max_behot_time, as_cp, signature, page_type):
    # page_type为0是爬取视频内容，为1是爬取文章内容
    # headers = {
    #     'authority': 'www.toutiao.com',
    #     'method': 'GET',
    #     'path': '/api/pc/feed/?category=gossip&utm_source=toutiao&widen=1&max_behot_time={max_behot_time}&max_behot_time_tmp=0&tadrequire=true&as={as}&cp={cp}&_signature={signature}'.format(
    #         page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp),
    #     'scheme': 'https',
    #     'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'content-type': 'application/x-www-form-urlencoded',
    #     'cookie': 'tt_webid=6841348526758512135; SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; s_v_web_id=verify_kbr905jt_Ek0NiGaY_PKfu_4Q4t_BIDf_o6PknNnxbmJn; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6841348526758512135; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; __tasessionId=nrkq50rpd1592889294325; tt_scid=vHiq-8o23l7UrpwGiPHbnPIPj9wGX8MuHBbTR-UcA8MLRyPX-3kZxsebxMGGJ3Kj97da',
    #     'referer': 'https://www.toutiao.com/ch/gossip/',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-origin',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    #     'x-requested-with': 'XMLHttpRequest'
    # }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    }
    url = 'https://www.toutiao.com/api/pc/feed/?category=gossip&utm_source=toutiao&widen=1&max_behot_time={max_behot_time}&max_behot_time_tmp=0&tadrequire=true&as={as}&cp={cp}&_signature={signature}'.format(
         page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp)
    print(url)
    response = requests.get(url, headers=headers)
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
    url = 'https://www.toutiao.com/api/pc/feed'  # url为用户文章和视频的源
    user_id = url.split('/')[-2]  # 获取用户user_id，等同于js中的userInfo.id
    max_behot_time = 0  # _signature参数生成需要，并且赖加载时也需要此参数
    isDown = True  # 一直获取数据
    page_type = 1  # 0为视频，1为文章
    while isDown:  # 解决赖加载问题
        as_cp = getHoney()
        print(getHoney())
        print(user_id)
        print(max_behot_time)
        signature = get_signature(user_id, max_behot_time)
        print("sign", signature)

        toutiao_json = get_json(user_id, max_behot_time, as_cp, signature, page_type)
        print(toutiao_json)
        # 由于今日头条的反爬虫机制，有时会获取到空的数据，所以需要用try来控制，一般比例是3：1所以是访问3次有一次获得数据
        if page_type:
            try:
                for n, item in enumerate(toutiao_json['data'], 0):
                    print("n", n)
                    print("item", item)
                    group_id = toutiao_json['data'][n]['group_id']
                    print(group_id)
                    print(toutiao_json['data'][n]['title'], "https://www.toutiao.com/a"+group_id)
                    f = open("D://pachong//toutiao//gossip.txt", "a", encoding="utf-8")
                    ij =toutiao_json['data'][n]
                    j = json.dumps(ij)
                    f.write("\n-------" + group_id + "-------"
                            + "\n标题--->：" + toutiao_json['data'][n]['title']
                            + "\n详情页--->：" + "https://www.toutiao.com/a"+group_id
                            + "\n数据--->:" + j)
                    f.close()
                    get_detail("https://www.toutiao.com/a"+group_id)


                max_behot_time = toutiao_json['next']['max_behot_time']  # 数据为空就没有这个选项从而引发try
                print('文章数据：%s' % str(toutiao_json))
                has_more = toutiao_json['has_more']  # 获取是否还有下一页数据
                if not has_more:  # 用来判断是否没有下一页了
                    isDown = False
                    break
            except Exception as e:
                continue
        else:
            try:
                max_behot_time = toutiao_json['next']['max_behot_time']  # 数据为空就没有这个选项从而引发try
                print('视频数据：%s' % str(toutiao_json))
                has_more = toutiao_json['has_more']  # 获取是否还有下一页数据
                if not has_more:  # 用来判断是否没有下一页了
                    isDown = False
                    break
            except Exception as e:
                continue

# if __name__ == '__main__':
# 	print(getHoney())

