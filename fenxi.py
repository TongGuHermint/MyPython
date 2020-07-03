import pandas as pd
import numpy as np

# 索引在左边 值在右边
# s = pd.Series([1, 2, 3, np.nan, 5, 6])
# print(s)

# 生成6行4列位置
# dates = pd.date_range('20180310', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
# print(df['B'])

# 创建特定数据的DataFrame
# df_1 = pd.DataFrame({'A': 1.,
#                      'B': pd.Timestamp('20180310'),
#                      'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                      'D': np.array([3] * 4, dtype='int32'),
#                      'E': pd.Categorical(["test", "train", "test", "train"]),
#                      'F': 'foo'
#                      })
# print(df_1)
# 行的序号
# print(df_1.index)
# 列的序号名字
# print(df_1.columns)
# 把每个值进行打印出来
# print(df_1.values)
# 数字总结
# print(df_1.describe())
# 翻转数据
# print(df_1.T)
# axis等于1按列进行排序 如ABCDEFG 然后ascending倒叙进行显示
# print(df_1.sort_index(axis=1, ascending=False))
# 按值进行排序
# print(df_1.sort_values(by='E'))


df = pd.read_excel('D:/pachong/weibo/weibo.xlsx')  # 读取xlsx中第一个sheet
data1 = df.head(7)  # 读取前7行的所有数据，dataFrame结构
data2 = df.values  # list形式，读取表格所有数据


print("获取到所有的值:\n{0}".format(data1)) #格式化输出
print("获取到所有的值:\n{0}".format(data2)) #格式化输出


#  行数 （不包含表头，且一下均如此）
print(len(df.index.values))
# 行索引
print(df.index.values)
#  列数
print(len(df.columns.values))
#  列索引
print(df.columns.values)

data = df.loc[0].values
print('第0行数据: \n', data)
#  读取多行数据（这里是第1行和第2行）
data = df.loc[[1, 2]].values
print('第1行和第2行数据: \n', data)

#  读第1列数据
data = df.iloc[:, 0].values
print('第0列数据: \n', data)
#  读取多列数据（这里是第1列和第2列）
data = df.iloc[:, [1, 2]].values
print('第1列和第2列数据: \n', data)

#  读取指定单元格数据（这里是第1行第一列数据）
data = df.iloc[1, 2]
print('第1行第1列数据: \n', data)
#  读取多行多列数据（第1,2行1,2列的数据）
data = df.iloc[[1, 2], [1, 2]].values
print('第1,2行1,2列的数据: \n', data)

# 输入
writer = pd.ExcelWriter('D:/pachong/weibo/weibo.xlsx')
# 字典
urlList = [
    "https://tvax1.sinaimg.cn/crop.0.0.512.512.180/007wRchgly8g115fxehekj30e80e8t8y.jpg?KID=imgbed,tva&Expires=1593318475&ssig=EIBw5w8WVE",
    "https://tvax1.sinaimg.cn/crop.0.0.512.512.180/007wRchgly8g115fxehekj30e80e8t8y.jpg?KID=imgbed,tva&Expires=1593318475&ssig=EIBw5w8WVE",
    "https://tvax1.sinaimg.cn/crop.0.0.512.512.180/007wRchgly8g115fxehekj30e80e8t8y.jpg?KID=imgbed,tva&Expires=1593318475&ssig=EIBw5w8WVE",
    "https://tvax1.sinaimg.cn/crop.0.0.512.512.180/007wRchgly8g115fxehekj30e80e8t8y.jpg?KID=imgbed,tva&Expires=1593318475&ssig=EIBw5w8WVE",
    "https://tvax1.sinaimg.cn/crop.0.0.512.512.180/007wRchgly8g115fxehekj30e80e8t8y.jpg?KID=imgbed,tva&Expires=1593318475&ssig=EIBw5w8WVE"]
temp = {'name': ['Ohio', 'Sda', 'Job', 'Bob', 'Jen'],
        'age': ['12', '3', '21', '16', '26'],
        'url': urlList,
        'sex': ['boy', 'girl', 'boy', 'girl', 'boy'],
        'date': ['2020-1-2', '2020-1-3', '2020-1-4', '2020-1-6', '2020-1-7']}
df2 = pd.DataFrame(data=temp,
                   columns=['name', 'age',  'sex', 'date', 'url'],
                   index=['one', 'two', 'three', 'four', 'five'])
#  不写index会输出索引
df2.to_excel(writer, 'Sheet1', index=False)
writer.save()
