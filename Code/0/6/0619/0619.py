#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0619.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 只出现一次的最大数字。
"""
import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # 计算每个数字的出现次数
    counts = my_numbers['num'].value_counts()

    # 找出只出现一次的数字
    single_numbers = counts[counts == 1].index

    # 如果没有单一数字，返回None
    if len(single_numbers) == 0:
        return pd.DataFrame({'num': [None]})

    # 找出最大的单一数字
    max_num = max(single_numbers)

    return pd.DataFrame({'num': [max_num]})


if __name__ == '__main__':
    data = [[8], [8], [3], [3], [1], [4], [5], [6]]
    my_numbers = pd.DataFrame(data, columns=['num']).astype({'num': 'Int64'})
    print(biggest_single_number(my_numbers))