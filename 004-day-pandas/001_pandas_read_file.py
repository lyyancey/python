import pandas as pd
import numpy as np


def read_csv_file():
    fpath = './datas/ratings.csv'
    ratings = pd.read_csv(fpath)
    headers = ratings.head() # 默认显示前5行
    print(headers)
    shape = ratings.shape
    print(shape)
    columns = ratings.columns
    print(columns)
    print(type(columns))
    dtype = ratings.dtypes
    print(dtype)

def pandas_series():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    # print(s)
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))
    # print(df)

    df2 = pd.DataFrame({
        'A': 1.0,
        'B': pd.Timestamp('20230101'),
        'C': pd.Series(1, index=list(range(4)), dtype="float32"),
        'D': np.array([3]*4, dtype="int32"),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': "foo"
    })
    print(df2)
    print(df2.dtypes)

def pandas_view_data():
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))

    # 查看开头和结尾的数据，默认为5行或者5列
    head = df.head()
    tail = df.tail(3)
    # print(head)
    # print(tail)

    # 索引是每一行的标签
    # print(df.index)
    # 列名是每一列的标签
    # print(df.columns)

    # 转换为numpy数组
    # print(df.to_numpy())

    # 快速统计数据
    # print(df.describe())

    # 转置数据
    # print(df.T)

    # 按轴排序，行是0，列是1
    # print(df.sort_index(axis=1, ascending=True))

    # 对某一列进行排序
    print(df.sort_values(by="A"))


# Getting
def getting_data():
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))
    
    # 选择一个列，产生一个Series，相当于df.A
    #print(df['A'])

    # 选择行，通过[]进行选择，切片
    # print(df[0:3])

    # 通过标签选择
    # print(df['20230101': '20230103'])

    # 通过标签进行选择
    # print(df.loc[dates[0]])

    # 通过标签选择多轴
    # print(df.loc[:, ['A', 'B']])
    # print(df.loc['20230101':'20230104', ['A','C']])
    # print(df.loc['20230104', ["A", "B"]])
    # print(df.loc[dates[0], 'A'])

    # 通过位置选择
    # print(df.iloc[3]) # 这样直接选择的是某一列
    # print(df.iloc[3:5, 0:2]) # 前面选择的是行，后面选择的是列
    # print(df.iloc[[1, 2, 3], [0, 2]])

    # 使用单个列的值去选择数据
    # print(df[df['A'] > 0])

    # 从满足布尔条件的DataFrame中选择值
    # print(df[df > 0])

    # 使用isin()方法进行过滤
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three', 'two', 'one']
    # print(df2)
    print(df2[df2['E'].isin(['two', 'four'])])


def setting_data():
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))

    # 设置新列会自动按索引对齐数据
    # s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=pd.date_range('20230101', periods=8))
    # df['F']=s1
    # print(df)

    # 通过标签设置新值
    # df.at[dates[0], "A"] = 0
    # print(df)

    # 通过位置设置值
    # df.iat[0, 1] = 0
    # print(df)

    # 使用NumPy数组设置一组新值
    # df.loc[:, 'D'] = np.array([5] * len(df))
    # print(df)

    # 通过where操作设置新值
    df2 = df.copy()
    df2[df2 > 0] = -df2
    print(df2)

def missing_data():
    # pandas中使用np.nan来代表缺失的数据
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns)+['E'])
    df1.loc[dates[0] : dates[1], ['E']] = 1
    # print(df1)

    # 删除含有缺失数据的行
    f = df1.dropna(how='any')
    # print(f)

    # 填充缺失数据
    f = df1.fillna(value=5)
    # print(f)

    # 获取值为nan的布尔掩码值
    f = pd.isna(df1)
    # print(f)

def operation_data():
    # 统计操作通常排除缺失的数据
    dates = pd.date_range('20230101', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list("ABCD"))
    # 统计均值，默认在0轴上进行统计
    print(df.mean())

    # 在另一个轴上进行统计
    print(df.mean(1))





if __name__ == '__main__':
    # read_csv_file()
    # pandas_series()
    # pandas_view_data()
    # getting_data()
    # setting_data()
    # missing_data()
    operation_data()