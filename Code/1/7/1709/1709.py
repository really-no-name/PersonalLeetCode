#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1709.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 访问日期之间最大的空档期。
"""
import pandas as pd


def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    # 排序
    df_sort = user_visits.sort_values(by=['user_id', 'visit_date'], ascending=[True, True])

    # 取 下次访问时间
    df_sort['next_date'] = df_sort.groupby('user_id')['visit_date'].shift(-1).fillna(pd.to_datetime('2021-1-1'))

    # 计算diff
    df_sort['diff'] = (df_sort['next_date'] - df_sort['visit_date']).dt.days

    # 取最大
    df_sort = df_sort.groupby('user_id')['diff'].max().reset_index(name='biggest_window')
    return df_sort


if __name__ == '__main__':
    data = [['1', '2020-11-28'], ['1', '2020-10-20'], ['1', '2020-12-3'], ['2', '2020-10-5'], ['2', '2020-12-9'],
            ['3', '2020-11-11']]
    user_visits = pd.DataFrame(data, columns=['user_id', 'visit_date']).astype(
        {'user_id': 'Int64', 'visit_date': 'datetime64[ns]'})
    print(biggest_window(user_visits))