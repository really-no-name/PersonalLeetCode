#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1873.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 计算特殊奖金。
"""
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if (row['employee_id'] % 2 == 1 and not row['name'].startswith('M')) else 0,
        axis=1
    )
    df_sort = employees.sort_values(by=['employee_id'], ascending=True)
    return df_sort[['employee_id', 'bonus']]


if __name__ == '__main__':
    data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
    print(calculate_special_bonus(employees))