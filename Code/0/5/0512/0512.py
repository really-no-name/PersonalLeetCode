#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0512.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 游戏玩法分析 II。
"""
import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df_sort = activity.sort_values(by=['event_date'], ascending=True)
    df_fliter = df_sort.drop_duplicates(subset=['player_id'], keep='first')
    return df_fliter[['player_id', 'device_id']]


if __name__ == '__main__':
    data = [[1, 2, '2016-03-01', 5],
            [1, 2, '2016-05-02', 6],
            [2, 3, '2017-06-25', 1],
            [3, 1, '2016-03-02', 0],
            [3, 4, '2018-07-03', 5]]
    activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype(
        {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    print(game_analysis(activity))