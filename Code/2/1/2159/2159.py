#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2159.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 分别排序两列。
"""
import pandas as pd


def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([
        data[['first_col']].sort_values('first_col', ascending=True).reset_index(drop=True),
        data[['second_col']].sort_values('second_col', ascending=False).reset_index(drop=True)
    ], axis=1)
    return df


if __name__ == '__main__':
    data = [[4, 2], [2, 3], [3, 1], [1, 4]]
    data = pd.DataFrame(data, columns=['first_col', 'second_col']).astype({'first_col': 'Int64', 'second_col': 'Int64'})
    print(order_two_columns(data))