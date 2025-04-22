#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0511.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 游戏玩法分析 I。
"""
import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by=['event_date'])
    screen = activity.drop_duplicates(subset=['player_id'])
    screen = screen.sort_values(by=['player_id'])
    result = screen.rename(columns={'event_date': 'first_login'})
    return result[['player_id', 'first_login']]


if __name__ == '__main__':
    data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0],
            [3, 4, '2018-07-03', 5]]
    activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype(
        {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    print(game_analysis(activity))