#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1149.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 文章浏览 II。
"""
import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df_grp = views.groupby(['viewer_id', 'view_date'])['article_id'].nunique().reset_index()
    df_filter = df_grp[df_grp['article_id'] >= 2][['viewer_id']].rename(columns={'viewer_id': 'id'})
    df_drop = df_filter.drop_duplicates(subset=['id'], keep='first')  # 同一 ID 多天均符合要求，去重
    df_sort = df_drop.sort_values(by=['id'])
    return df_sort


if __name__ == '__main__':
    data = [[1, 3, 5, '2019-08-01'], [3, 4, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'],
            [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
    views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
        {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
    print(article_views(views))