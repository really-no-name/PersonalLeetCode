#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1729.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 求关注者的数量。
"""
import pandas as pd


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df_cnt = followers.groupby('user_id')['follower_id'].nunique().reset_index()
    df_cnt = df_cnt.rename(columns={'follower_id': 'followers_count'})
    df_sort = df_cnt.sort_values('user_id', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']]
    followers = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype(
        {'user_id': 'Int64', 'follower_id': 'Int64'})
    print(count_followers(followers))