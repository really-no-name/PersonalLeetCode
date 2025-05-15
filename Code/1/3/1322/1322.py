#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1322.py
作者: Bolun Xu
创建日期: 2025/5/15
版本: 1.0
描述: 广告效果。
"""
import pandas as pd


def CTR(row):
    clicked = row.get('Clicked', 0)  # 如果 'Clicked' 不存在，默认为 0
    viewed = row.get('Viewed', 0)    # 如果 'Viewed' 不存在，默认为 0
    total = clicked + viewed
    if total == 0:
        return 0
    else:
        return round((clicked / total) * 100, 2)

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    # 分组计数
    df_grp = ads.groupby(['ad_id', 'action'])['user_id'].nunique().reset_index()

    # 数据重塑
    df_pivot = df_grp.pivot_table(index='ad_id', columns='action', values='user_id').fillna(0).reset_index()
    # pivot_table 操作后，ad_id 变成了 DataFrame 的索引(index)，而不是列(column)
    df_pivot.columns.name = None  # 移除列名标签

    df_pivot['ctr'] = df_pivot.apply(CTR, axis=1)

    # 重置索引，使ad_id成为列
    # df_pivot = df_pivot.reset_index()

    # sort
    df_sort = df_pivot[['ad_id', 'ctr']].sort_values(by=['ctr', 'ad_id'], ascending=[False, True])

    return df_sort


if __name__ == '__main__':
    data = [[1, 1, 'Clicked'], [2, 2, 'Clicked'], [3, 3, 'Viewed'], [5, 5, 'Ignored'], [1, 7, 'Ignored'],
            [2, 7, 'Viewed'], [3, 5, 'Clicked'], [1, 4, 'Viewed'], [2, 11, 'Viewed'], [1, 2, 'Clicked']]
    ads = pd.DataFrame(data, columns=['ad_id', 'user_id', 'action']).astype(
        {'ad_id': 'Int64', 'user_id': 'Int64', 'action': 'object'})
    print(ads_performance(ads))