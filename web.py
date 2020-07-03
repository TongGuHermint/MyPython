import time

from selenium import webdriver


dr = webdriver.Chrome(executable_path="C://Users//dNao//AppData//Local//Programs//Python//Python38//chromedriver.exe")#初始化chrome浏览器实例
dr.maximize_window()#浏览器最大化
dr.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%90%9E%E7%AC%91&fenlei=256&rsv_pq=c2f6b9c3000be453&rsv_t=95e8u0po2hJl1pJk2nV8f8YASW8FBj5j02GsbSsktIDWXw8IKdiQIU%2BUm4I&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=2&rsv_btype=i&inputT=85&rsv_sug4=85')#打开百度首页
# test = dr.find_element_by_id('kw')#通过id属性定位输入框
# test.send_keys('搞笑')#输入测试一下
# btn = dr.find_element_by_id('su')
# btn.click()
# time.sleep(2)
# item = dr.find_element_by_class_name('opr-recommends-merge-mask')
# item = dr.find_element_by_xpath("//h3[contains(@class,'t')]")
# item = dr.find_element_by_link_text("笑话大全_污段子大全_<em>搞笑</em>段子_<em>搞笑</em>图片大全_傲游哈哈")
item = dr.find_elements_by_link_text("逗比")

item[1].click()

dr.quit()

