#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1264.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 页面推荐。
"""
import pandas as pd


def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    # 筛选 user1_id = 1 的朋友
    friends_user1 = friendship[friendship['user1_id'] == 1]['user2_id']
    friends_user2 = friendship[friendship['user2_id'] == 1]['user1_id']
    id1_friendship = pd.concat([friends_user1, friends_user2])

    # 筛选 likes 表中 id1 喜欢的页面
    df_id1_likes = likes[likes['user_id'] == 1]

    # 筛选 likes 表，即是朋友，又不与ID1 喜欢的重复
    condition = ((likes['user_id'].isin(id1_friendship)) &
                 (~likes['page_id'].isin(df_id1_likes['page_id']))
                 )
    df_likes_filter = likes[condition]

    # 去重 重命名
    df_result = df_likes_filter[['page_id']].drop_duplicates(keep='first')
    df_result = df_result.rename(columns={'page_id': 'recommended_page'})
    return df_result


if __name__ == '__main__':
    data = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [6, 1]]
    friendship = pd.DataFrame(data, columns=['user1_id', 'user2_id']).astype({'user1_id': 'Int64', 'user2_id': 'Int64'})
    data = [[1, 88], [2, 23], [3, 24], [4, 56], [5, 11], [6, 33], [2, 77], [3, 77], [6, 88]]
    likes = pd.DataFrame(data, columns=['user_id', 'page_id']).astype({'user_id': 'Int64', 'page_id': 'Int64'})
    print(page_recommendations(friendship, likes))