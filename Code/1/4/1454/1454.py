#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1454.py
作者: Bolun Xu
创建日期: 2025/5/27
版本: 1.0
描述: 活跃用户。
"""
import pandas as pd


def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    df_l = logins.copy()
    # 去重
    df_l = df_l.drop_duplicates(subset=['id','login_date'])
    # 对 logins 分组排序
    df_l['rank'] = df_l.groupby('id').rank(method='first', ascending=True)
    df_l['diff'] = df_l.apply(lambda x: x['login_date'] - pd.Timedelta(days=x['rank']), axis=1)

    df_grp = df_l.groupby('id')['diff'].value_counts().reset_index()
    df_filter = df_grp[df_grp['count'] >= 5].drop_duplicates(subset='id', keep='first')

    df_merge = df_filter[['id']].merge(accounts, on='id', how='left')
    df_sort = df_merge.sort_values(by=['id'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, 'Winston'], [7, 'Jonathan']]
    accounts = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[7, '2020-05-30'], [1, '2020-05-30'], [7, '2020-05-31'], [7, '2020-06-01'], [7, '2020-06-02'],
            [7, '2020-06-02'], [7, '2020-06-03'], [1, '2020-06-07'], [7, '2020-06-10']]
    logins = pd.DataFrame(data, columns=['id', 'login_date']).astype({'id': 'Int64', 'login_date': 'datetime64[ns]'})
    print(active_users(accounts, logins))