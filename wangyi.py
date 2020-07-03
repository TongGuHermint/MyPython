import requests
from pyquery import PyQuery as pq


def getArticle(limit, offset):
    # url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit='+limit+'&offset='+offset
    url = 'https://music.163.com/discover/playlist/?cat=全部&order=hot&limit='+limit+'&offset='+offset
    print(url)
    header = {
        # 'cookie': '_iuqxldmzr_=32; _ntes_nnid=69aed684adc5f0fe6721769e529bff47,1586749468447; _ntes_nuid=69aed684adc5f0fe6721769e529bff47; WM_TID=TjqC3XWvRx9FBABRARZrRy8SyEpj6zxE; UM_distinctid=171a5f4a43a677-02741c15b52234-3f6b4b04-1fa400-171a5f4a43bae7; __root_domain_v=.163.com; _qddaz=QD.rrb5zs.uxhjh8.k9kxs6ux; ntes_kaola_ad=1; MUSICIAN_COMPANY_LAST_ENTRY=1379972374_musician; MUSIC_U=9de0b492647e4661c3304025ecce79afd8b923ac5e21ec2e7d489653eb498862b3dada19dbba5eb65da9625e97c20bb7735310822213e475bf122d59fa1ed6a2; __csrf=3beb24143ab87a450960d4f20eab5c0b; vinfo_n_f_l_n3=52b8818c91555ca6.1.3.1587627204332.1592193298194.1592465627109; JSESSIONID-WYYY=dxH7BdxRhXBQ9T%2Fj%2BgnBRgSJAGzBrZi%5Ctl%5CNXEurQsZAlszYtEC7uOkJm%2FBaQko2qpe9DgQRRtIqfehSS72aONEKsthCNYg1Gpb%2BNxSc7qtZW7BIN1wX%2BnQiVVziDsmBKwlyXfUOSloqeYuaN%2F65hFPwe%2BQT53n62xFe%5CSldhNBBhj%5CQ%3A1593487213235; WM_NI=IqzxkkK9%2BcJVyhlm%2Bpjm2vB%2BVqEi1r3Or7xSsmGBk6FCnNULC2WMlDTScHpQhyA5BNlAIc%2BWzCm8IzlPMNTvYGn7rLkLgb9cQnmrB9j2WZKy3LolJhoyCtcfT2ovI3lEY3c%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8bf26095bdfd86e933f2ef8fb2c84b879e8a85aa59bc9aaeb9c56ef4ee8a88c12af0fea7c3b92a8bafb699ea6189e7e584c95ebbb8a48eaa7caab3fe97c12196af8b8ab47af191bed8fb59b1b389a3ea3e869da2afd84881ee99aeef50988dada9f35baca78fd6c146b09f8784aa5dba9da3d9cc72b09083afd77e9b99a2d8f148a994a983bc6993b2a393c133aaee99bbca73f194a18dc964ada78d95e26e98eea197cc39b09b97d4e237e2a3; playerid=40300610',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = requests.get(url=url, headers=header)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    # 初始化pyquery对象
    doc = pq(html)
    # 传入css选择器
    items = doc('.g-wrap ul li').items()
    count = 0
    for each in items:
        title = each.find('a').attr('title')
        url = each.find('a').attr('href')
        img = each.find('img').attr('src')
        rel_img = img.split("?")[-2]
        # 有的没有url
        if url:
            url = 'https://music.163.com' + url
            rel_img = img.split("?")[-2]
            # if count == 5:
            #     print("**** 获取结束 ****")
            #     break
            # count = count + 1
            print("-----------------" +
                  "\n标题:" + title +
                  "\n详情:" + url +
                  "\n图片:" + img)

            file_name = str(rel_img).split('/')[-1]
            file_rel_name = str(file_name).split('.')[-2]
            file_data = requests.get(rel_img).content
            file_data_s = requests.get(img).content
            f = open("D://pachong//wyy//imgs//"+file_name, 'wb')
            f.write(file_data)
            f.close()
            fs = open("D://pachong//wyy//imgs//"+file_rel_name+"_s.jpg", 'wb')
            fs.write(file_data_s)
            fs.close()


if __name__ == '__main__':
    limit = 35
    offset = 0
    for i in range(2):
        offset = offset + limit * i
        print(i)
        print(offset)
        getArticle(str(limit), str(offset))
