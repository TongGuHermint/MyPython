import requests
from pyquery import PyQuery as pq
import json

# 提取标签(find)、筛选属性(filter)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36
jlist = []


def getDouBanMovieList(start):
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.162 Safari/537.36"}  # 是一个标准的浏览器的身份标识的字段
    url = "https://movie.douban.com/top250?start=%s&filter=," % start
    req = requests.get(url, headers=kv)
    req.encoding = 'utf-8'
    html = req.text

    doc = pq(html)

    items = doc('.article ol li').items()
    count = 1
    print("**** 获取开始 ****")
    for each in items:
        # title = each.text()
        # url = each.find('.hd a span[class=title]')
        img = each.find('.pic em')
        imgurl = each.find('.pic a img').attr("src")
        title = each.find('.hd')
        arts = each.find('.bd p[class=""]')
        point = each.find('.star span[class=rating_num]')
        quote = each.find('.bd p[class=quote]')
        nexturl = each.find('.hd a').attr("href")
        img = img.text()
        title = title.text()
        arts = arts.text()
        point = point.text()
        quote = quote.text()
        # if count == 6:
        #     print("**** 获取结束 ****")
        #     break
        # count = count + 1
        print("-------" + img + "-------")
        print("标题--->：" + title)
        print("人员--->：" + arts)
        print("评分--->：" + point)
        print("引用--->:" + quote)
        print("图片地址--->" + imgurl)
        ij = {
            'id': img,
            'title': title,
            'arts': arts,
            'point': point,
            'quote': quote,
            'imgUrl': imgurl
        }
        j = json.dumps(ij)
        jlist.append(ij)
        print(j)
        file = open("D://pachong//douban//movie//top250.txt", 'a', encoding="utf-8")
        file.write("\n-------" + img + "-------"
                   + "\n标题--->：" + title
                   + "\n人员--->：" + arts
                   + "\n评分--->：" + point
                   + "\n引用--->:" + quote
                   + "\n图片地址--->" + imgurl)

        file.close()
        if nexturl:
            getDbMovieDetial(nexturl)
    if start == 25:
        jfile = open("D://pachong//douban//movie//top250.json", 'w', encoding="utf-8")
        lidi = {
            'data': jlist
        }
        jlistdi = json.dumps(lidi)
        jfile.write(jlistdi)
        jfile.close()


def getDbMovieDetial(nextUrl):
    kv = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.162 Safari/537.36"}
    url = nextUrl
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
    file = open("D://pachong//douban//movie//top250_content.txt", "a", encoding="utf-8")
    file.write("\n-------" + title + "-------"
               + "\n" + detail
               + "\n" + info.text()
               + "\n" + content.find("span").eq(-2).text())
    file.close()


start = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225]
# start = [0, 25]

for i in start:
    print("start------------->", i)
    getDouBanMovieList(i)
