import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# RuntimeWarning: Glyph 38388 missing from current font.
#   font.set_text(s, 0.0, flags=flags)
# 解决此问题加如下两行
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

df = pd.read_csv('D:/pachong/biao/aishare_day_20200628.csv')  # 读取xlsx中第一个sheet
print(df)
# df.plot.pie(subplots=True)
data = df.loc[0].values
print(data)
data = df.loc[1].values
print(data)
time_list = df.iloc[:, 0].values
user_list = df.iloc[:, 1].values
per_list = df.iloc[:, 2].values
print(time_list)
print(user_list)
print(per_list)
label = ["1秒-3秒", "4秒-10秒", "11秒-30秒", "31秒-1分", "1分-3分", "3分-10分", "10分-30分", "30分+ "]
# user_list = [101,  213,  540,  686, 2370, 2824, 1499,  761]
# per_list = [0.012, 0.0237, 0.06, 0.0763, 0.2635, 0.314, 0.1667, 0.0846]
temp = {
        'per': per_list}

explode = [0, 0, 0, 0.1, 0, 0, 0, 0]

# 饼状图
# plt.axes(aspect=1)
# plt.pie(x=per_list,
#         labels=label,
#         autopct='%3.1f %%',
#         explode=explode)
# plt.title('爱享云日均使用时长')
# plt.show()

# 柱状图
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.2, 1.03 * height, '%s' % int(height))


autolabel(plt.bar(range(len(user_list)), user_list, tick_label=time_list))
# plt.bar(range(len(user_list)), user_list, tick_label=label) # 最简 没有详细数据
plt.title('爱享云日均使用时长')
plt.show()
