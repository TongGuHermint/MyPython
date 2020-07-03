import time
import json

import requests
from pyquery import PyQuery as pq
from urllib import parse


def get_mx():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    }
    res = requests.get(url, headers=kv)
    print(res.text)
    js_data = json.loads(res.text)
    for item in js_data['hero']:

        print("\n|-----------------" +
              "\n|-----  " + item['heroId'] + "  -----" +
              "\n|-----  " + item['name'] + "  -----" +
              "\n|-----  " + item['alias'] + "  -----" +
              "\n|-----------------")
        info_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/'+item['heroId']+'.js'

        info_res = requests.get(info_url, headers=kv)
        print(info_res.text)
        info_data = json.loads(info_res.text)
        for skin_item in info_data['skins']:
            if skin_item['mainImg'] != '':
                img = skin_item['mainImg']
                file_data = requests.get(img).content
                rel_img = str(img).split('/')[-1]
                print(img)
                f = open("D://pachong//lol//" + rel_img, 'wb')
                f.write(file_data)
                f.close()
            else:
                xc_img = skin_item['chromaImg']
                print(xc_img)
                file_xc_data = requests.get(xc_img).content
                rel_chromas_img = str(xc_img).split('/')[-4]+"_"+str(xc_img).split('/')[-3]+"_"+str(xc_img).split('/')[-2]+str(xc_img).split('/')[-1]
                f = open("D://pachong//lol//" + rel_chromas_img, 'wb')
                f.write(file_xc_data)
                f.close()


get_mx()
