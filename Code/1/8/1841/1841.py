#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1841.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 联赛信息统计。
"""
import pandas as pd


def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    # STEP 1: 比赛次数
    df_1 = matches.drop(labels=['home_team_goals', 'away_team_goals'], axis=1) \
        .stack().value_counts() \
        .reset_index()
    df_1.columns = ['team_id', 'matches_played']
    df_result = teams.merge(df_1, on='team_id')

    # STEP 2: 计算 球队获得的总分数 总进球数 对手球队的所有进球数
    df = matches.copy()
    # STEP 2.1: 计算 分数
    def home_score(row):
        if row['home_team_goals'] == row['away_team_goals']:
            return 1
        elif row['home_team_goals'] > row['away_team_goals']:
            return 3
        else:
            return 0

    def away_score(row):
        if row['home_team_goals'] == row['away_team_goals']:
            return 1
        elif row['home_team_goals'] < row['away_team_goals']:
            return 3
        else:
            return 0

    df['home_score'] = df.apply(home_score, axis=1)
    df['away_score'] = df.apply(away_score, axis=1)

    #  STEP 2.2: 合并
    df_home = df[['home_team_id', 'home_score', 'home_team_goals', 'away_team_goals']] \
        .rename(columns={
        'home_team_id': 'team_id',
        'home_score': 'points',
        'home_team_goals': 'goal_for',
        'away_team_goals': 'goal_against'})
    df_away = df[['away_team_id', 'away_score', 'away_team_goals', 'home_team_goals']] \
        .rename(columns={
        'away_team_id': 'team_id',
        'away_score': 'points',
        'away_team_goals': 'goal_for',
        'home_team_goals': 'goal_against'})
    df_concat = pd.concat([df_home, df_away])

    #  STEP 2.3: 求和
    df_2 = df_concat.groupby('team_id') \
        .agg({'points': 'sum',
              'goal_for': 'sum',
              'goal_against': 'sum'})

    # STEP 2.4 计算diff
    df_2['goal_diff'] = df_2['goal_for'] - df_2['goal_against']

    # STEP 3 合并 排序
    df_result = df_result.merge(df_2, on='team_id', how='left').fillna(0).drop(labels=['team_id'], axis=1)
    df_sort = df_result.sort_values(by=['points', 'goal_diff', 'team_name'], ascending=[False, False, True])
    return df_sort


if __name__ == '__main__':
    data = [[1, 'Ajax'], [4, 'Dortmund'], [6, 'Arsenal']]
    teams = pd.DataFrame(data, columns=['team_id', 'team_name']).astype({'team_id': 'Int64', 'team_name': 'object'})
    data = [[1, 4, 0, 1], [1, 6, 3, 3], [4, 1, 5, 2], [6, 1, 0, 0]]
    matches = pd.DataFrame(data, columns=['home_team_id', 'away_team_id', 'home_team_goals', 'away_team_goals']).astype(
        {'home_team_id': 'Int64', 'away_team_id': 'Int64', 'home_team_goals': 'Int64', 'away_team_goals': 'Int64'})
    print(league_statistics(teams, matches))