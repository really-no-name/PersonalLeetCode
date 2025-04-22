#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1731.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 每位经理的下属员工数量。
"""
import pandas as pd


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # 统计 聚合
    result = employees.groupby('reports_to').agg(
        reports_count=('reports_to', 'count'),
        average_age=('age', 'mean')
    ).reset_index().rename(columns={'reports_to': 'employee_id'})

    # 处理数据
    result['average_age'] = result['average_age'].apply(lambda x: int(x + 0.5))  # 四舍五入

    # 合并
    result = result.merge(employees[['employee_id', 'name']], on='employee_id', how='left')

    # 调整列顺序
    return result[['employee_id', 'name', 'reports_count', 'average_age']]

if __name__ == '__main__':
    data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'reports_to': 'Int64', 'age': 'Int64'})
    print(count_employees(employees))

    # data = [
    #     [1, 'Michael', None, 45],
    #     [2, 'Alice', 1, 38],
    #     [3, 'Bob', 1, 42],
    #     [4, 'Charlie', 2, 34],
    #     [5, 'David', 2, 40],
    #     [6, 'Eve', 3, 37],
    #     [7, 'Frank', None, 50],
    #     [8, 'Grace', None, 48]
    # ]
    #
    # employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype(
    #     {'employee_id': 'Int64', 'name': 'object', 'reports_to': 'Int64', 'age': 'Int64'})
    # print(count_employees(employees))
