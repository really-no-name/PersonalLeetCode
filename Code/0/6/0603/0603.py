#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0603.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 连续空余座位。
"""
import pandas as pd


def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema.sort_values(by='seat_id')
    # 筛出当前行和上一行或者和下一行都是1的，就是结果
    df_filt = cinema[((cinema['free'] == 1) & (cinema.shift(1)['free'] == 1)) | (
                (cinema['free'] == 1) & (cinema.shift(-1)['free'] == 1))]
    return df_filt[['seat_id']]


if __name__ == '__main__':
    data = [[1, 1], [2, 0], [3, 1], [4, 1], [5, 1]]
    cinema = pd.DataFrame(data, columns=['seat_id', 'free']).astype({'seat_id': 'Int64', 'free': 'int'})
    print(consecutive_available_seats(cinema))