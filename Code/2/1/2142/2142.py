#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2142.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 每辆车的乘客人数 I。
"""
import pandas as pd


def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    # 对 buses 按 到达时间排序
    df_buses = buses.sort_values(by='arrival_time', ascending=True)
    df_buses['last_bus'] = df_buses['arrival_time'].shift(1).fillna(0)

    # cross 连接
    df_merge = pd.merge(df_buses, passengers, how='cross')

    # 筛选可以上车的人
    condition = (df_merge['arrival_time_y'] <= df_merge['arrival_time_x']) & (df_merge['arrival_time_y'] > df_merge['last_bus'])
    df_filter = df_merge[condition]

    # 计数
    df_grp = df_filter.groupby('bus_id')['passenger_id'].nunique().reset_index(name='passengers_cnt')

    # 合并，防止公交车无乘客
    df_result = buses[['bus_id']].merge(df_grp, on='bus_id', how='left').fillna(0)

    # 排序
    df_sort = df_result.sort_values(by='bus_id', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, 2], [2, 4], [3, 7]]
    buses = pd.DataFrame(data, columns=['bus_id', 'arrival_time']).astype({'bus_id': 'Int64', 'arrival_time': 'Int64'})
    data = [[11, 1], [12, 5], [13, 6], [14, 7]]
    passengers = pd.DataFrame(data, columns=['passenger_id', 'arrival_time']).astype(
        {'passenger_id': 'Int64', 'arrival_time': 'Int64'})
    print(count_passengers_in_bus(buses, passengers))