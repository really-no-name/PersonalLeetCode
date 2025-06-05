#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2228.py
作者: Bolun Xu
创建日期: 2025/6/5
版本: 1.0
描述: 7 天内两次购买的用户。
"""
import pandas as pd


def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    # 根据 user_id 和 purchase_date 排序
    df_sort = purchases.sort_values(by=['user_id', 'purchase_date'])

    # 获取当前id的下一笔订单日期，并筛选有两笔订单的id
    df_sort['next_date'] = df_sort.groupby('user_id')['purchase_date'].shift(-1)
    df_filter = df_sort[~df_sort['next_date'].isna()].copy()

    # 获取两笔订单的差
    df_filter['diff'] = (df_filter['next_date'] - df_filter['purchase_date']).dt.days

    # 筛选 间隔 7 天
    df_filter2 = df_filter[df_filter['diff'] <= 7]

    # 对结果去重
    df_result = df_filter2[['user_id']].drop_duplicates(keep='first').sort_values(by=['user_id'])
    return df_result


if __name__ == '__main__':
    # data = [[4, 2, '2022-03-13'], [1, 5, '2022-02-11'], [3, 7, '2022-06-19'], [6, 2, '2022-03-20'],
    #         [5, 7, '2022-06-19'], [2, 2, '2022-06-08']]
    # purchases = pd.DataFrame(data, columns=['purchase_id', 'user_id', 'purchase_date']).astype(
    #     {'purchase_id': 'Int64', 'user_id': 'Int64', 'purchase_date': 'datetime64[ns]'})
    # print('TEST 1\n', find_valid_users(purchases))

    data = [[7, 5, '2022-05-09'],
            [5, 9, '2022-04-04'],
            [2, 5, '2022-12-13'],
            [8, 1, '2022-10-30'],
            [9, 1, '2022-09-26'],
            [3, 9, '2022-09-06'],
            [1, 1, '2022-09-06'],
            [4, 1, '2022-03-12'],
            [6, 5, '2022-11-14']]
    purchases = pd.DataFrame(data, columns=['purchase_id', 'user_id', 'purchase_date']).astype(
        {'purchase_id': 'Int64', 'user_id': 'Int64', 'purchase_date': 'datetime64[ns]'})
    print('TEST 2\n', find_valid_users(purchases))