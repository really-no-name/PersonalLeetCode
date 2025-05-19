#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0180.py
作者: Bolun Xu
创建日期: 2025/5/18
版本: 1.0
描述: 连续出现的数字。
"""
import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df_filt = logs[(logs['num'] == logs.shift(1)['num']) &
                   (logs['num'] == logs.shift(-1)['num'])]
    df_drop = df_filt.drop_duplicates(subset=['num'], keep='first')
    return df_drop[['num']].rename(columns={'num': 'ConsecutiveNums'})


if __name__ == '__main__':
    data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id': 'Int64', 'num': 'Int64'})
    print(consecutive_numbers(logs))