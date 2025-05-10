#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2668.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 查询员工当前薪水。
"""
import pandas as pd


def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    df = salary.groupby(['emp_id', 'firstname', 'lastname', 'department_id'])['salary'].max().reset_index()
    return df[['emp_id', 'firstname', 'lastname', 'salary', 'department_id']]


if __name__ == '__main__':
    data = [[1, 'Todd', 'Wilson', 110000, 'D1006'],
            [1, 'Todd', 'Wilson', 106119, 'D1006'],
            [2, 'Justin', 'Simon', 128922, 'D1005'],
            [2, 'Justin', 'Simon', 130000, 'D1005'],
            [3, 'Kelly', 'Rosario', 42689, 'D1002'],
            [4, 'Patricia', 'Powell', 162825, 'D1004'],
            [4, 'Patricia', 'Powell', 170000, 'D1004'],
            [5, 'Sherry', 'Golden', 44101, 'D1002'],
            [6, 'Natasha', 'Swanson', 79632, 'D1005'],
            [6, 'Natasha', 'Swanson', 90000, 'D1005']]
    salary = pd.DataFrame(data, columns=['emp_id', 'firstname', 'lastname', 'salary', 'department_id']).astype(
        {'emp_id': 'Int64', 'firstname': 'object', 'lastname': 'object', 'salary': 'Int64', 'department_id': 'object'})
    print(find_latest_salaries(salary))
