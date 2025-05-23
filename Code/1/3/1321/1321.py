#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1321.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 餐馆营业额变化增长。
"""
import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.copy()

    # 按日期排序，按天group，放置一天多个人顾客
    df = df.sort_values(by=['visited_on'], ascending=True)
    df = df.groupby('visited_on')['amount'].sum().reset_index()
    df['amount'] = df['amount'].rolling(7).sum()

    # 筛选 有效范围
    df_filter = df[df['amount'].notna()]

    # 计算均值
    df_filter['average_amount'] = round(df_filter['amount'] / 7, 2)
    return df_filter


if __name__ == '__main__':
    data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120],
            [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140],
            [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110],
            [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
    customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype(
        {'customer_id': 'Int64', 'name': 'object', 'visited_on': 'datetime64[ns]', 'amount': 'Int64'})
    print(restaurant_growth(customer))