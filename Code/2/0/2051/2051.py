#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2051.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 商店中每个成员的级别。
"""
import pandas as pd


def find_categories(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    # 合并 visits 和 purchases
    df_shopping = visits.merge(purchases, on='visit_id', how='left')

    # 计算 访问次数 和 购买总数
    df = df_shopping.groupby('member_id').agg({'visit_id': 'count', 'charged_amount': 'count'}).reset_index()

    # 计算 转化率
    df['conversion'] = 100 * df['charged_amount'] / df['visit_id']

    # 合并
    df_merge = members.merge(df, on='member_id', how='left').fillna(0)

    # 分类
    def conversion2type(row):
        if row['visit_id'] == 0:
            return 'Bronze'
        else:
            if row['conversion'] < 50:
                return 'Silver'
            elif row['conversion'] >= 80:
                return 'Diamond'
            else:
                return 'Gold'
    df_merge['category'] = df_merge.apply(conversion2type, axis=1)
    return df_merge[['member_id', 'name', 'category']]



if __name__ == '__main__':
    data = [[9, 'Alice'], [11, 'Bob'], [3, 'Winston'], [8, 'Hercy'], [1, 'Narihan']]
    members = pd.DataFrame(data, columns=['member_id', 'name']).astype({'member_id': 'Int64', 'name': 'object'})
    data = [[22, 11, '2021-10-28'], [16, 11, '2021-01-12'], [18, 9, '2021-12-10'], [19, 3, '2021-10-19'],
            [12, 11, '2021-03-01'], [17, 8, '2021-05-07'], [21, 9, '2021-05-12']]
    visits = pd.DataFrame(data, columns=['visit_id', 'member_id', 'visit_date']).astype(
        {'visit_id': 'Int64', 'member_id': 'Int64', 'visit_date': 'datetime64[ns]'})
    data = [[12, 2000], [18, 9000], [17, 7000]]
    purchases = pd.DataFrame(data, columns=['visit_id', 'charged_amount']).astype(
        {'visit_id': 'Int64', 'charged_amount': 'Int64'})
    print(find_categories(members, visits, purchases))