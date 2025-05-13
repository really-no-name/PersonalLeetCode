#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1076.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 项目员工II。
"""
import pandas as pd


def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df_cnt = project.groupby('project_id')['employee_id'].count().reset_index(name='count')
    df_filt = df_cnt[df_cnt['count'] == df_cnt['count'].max()]
    return df_filt[['project_id']]


if __name__ == '__main__':
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype(
        {'project_id': 'Int64', 'employee_id': 'Int64'})
    data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    print(project_employees_ii(project, employee))