#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1705.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 项目员工 I。
"""
import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(project, employee, on='employee_id', how='left')
    # 按项目分组计算平均工作年限，并四舍五入到2位小数
    result = merged_df.groupby('project_id')['experience_years'].mean().round(2).reset_index()  # 均值
    result = result.rename(columns={'experience_years': 'average_years'})
    return result[['project_id', 'average_years']]


if __name__ == '__main__':
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype(
        {'project_id': 'Int64', 'employee_id': 'Int64'})
    data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    print(project_employees_i(project, employee))