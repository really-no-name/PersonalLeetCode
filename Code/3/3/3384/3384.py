#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3384.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 球队传球成功的优势得分。
"""
import pandas as pd


def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(passes, teams, left_on='pass_from', right_on='player_id')
    merged_df = merged_df.rename(columns={'team_name': 'pass_from_team'})
    del merged_df['player_id']
    merged_df = pd.merge(merged_df, teams, left_on='pass_to', right_on='player_id')
    merged_df = merged_df.rename(columns={'team_name': 'pass_to_team'})
    del merged_df['player_id']

    merged_df['half_number'] = (
        merged_df['time_stamp'].str.split(':')
        .apply(lambda x: int(x[0]) * 60 + int(x[1]))
        .gt(45 * 60)  # 45分钟转换为秒
        .astype(int) + 1
    )
    merged_df['dominance'] = merged_df.apply(lambda row: 1 if row['pass_from_team'] == row['pass_to_team'] else -1, axis=1)
    merged_df = merged_df.groupby(['pass_from_team', 'half_number'])['dominance'].sum().reset_index()
    result_df = merged_df.sort_values(by=['pass_from_team', 'half_number'], ascending=[True, True])
    result_df = result_df.rename(columns={'pass_from_team': 'team_name'})
    return result_df


if __name__ == '__main__':
    data = [[1, 'Arsenal'],
            [2, 'Arsenal'],
            [3, 'Arsenal'],
            [4, 'Chelsea'],
            [5, 'Chelsea'],
            [6, 'Chelsea']]
    teams = pd.DataFrame(data, columns=["player_id", "team_name"]).astype({"player_id": "int", "team_name": "string"})

    data = [[1, '00:15', 2],
            [2, '00:45', 3],
            [3, '01:15', 1],
            [4, '00:30', 1],
            [2, '46:00', 3],
            [3, '46:15', 4],
            [1, '46:45', 2],
            [5, '46:30', 6]]
    passes = pd.DataFrame(data, columns=["pass_from", "time_stamp", "pass_to"]).astype(
        {"pass_from": "int", "time_stamp": "string", "pass_to": "int"})
    print('TEST 1\n', calculate_team_dominance(teams, passes))

    data = [[1, 'Arsenal'],
            [2, 'Arsenal'],
            [3, 'Arsenal'],
            [4, 'Chelsea'],
            [5, 'Chelsea'],
            [6, 'Chelsea']]
    teams = pd.DataFrame(data, columns=["player_id", "team_name"]).astype({"player_id": "int", "team_name": "string"})

    data = [[2, '16:32',  4],
            [3, '18:27',  6],
            [5, '38:29',  1],
            [2, '43:27',  6],
            [5, '45:43',  3],
            [6, '54:23',  5],
            [6, '79:48',  1],
            [2, '85:19',  5]]
    passes = pd.DataFrame(data, columns=["pass_from", "time_stamp", "pass_to"]).astype(
        {"pass_from": "int", "time_stamp": "string", "pass_to": "int"})
    print('TEST 11\n', calculate_team_dominance(teams, passes))