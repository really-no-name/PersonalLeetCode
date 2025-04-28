#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0570.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0
描述: 至少有5名直接下属的经理。
"""
import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # 计算每个managerId出现的次数（即下属人数）
    manager_counts = employee['managerId'].value_counts().reset_index()
    manager_counts.columns = ['id', 'count']  # 重命名列

    result = manager_counts[manager_counts['count'] >= 5]
    result = result.merge(employee, on='id')

    return result[['name']]


if __name__ == '__main__':
    import pandas as pd

    data = [
        [101, 'John', 'A', None],
        [102, 'Dan', 'A', 101],
        [103, 'James', 'A', 101],
        [104, 'Amy', 'A', 101],
        [105, 'Anne', 'A', 101],
        [106, 'Ron', 'B', 101],
        [107, 'Tom', 'A', 102],
        [108, 'Tommy', 'A', 102],
        [109, 'Peter', 'C', 102],
        [110, 'Dong', 'A', 102]
    ]

    employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype(
        {'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'}
    )
    print(find_managers(employee))