#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1212.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 查询球队积分。
"""
import pandas as pd


def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    df = matches.copy()

    # 计算 host 得分
    def host_score(row):
        if row['host_goals'] > row['guest_goals']:
            return 3
        elif row['host_goals'] == row['guest_goals']:
            return 1
        else:
            return 0

    df['host_score'] = df.apply(host_score, axis=1)
    df_grp1 = df.groupby(['host_team'])['host_score'].sum().reset_index()

    # 计算 guest 得分
    def guest_score(row):
        if row['guest_goals'] > row['host_goals']:
            return 3
        elif row['host_goals'] == row['guest_goals']:
            return 1
        else:
            return 0

    df['guest_score'] = df.apply(guest_score, axis=1)
    df_grp2 = df.groupby(['guest_team'])['guest_score'].sum().reset_index()

    # 合并
    df_merge = teams.merge(df_grp1, left_on='team_id', right_on='host_team', how='left') \
        .merge(df_grp2, left_on='team_id', right_on='guest_team', how='left').fillna(0)

    # 计算总得分
    df_merge['num_points'] = df_merge['guest_score'] + df_merge['host_score']

    df_result = df_merge[['team_id', 'team_name', 'num_points']].sort_values(by=['num_points', 'team_id'], ascending=[False, True])
    return df_result


if __name__ == '__main__':
    data = [[10, 'Leetcode FC'], [20, 'NewYork FC'], [30, 'Atlanta FC'], [40, 'Chicago FC'], [50, 'Toronto FC']]
    teams = pd.DataFrame(data, columns=['team_id', 'team_name']).astype({'team_id': 'Int64', 'team_name': 'object'})
    data = [[1, 10, 20, 3, 0], [2, 30, 10, 2, 2], [3, 10, 50, 5, 1], [4, 20, 30, 1, 0], [5, 50, 30, 1, 0]]
    matches = pd.DataFrame(data, columns=['match_id', 'host_team', 'guest_team', 'host_goals', 'guest_goals']).astype(
        {'match_id': 'Int64', 'host_team': 'Int64', 'guest_team': 'Int64', 'host_goals': 'Int64',
         'guest_goals': 'Int64'})
    print(team_scores(teams, matches))