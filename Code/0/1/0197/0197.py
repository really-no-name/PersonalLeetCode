#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0197.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 上升的温度。
"""
import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')

    weather['pre_date'] = weather['recordDate'].shift(1)
    weather['pre_temp'] = weather['temperature'].shift(1)
    print(weather)
    mask = (
        (weather['temperature'] > weather['pre_temp']) &
        (weather['recordDate'] - weather['pre_date'] == pd.Timedelta(days=1))
    )

    result = pd.DataFrame(weather.loc[mask, 'id'])
    return result


if __name__ == '__main__':
    data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
    weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype(
        {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'})
    print(rising_temperature(weather))

    data = [[1, '2000-12-16', 3], [2, '2000-12-15', -1]]
    weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype(
        {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'})
    print(rising_temperature(weather))