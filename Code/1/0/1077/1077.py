#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1077.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 项目员工 III。
"""
import pandas as pd


def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    """
    报告在每一个项目中 经验最丰富 的雇员是谁。如果出现经验年数相同的情况，请报告所有具有最大经验年数的员工。
    """
    df_merge = project.merge(employee, on='employee_id', how='left')
    df_merge['rank'] = df_merge.groupby('project_id')['experience_years'].rank(method='dense', ascending=False)
    df_filter = df_merge[df_merge['rank'] == 1]
    return df_filter[['project_id', 'employee_id']]


if __name__ == '__main__':
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype(
        {'project_id': 'Int64', 'employee_id': 'Int64'})
    data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 3], [4, 'Doe', 2]]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    print(project_employees(project, employee))
