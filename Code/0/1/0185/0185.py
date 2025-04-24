#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0185.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0
描述: 部门工资前三高的所有员工。
"""
import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id': 'departmentId', 'name': 'Department'})
    employee = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    merged_df = employee.merge(department, how='left', on='departmentId')
    merged_df['rank'] = merged_df.groupby('departmentId')['Salary'].rank(method='dense', ascending=False)
    result = merged_df[merged_df['rank'] <= 3]

    return result[['Department', 'Employee', 'Salary']]


if __name__ == '__main__':
    data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1],
            [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(top_three_salaries(employee, department))