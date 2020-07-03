
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)
print("*********运算********")
# 除法运算  /
# 余数  %
# 除法运算（只取整数）  //
# 加 减 乘  + - *
# 乘方 **
a = 11/3
print("11 / 3 得:", 11 / 3)
print("11 % 3 得:", 11 % 3)
print("11 // 3 得:", 11 // 3)
print("2 ** 3 得:", 2 ** 3)
# 反斜杠 \ 可以用来转义
print('doesn\'t')
# 如果你不希望前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可:
print(r'C:\users\nao')
# 字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。
# 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("*********字符串********")
# 字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:
print("a"*3 + "b")
# 相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.把很长的字符串拆开分别输入的时候尤其有用:
text = ('Put several strings within parentheses '
       'to have them joined together.')
print(text)
# 字符串是可以被 索引 （下标访问）的，第一个字符索引是 0。单个字符并没有特殊的类型，只是一个长度为一的字符串:
# 索引也可以用负数，这种会从右边开始数,注意 -0 和 0 是一样的，所以负数索引从 -1 开始:
text2 = "Son of Bitch"
print(text2[0])
print(text2[1])
print(text2[-1])
# 除了索引，字符串还支持 切片。索引可以得到单个字符，而 切片 可以获取子字符串:
print(text2[0:3])
# 注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
# 切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:
print(text2[:3])
print(text2[:-3])
print(text2[3:])
print(text2[-3:])
print(text2[:3]+text2[3:])
# 内建函数 len() 返回一个字符串的长度:
print(len(text2))
print("*********列表********")
# Python 中可以通过组合一些值得到多种 复合 数据类型。其中最常用的 列表 ，可以通过方括号括起、逗号分隔的一组值（元素）得到。
# 一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同:
list = [1, 2, 4, 8, 16, 32, 64]
print(list)
# 和字符串（以及各种内置的 sequence 序列类型）一样，列表也支持索引和切片:
print(list[0])
print(list[2])
print(list[2:])#    数字在：前  取包括list[2]之后的数据 包括list[2]
print(list[-2:])
print(list[:2])#   数字在：后 取包括list[2]之前的数据 不包括list[2]
print(list[:-2])
#  通过 append() 方法 来添加新元素 和 对元素赋值
# 内置函数 len() 也可以作用到列表上:
list.append(128)
print(list)
print(len(list))
list[0] = 0
print(list)
# 给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:
list[1:4] = [3, 9, 81]
print(list)
list[1:4] = []
print(list)
list[:] = []
print(list)
# 也可以嵌套列表 (创建包含其他列表的列表), 比如说:
x = ['a', 'b', 'c']
y = [1, 2, 3]
z = [x, y]
print(z)
print(z[0])
print(z[0][0])
# print("*********if elif ********")
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('比0小')
# elif x == 0:
#     print("0")
# elif x > 0:
#     print("比0大")
print("*********for ********")
# range()  enumerate(iterable, start=0)
a = ['a', 'b', 'c', 'd', 'e']
for i in range(len(a)):
    print(i, a[i])
print("********* def ********")
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print("*********爬虫开始 ********")

import requests

kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}      # 是一个标准的浏览器的身份标识的字段
url = "http://www.zhihu.com"
r = requests.get(url, headers=kv)        #注意这里要加headers，因为headers已经更该过。
print("\nr的类型" + str(type(r)))

print("\n状态码是:" + str(r.status_code))

print("\n头部信息:" + str(r.headers))

print("\nurl:" + str(r.url))

print("\n响应内容:")

print(r.text)

#保存文件
file = open('D://pachong//new//ss.html', 'w', encoding="utf")
#打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制

file.write(r.text)

file.close()









