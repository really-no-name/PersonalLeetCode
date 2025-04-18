#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0181.py
作者: Bolun Xu
创建日期: 2025/4/18
版本: 1.0
描述: 超过经理收入的员工。
"""
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee['managerSalary'] = employee['managerId'].map(employee.set_index('id')['salary'])  # 自查
    result = employee[(employee['salary'] > employee['managerSalary']) & (employee['managerId'].notna())]
    print(result)
    return result[['name']].rename(columns={'name': 'Employee'})  # 更改列名


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})
    print(find_employees(employee))