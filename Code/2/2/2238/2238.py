#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2238.py
作者: Bolun Xu
创建日期: 2025/6/5
版本: 1.0
描述: 司机成为乘客的次数。
"""
import pandas as pd


def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    # 获取 driver_id
    df_driver = rides[['driver_id']].drop_duplicates(keep='first')

    # 获取乘客id 和 次数
    passenger = rides.drop(['ride_id', 'driver_id'], axis=1).stack().value_counts()
    df_passenger = passenger.reset_index()
    df_passenger.columns = ['passenger_id', 'cnt']

    # 合并
    df_merge = df_driver.merge(df_passenger, left_on='driver_id', right_on='passenger_id', how='left').fillna(0)

    return df_merge[['driver_id', 'cnt']]


if __name__ == '__main__':
    data = [[1, 7, 1], [2, 7, 2], [3, 11, 1], [4, 11, 7], [5, 11, 7], [6, 11, 3]]
    rides = pd.DataFrame(data, columns=['ride_id', 'driver_id', 'passenger_id']).astype(
        {'ride_id': 'Int64', 'driver_id': 'Int64', 'passenger_id': 'Int64'})
    print(driver_passenger(rides))