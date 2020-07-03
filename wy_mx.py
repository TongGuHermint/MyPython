import time
import json

import requests
from pyquery import PyQuery as pq
from urllib import parse


def get_wymx(page):
    # area = 1内地 2港台 3欧美 4日韩 999其他
    url = 'http://ent.sina.com.cn/ku/star_search_index.d.html?area=999&page='+str(page)
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    }
    res = requests.get(url, headers=hd)
    res.encoding = 'utf-8'
    doc = pq(res.text)
    # print(doc('.module-box ul'))
    # data = doc('.tv-list')
    # print(data.text())
    j_list = []
    for n, item in enumerate(doc('.tv-list li').items(), 1):
        print(n)
        print(item.text())
        info = item.find('a').attr('href')
        img = item.find('img').attr('src')
        print('主页:'+info)
        print('img:http:'+img)
        item_data = {
            'url': info,
            'img': 'http:'+img,
            'info': item.text()
        }
        j_list.append(item_data)
    if len(j_list) > 0:
        data = {
            'data': j_list
        }
        jd = json.dumps(data)
        f = open("D://pachong//mx//mx_qt_"+str(page)+'.json', 'w', encoding="utf-8")
        f.write(jd)
        f.close()


for page in range(220):
    print('page--->'+str(page+1))
    get_wymx(page+1)
