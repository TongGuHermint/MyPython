import requests
from pyquery import PyQuery as pq
import json
import math
import time
import hashlib
import execjs
import pandas as pd
from urllib import parse


def get_detail_json_data(name):
    # name = input('请输入搜索关键词：')
    # # name = '秦昊'
    # name = '伊能静'
    print('\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>正在爬取 '+name+' <<<<<<<<<<<<<<<<<<<<<<<<')
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type'+parse.quote('=1&q='+name)+'&page_type=searchall'
    print(url)
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
        # "cookies": "SLARDAR_WEB_ID=e8fb43b7-b8d2-4290-878f-75ae79b35974; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=76ec6a61c5eb86edf99f0da8d8621d90; ttcid=97a887f7191d4378b26b570e86d745c130; s_v_web_id=verify_kbsnotle_k2ciOQH5_vJ8o_4gR5_B96c_pE3SiBlo2yQo; tt_webid=6841732822202975751; tt_webid=6841732822202975751; __tasessionId=ux5xozmie1592977446034; __ac_nonce=05ef2e82a00855b57c674; __ac_signature=_02B4Z6wo00f01.qVyewAAIBBuWvDQ8uoIZv6kM1AAKBhcaYO0Fqjv8WtiBxjFTE3HA4puRMNVrSPO-sFILnX317ytzUmsotGlVGUSFhGuuVp77vwNLlcKDnOWJVpjKp3cMmJbMRjZvyspqzLcd; tt_scid=Jfnsvvtv0TkQa85wPNC--i2mSHnx0usDGaJ495A7-S4OC9rCfUTPMWfJP8.8ohn-be75"
    }
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        print(response.text)
        json_data = json.loads(response.text)
        return json_data


# 热门人物榜
def get_start(name):
    is_go_on = True
    page = 0
    dto = get_detail_json_data(name)
    n = 0
    # 判断是否有热搜引导词 card_type = 4
    if dto['data']['cards'][0]['card_type'] == 4:
        print(dto['data']['cards'][0]['desc'])
        print(dto['data']['cards'][0]['scheme'])
        n = n+1
    # 判断是否有明星微博 相关用户
    if dto['data']['cards'][n]['card_type'] == 11:
        info = dto['data']['cards'][n]['card_group'][0]
        if len(dto['data']['cards'][n]['card_group']) > 2:
            print('--------[明星微博信息]--------')
            user_id = info['user']['id']
            screen_name = info['user']['screen_name']
            profile_image_url = info['user']['profile_image_url']
            profile_url = info['user']['profile_url']
            desc1 = info['desc1']
            desc2 = info['desc2']
            print('id:' + str(user_id))
            print('screen_name:' + screen_name)
            print('头像:' + profile_image_url)
            print('主页:' + profile_url)
            print('desc1:' + desc1)
            print('desc2:' + desc2)

        # 相关用户
        user_list = dto['data']['cards'][n]['card_group'][-2]['users']
        print('--------[相关用户]--------')
        for item in user_list:
            print('********')
            # print(item['screen_name'] + '\n头像：' + item['profile_image_url'] + '\n主页：' + item['profile_url'])
            print(item['screen_name'] + '\n头像：' + item['profile_image_url'])
        if dto['data']['cards'][n]['card_group'][-1]['card_type'] == 19:
            group = dto['data']['cards'][n]['card_group'][-1]['group']
            for g in group:
                print('--------[' + g['item_title'] + ']--------')
                print(g['item_desc'])
                print(g['scheme'])
            print('----------------')
        else:
            group = dto['data']['cards'][n]['card_group'][-1]
            print('--------[' + group['desc'] + ']--------')
            print(group['desc_extr'])
            print(group['scheme'])
        n = n + 1
    # 精选微博 9  2条
    if dto['data']['cards'][n]['card_type'] == 9:
        if dto['data']['cards'][n]['mblog']['title']['text']=='精选':
            print('--------[精选微博]--------')
            special_items = dto['data']['cards'][n]
            print('**************')
            print(special_items['mblog']['user']['screen_name'] + '----' + special_items['mblog']['created_at'])
            print(special_items['mblog']['raw_text'])
            print(special_items['scheme'])
            special_item = dto['data']['cards'][n + 1]['card_group'][0]
            print('***************')
            print(special_item['mblog']['user']['screen_name'] + '----' + special_item['mblog']['created_at'])
            print(special_item['mblog']['raw_text'])
            print(special_item['scheme'])
            print('----------------')
            n = n + 2
    # 热门微博 9  2条
    print('--------[热门微博]--------')
    for hot_items in dto['data']['cards'][n:n+2]:
        print('**************')
        print(hot_items['mblog']['user']['screen_name'] + '----' + hot_items['mblog']['created_at'])
        print(hot_items['mblog']['raw_text'])
        print(hot_items['scheme'])
    # 热门微博  11-->9  1条(结尾)
    hot_item = dto['data']['cards'][n+2]['card_group'][0]
    print('**************')
    print(hot_item['mblog']['user']['screen_name'] + '----' + hot_item['mblog']['created_at'])
    print(hot_item['mblog']['raw_text'])
    print(hot_item['scheme'])
    print('----------------')
    n = n + 3
    # 热门视频
    video = dto['data']['cards'][n]['card_group'][0]
    if video['desc'] == '热门视频':
        print('--------[' + video['desc'] + ']--------')
        print(video['scheme'])
        video_item = dto['data']['cards'][n]['card_group'][1]['items']
        for v_item in video_item:
            print('**************')
            print(v_item['title'])
            print(v_item['scheme'])
        print('----------------')
        n = n + 1

    # 热门文章 11-->42 -->8/27(要登陆)
    article = dto['data']['cards'][n]['card_group'][0]
    if article['desc'] == '热门文章':
        print('--------[' + article['desc'] + ']--------')
        print(article['scheme'])
        article_item = dto['data']['cards'][n]['card_group'][1:4]
        for a_item in article_item:
            if a_item['card_type'] == 8:
                print('**************')
                print(a_item['title_sub'])
                print(a_item['desc1'])
                print(a_item['scheme'])
        n = n + 1

    # 判断有没有超话
    judge = dto['data']['cards'][n]['card_group'][0]['card_type']
    if judge == 42:
        # 超话 11-->42 -->16
        s_topic = dto['data']['cards'][n]['card_group']
        print('--------[' + s_topic[0]['desc'] + ']--------')
        print(s_topic[0]['scheme'])
        for topic_item in s_topic[2]['group']:
            print('**************')
            print(topic_item['title_sub'])
            print(topic_item['scheme'])
        n = n + 1
    # 实时微博 11-->9  1条(开头)
    print('--------[' + dto['data']['cards'][n]['title'] + ']--------')
    blog_top = dto['data']['cards'][n]['card_group'][0]
    print('**************')
    print(blog_top['mblog']['user']['screen_name'] + '----' + blog_top['mblog']['created_at'])
    print(blog_top['mblog']['raw_text'])
    print(blog_top['scheme'])
    n = n + 1
    # 实时微博 9
    for blog in dto['data']['cards'][n:-1]:
        print('**************')
        print(blog['mblog']['user']['screen_name'] + '----' + blog['mblog']['created_at'])
        print(blog['mblog']['raw_text'])
        print(blog['scheme'])


# get_start()

# name_list = ['伊能静', '秦昊']
# for name in name_list:
#     get_start(name)
get_start(input('请输入搜索关键词：'))

