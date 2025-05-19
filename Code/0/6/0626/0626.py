#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0626.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 换座位。
"""
import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    """
    对于每个学生，如果ID是偶数，则新ID为原ID减1；如果ID是奇数且不是最后一个ID，则新ID为原ID加1；否则保持不变。
    """
    # 创建一个新的DataFrame来处理交换逻辑
    result = seat.copy()

    # 交换相邻的座位
    for i in range(0, len(seat) - 1, 2):
        result.loc[i, 'student'], result.loc[i + 1, 'student'] = seat.loc[i + 1, 'student'], seat.loc[i, 'student']

    # 按id升序排列
    result = result.sort_values('id')

    return result


if __name__ == '__main__':
    data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
    seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id': 'Int64', 'student': 'object'})
    print(exchange_seats(seat))