#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1214.py
作者: Bolun Xu
创建日期: 2025/5/15
版本: 1.0
描述: 每个帖子的评论数。
"""
import pandas as pd


def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    df_grp = submissions.groupby('parent_id')['sub_id'].nunique().reset_index()
    df_grp = df_grp.rename(columns={'parent_id': 'post_id', 'sub_id': 'number_of_comments'})
    df_filt = submissions[submissions['parent_id'].isna()].drop_duplicates(subset=['sub_id'])
    df_filt = df_filt.rename(columns={'sub_id': 'post_id'})
    df_merge = df_filt.merge(df_grp, on='post_id', how='left').fillna(0)
    df_sort = df_merge[['post_id', 'number_of_comments']].sort_values('post_id', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, None], [2, None], [1, None], [12, None], [3, 1], [5, 2], [3, 1], [4, 1], [9, 1], [10, 2], [6, 7]]
    submissions = pd.DataFrame(data, columns=['sub_id', 'parent_id']).astype({'sub_id': 'Int64', 'parent_id': 'Int64'})
    print(count_comments(submissions))