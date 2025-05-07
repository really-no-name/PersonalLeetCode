#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2339.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 联赛的所有比赛。
"""
import pandas as pd


def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    merged_df = teams.merge(teams, how="cross")
    merged_df = merged_df[merged_df['team_name_x'] != merged_df['team_name_y']]
    result_df = merged_df.rename(columns={"team_name_x": "home_team", "team_name_y": "away_team"})
    return result_df


if __name__ == "__main__":
    data = [['Leetcode FC'], ['Ahly SC'], ['Real Madrid']]
    teams = pd.DataFrame(data, columns=['team_name']).astype({'team_name': 'object'})
    print(find_all_matches(teams))