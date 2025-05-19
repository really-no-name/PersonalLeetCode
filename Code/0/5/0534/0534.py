#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0534.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 游戏玩法分析 III。
"""
import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df_sort = activity.sort_values(by=['player_id', 'event_date'])
    df_sort['games_played_so_far'] = df_sort.groupby('player_id')['games_played'].cumsum()  # 累加
    return df_sort[['player_id', 'event_date', 'games_played_so_far']]


if __name__ == '__main__':
    data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [1, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0],
            [3, 4, '2018-07-03', 5]]
    activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype(
        {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    print(gameplay_analysis(activity))