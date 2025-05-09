#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0601.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 体育馆的人流量。
"""
import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # 使用条件过滤
    filtered_stadium = stadium[stadium['people'] >= 100]
    filtered_stadium['rnk_diff'] = filtered_stadium['id'] - filtered_stadium['id'].rank(method='first')
    valid_rnk_diff = filtered_stadium.groupby('rnk_diff').filter(lambda group: len(group) >= 3)['rnk_diff'].unique()
    result = filtered_stadium[filtered_stadium['rnk_diff'].isin(valid_rnk_diff)][['id', 'visit_date', 'people']]
    return result


if __name__ == '__main__':
    data = [[1, '2017-01-01', 10],
            [2, '2017-01-02', 109],
            [3, '2017-01-03', 150],
            [4, '2017-01-04', 99],
            [5, '2017-01-05', 145],
            [6, '2017-01-06', 1455],
            [7, '2017-01-07', 199],
            [8, '2017-01-09', 188]]
    stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype(
        {'id': 'Int64', 'visit_date': 'datetime64[ns]', 'people': 'Int64'})
    print(human_traffic(stadium))