#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2687.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 自行车的最后使用时间。
"""
import pandas as pd


def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    df_sort = bikes.sort_values('end_time', ascending=False)
    def_group = df_sort.groupby('bike_number').head(1)
    result_df = def_group[['bike_number', 'end_time']]
    return result_df


if __name__ == '__main__':
    data = [[1, 'W00576', '2012-03-25 11:30:00', '2012-03-25 12:40:00'],
            [2, 'W00300', '2012-03-25 10:30:00', '2012-03-25 10:50:00'],
            [3, 'W00455', '2012-03-26 14:30:00', '2012-03-26 17:40:00'],
            [4, 'W00455', '2012-03-25 12:30:00', '2012-03-25 13:40:00'],
            [5, 'W00576', '2012-03-25 08:10:00', '2012-03-25 09:10:00'],
            [6, 'W00576', '2012-03-28 02:30:00', '2012-03-28 02:50:00']]
    bikes = pd.DataFrame(data, columns=['ride_id', 'bike_number', 'start_time', 'end_time']).astype(
        {'ride_id': 'Int64', 'bike_number': 'object', 'start_time': 'datetime64[ns]', 'end_time': 'datetime64[ns]'})
    print(last_used_time(bikes))