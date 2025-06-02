#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1951.py
作者: Bolun Xu
创建日期: 2025/6/2
版本: 1.0
描述: 查询具有最多共同关注者的所有两两结对组。
"""
import pandas as pd


def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    # 获取每个ID的follower
    df_follower = relations.groupby('user_id')['follower_id'].agg(set).reset_index()

    # cross 合并
    df_merge = pd.merge(df_follower, df_follower, how='cross')
    df_merge = df_merge[df_merge['user_id_y'] > df_merge['user_id_x']]

    # 筛选交集大于等于3
    # 方法1：使用apply
    df_merge['common_follower'] = df_merge.apply(
        lambda row: len(row['follower_id_x'] & row['follower_id_y']),
        axis=1
    )
    df_filter = df_merge[df_merge['common_follower'] == df_merge['common_follower'].max()]

    df_result = df_filter[['user_id_x', 'user_id_y']].rename(columns={'user_id_x': 'user1_id', 'user_id_y': 'user2_id'})
    return df_result


if __name__ == '__main__':
    data = [[1, 3], [2, 3], [7, 3], [1, 4], [2, 4], [7, 4], [1, 5], [2, 6], [7, 5]]
    relations = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype(
        {'user_id': 'Int64', 'follower_id': 'Int64'})
    print(find_pairs(relations))