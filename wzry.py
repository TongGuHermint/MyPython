import time
import json

import requests
from pyquery import PyQuery as pq
from urllib import parse


def get_mx():
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    }
    res = requests.get(url, headers=kv)
    print(res.text)
    js_data = json.loads(res.text)
    for item in js_data:
        id = str(item['ename'])
        if id == '518':
            skin = '冷晖之枪|幸存者|神威'
        else:
            skin = item['skin_name']
        for i in range(len(str(skin).split('|'))):
            print(str(i+1))
            img_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+id+'/'+id+'-bigskin-'+str(i+1)+'.jpg'
            print(img_url)
            file_data = requests.get(img_url).content
            file_name = str(img_url).split('/')[-1]
            f = open("D://pachong//wzry//" + file_name, 'wb')
            f.write(file_data)
            f.close()


get_mx()
