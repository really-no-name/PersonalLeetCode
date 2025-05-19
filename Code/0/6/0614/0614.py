#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0614.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 二级关注者。
"""
import pandas as pd


def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    df_filter = follow[follow['followee'].isin(follow['follower'])]
    df_grp = df_filter.groupby('followee')['follower'].nunique().reset_index()
    df_grp = df_grp.rename(columns={'followee': 'follower', 'follower': 'num'})
    df_sort = df_grp.sort_values('follower', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [['Alice', 'Bob'], ['Bob', 'Cena'], ['Bob', 'Donald'], ['Donald', 'Edward']]
    follow = pd.DataFrame(data, columns=['followee', 'follower']).astype({'followee': 'object', 'follower': 'object'})
    print(second_degree_follower(follow))