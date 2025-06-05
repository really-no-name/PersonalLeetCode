#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2308.py
作者: Bolun Xu
创建日期: 2025/6/5
版本: 1.0
描述: 按性别排列表格。
"""
import pandas as pd


def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    df = genders.copy()
    # 分组排序
    df['rnk'] = df.groupby('gender')['user_id'].rank(ascending=True, method='first')
    df['gender_rnk'] = df['gender'].apply(lambda x: 1 if x == 'female' else (2 if x == 'other' else 3))

    # 排序
    df_sort = df.sort_values(by=['rnk', 'gender_rnk'], ascending=[True, True])

    return df_sort[['user_id', 'gender']]


if __name__ == '__main__':
    data = [[4, 'male'], [7, 'female'], [2, 'other'], [5, 'male'], [3, 'female'], [8, 'male'], [6, 'other'],
            [1, 'other'], [9, 'female']]
    genders = pd.DataFrame(data, columns=['user_id', 'gender']).astype({'user_id': 'Int64', 'gender': 'object'})
    print(arrange_table(genders))