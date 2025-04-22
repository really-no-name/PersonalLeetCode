#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1978.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 上级经理已离职的公司员工。
"""
import pandas as pd


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (
            (~employees['manager_id'].isin(employees['employee_id'])) &
            (employees['manager_id'].notna()) &
            (employees['salary'] < 30000)
    )
    screen = employees[condition]
    result = screen[['employee_id']].sort_values('employee_id')
    return result


if __name__ == '__main__':
    data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241],
            [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'manager_id': 'Int64', 'salary': 'Int64'})
    print(find_employees(employees))
