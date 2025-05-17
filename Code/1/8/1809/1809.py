#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1809.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 没有广告的剧集。
"""
import pandas as pd


def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    # 合并 Playback 和 Ads 表，基于 customer_id
    df_merge = playback.merge(ads, how='left', on='customer_id')

    # 过滤出 timestamp 在 start_time 和 end_time 之间的行
    df_filter = df_merge[(df_merge['start_time'] <= df_merge['timestamp']) & (df_merge['end_time'] >= df_merge['timestamp'])]

    # 提取这些行的 session_id
    df_ads = df_filter['session_id'].unique()

    df_result = playback[~playback['session_id'].isin(df_ads)][['session_id']]
    return df_result


if __name__ == '__main__':
    # data = [[1, 1, 1, 5],
    #         [2, 1, 15, 23],
    #         [3, 2, 10, 12],
    #         [4, 2, 17, 28],
    #         [5, 2, 2, 8]]
    # playback = pd.DataFrame(data, columns=['session_id', 'customer_id', 'start_time', 'end_time']).astype(
    #     {'session_id': 'Int64', 'customer_id': 'Int64', 'start_time': 'Int64', 'end_time': 'Int64'})
    # data = [[1, 1, 5],
    #         [2, 2, 17],
    #         [3, 2, 20]]
    # ads = pd.DataFrame(data, columns=['ad_id', 'customer_id', 'timestamp']).astype(
    #     {'ad_id': 'Int64', 'customer_id': 'Int64', 'timestamp': 'Int64'})
    # print('Test 1\n', ad_free_sessions(playback, ads))

    data = [[7 , 5, 329, 355],
            [1 , 4, 100, 169],
            [6 , 5, 789, 894],
            [4 , 5, 553, 655],
            [13, 4, 399, 399],
            [8 , 5, 69 , 183],
            [14, 4, 583, 610]]
    playback = pd.DataFrame(data, columns=['session_id', 'customer_id', 'start_time', 'end_time']).astype(
        {'session_id': 'Int64', 'customer_id': 'Int64', 'start_time': 'Int64', 'end_time': 'Int64'})
    data = [[9 , 5, 863],
            [5 , 4, 123],
            [8 , 4, 399],
            [12, 5, 152],
            [14, 4, 102],
            [7 , 5, 348],
            [10, 5, 850],
            [11, 5, 799],
            [13, 5, 161],
            [3 , 5, 82 ],
            [4 , 5, 85 ],
            [2 , 4, 593]]
    ads = pd.DataFrame(data, columns=['ad_id', 'customer_id', 'timestamp']).astype(
        {'ad_id': 'Int64', 'customer_id': 'Int64', 'timestamp': 'Int64'})
    print('Test 2\n', ad_free_sessions(playback, ads))