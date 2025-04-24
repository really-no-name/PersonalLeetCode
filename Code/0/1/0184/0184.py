#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 01843.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0
描述: 部门工资最高的员工。
"""
import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id': 'departmentId', 'name': 'Department'})
    employee = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    merged_df = employee.merge(department, how='left', on='departmentId')
    merged_df['rank'] = merged_df.groupby('departmentId')['Salary'].rank(method='dense', ascending=False)
    result = merged_df[merged_df['rank'] == 1]

    return result[['Department', 'Employee', 'Salary']]


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2],
            [5, 'Max', 90000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(department_highest_salary(employee, department))