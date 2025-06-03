#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2175.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 世界排名的变化。
"""
import pandas as pd


def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    # 计算分数变化
    df_points_change = points_change.groupby('team_id')['points_change'].sum().reset_index()

    # 合并
    df_merge = team_points.merge(df_points_change, on='team_id', how='left')

    # 计算新分数
    df_merge['points_new'] = df_merge['points'] + df_merge['points_change']

    # 排名
    # 先根据字典序 排序
    df_merge = df_merge.sort_values(by=['name'], ascending=True)
    df_merge['old_rnk'] = df_merge['points'].rank(method='first', ascending=False)
    df_merge['new_rnk'] = df_merge['points_new'].rank(method='first', ascending=False)

    # 计算diff
    df_merge['rank_diff'] = df_merge['old_rnk'] - df_merge['new_rnk']

    return df_merge[['team_id', 'name', 'rank_diff']]


if __name__ == '__main__':
    data = [[3, 'Algeria', 1431], [1, 'Senegal', 2132], [2, 'New Zealand', 1402], [4, 'Croatia', 1817]]
    team_points = pd.DataFrame(data, columns=['team_id', 'name', 'points']).astype(
        {'team_id': 'Int64', 'name': 'object', 'points': 'Int64'})
    data = [[3, 399], [2, 0], [4, 13], [1, -22]]
    points_change = pd.DataFrame(data, columns=['team_id', 'points_change']).astype(
        {'team_id': 'Int64', 'points_change': 'Int64'})
    print(global_ratings_change(team_points, points_change))