#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3246.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 英超积分榜排名。
"""
import pandas as pd


def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    return 1


if __name__ == '__main__':
    data = [[1, 'Manchester City', 10, 6, 2, 2], [2, 'Liverpool', 10, 6, 2, 2], [3, 'Chelsea', 10, 5, 3, 2],
            [4, 'Arsenal', 10, 4, 4, 2], [5, 'Tottenham', 10, 3, 5, 2]]
    team_stats = pd.DataFrame(data,
                              columns=["team_id", "team_name", "matches_played", "wins", "draws", "losses"]).astype(
        {"team_id": "int", "team_name": "string", "matches_played": "int", "wins": "int", "draws": "int",
         "losses": "int"})
    print(calculate_team_standings(team_stats))