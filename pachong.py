import requests
from pyquery import PyQuery as pq


def getArticle():
    url = 'http://www.shengxu5w.com/11_11217/'
    req = requests.get(url=url)
    req.encoding = 'gbk'
    html = req.text
    # print(html)
    # 初始化pyquery对象
    doc = pq(html)
    # 传入css选择器
    items = doc('.box_con dl dd').items()
    print("**** 开始获取最新9章 ****")
    count = 1
    for each in items:
        title = each.text()
        url = each.find('a').attr('href')
        # 有的没有url
        if url:
            url = 'http://www.shengxu5w.com' + url
            if count == 10:
                print("**** 获取结束 ****")
                break
            count = count + 1
            print(title, url)
            Text(title, url)


def Text(title, url):
    print('正在提取:', url)
    req = requests.get(url=url)
    req.encoding = 'gbk'
    html = req.text
    doc = pq(html)
    item = doc('.box_con div[id=content]').text()
    print(item)

    path = 'D://pachong//new//' + title + '.txt'
    # 保存文件
    # file = open(path, 'w', encoding="utf-8")
    file = open("D://pachong//new//%s.txt" % title, 'w', encoding="utf-8")

    # 打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制

    file.write(item)

    file.close()


getArticle()
