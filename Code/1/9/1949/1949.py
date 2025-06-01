#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1949.py
作者: Bolun Xu
创建日期: 2025/5/31
版本: 1.0
描述: 坚定的友谊。
"""
import pandas as pd


def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    # 获取所有id
    # df_id = pd.DataFrame(friendship.stack().unique())
    # df_id.columns = ['id']
    # df_result = df_id.merge(df_id, how='cross')
    # df_result = df_result[df_result['id_x'] < df_result['id_y']]
    # df_result.columns = ['user1_id', 'user2_id']

    # 获取每个 id 的朋友
    friendship_1 = friendship.rename(columns={'user1_id': 'user1_id', 'user2_id': 'friend'})
    friendship_2 = friendship.rename(columns={'user1_id': 'friend', 'user2_id': 'user1_id'})
    df_friend = pd.concat([friendship_1, friendship_2])
    df_friend = df_friend.groupby('user1_id')['friend'].agg(set).reset_index()  # 改为agg(set)

    # 合并
    df_result = friendship.merge(df_friend, how='left', on='user1_id')
    df_result = df_result.merge(df_friend, how='left', left_on='user2_id', right_on='user1_id')
    df_result = df_result.drop(columns=['user1_id_y'], axis=1).rename(columns={'user1_id_x': 'user1_id'})

    # 筛选交集大于等于3
    # 方法1：使用apply
    df_result['common_friend'] = df_result.apply(
        lambda row: len(row['friend_x'] & row['friend_y']),
        axis=1
    )
    df_filter = df_result[df_result['common_friend'] >= 3]

    # 或者方法2：使用列表推导式（性能更好）
    # mask = [len(row['friend_x'] & row['friend_y']) >= 3
    #         for _, row in df_result.iterrows()]
    # df_filter = df_result[mask]

    return df_filter[['user1_id', 'user2_id', 'common_friend']]


if __name__ == '__main__':
    data = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [1, 5], [2, 5], [1, 7], [3, 7], [1, 6], [3, 6], [2, 6]]
    friendship = pd.DataFrame(data, columns=['user1_id', 'user2_id']).astype({'user1_id': 'Int64', 'user2_id': 'Int64'})
    print(strong_friendship(friendship))