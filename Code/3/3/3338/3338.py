#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3338.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 第二高的薪水 II。
"""
import pandas as pd


def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    employees['rank'] = employees.groupby('dept')['salary'].rank(method='dense', ascending=False)
    result = employees[employees['rank'] == 2].sort_values(by=['emp_id'])
    return result[['emp_id', 'dept']]


if __name__ == '__main__':
    data = [[1, 70000, 'Sales'],
            [2, 80000, 'Sales'],
            [3, 80000, 'Sales'],
            [4, 90000, 'Sales'],
            [5, 55000, 'IT'],
            [6, 65000, 'IT'],
            [7, 65000, 'IT'],
            [8, 50000, 'Marketing'],
            [9, 55000, 'Marketing'],
            [10, 55000, 'HR']]
    employees = pd.DataFrame(data, columns=['emp_id', 'salary', 'dept']).astype(
        {'emp_id': int, 'salary': int, 'dept': str})
    print(find_second_highest_salary(employees))