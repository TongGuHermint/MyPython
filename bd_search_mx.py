import requests
from pyquery import PyQuery as pq
from urllib import parse


def get_mx():
    name = input("请输入明星姓名：")
    parse.quote(name)
    url = 'https://baike.baidu.com/item/'+parse.quote(name)+'?fr=aladdin'
    print(url)
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
    }
    res = requests.get(url, headers=kv)
    html = res.text
    doc = pq(html)
    print("-----------简介---------")
    info = doc.find('.lemma-summary')
    info.remove('sup')
    print(info.text())
    print("-----------代表作品---------")
    movie = doc('#slider_works')
    print(movie.text())
    print("-----------明星关系---------")
    relation = doc('#slider_relations')
    print(relation.text())


get_mx()
