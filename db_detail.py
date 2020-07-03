import requests
from pyquery import PyQuery as pq
import json


def getDbMovieDetial():
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.162 Safari/537.36"}
    url = "https://movie.douban.com/subject/1291546/"
    req = requests.get(url, headers=kv)
    req.encoding = 'utf-8'
    html = req.text
    doc = pq(html)
    title = doc("h1").text()
    print(title)
    detail = doc(".subject div[id=info]").text()
    print(detail)
    info = doc(".related-info h2 i")
    print(info.text())
    content = doc(".related-info div[id=link-report]")
    print(content.find("span").eq(-2).text())


getDbMovieDetial()
