#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0627.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 变更性别。
"""
import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].apply(lambda x: 'f' if x == 'm' else 'm')
    return salary


if __name__ == '__main__':
    data = [[1, 'A', 'm', 2500],
            [2, 'B', 'f', 1500],
            [3, 'C', 'm', 5500],
            [4, 'D', 'f', 500]]
    salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype(
        {'id': 'Int64', 'name': 'object', 'sex': 'object', 'salary': 'Int64'})
    print(swap_salary(salary))