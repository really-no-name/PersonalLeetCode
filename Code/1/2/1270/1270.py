#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1270.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 向公司 CEO 汇报工作的所有人。
"""
import pandas as pd


def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    # 第一次查询
    df_filter = employees[employees['manager_id'] == 1]
    df_result = df_filter.copy()

    # 第二次查询
    df_filter = employees[employees['manager_id'].isin(df_result['employee_id'])]
    df_result = pd.concat([df_filter, df_result])

    # 第三次查询
    df_filter = employees[employees['manager_id'].isin(df_filter['employee_id'])]
    df_result = pd.concat([df_filter, df_result])

    # 结果
    df_result = df_result[df_result['employee_id'] != 1][['employee_id']].drop_duplicates(keep='first')
    return df_result


if __name__ == '__main__':
    data = [[1, 'Boss', 1], [3, 'Alice', 3], [2, 'Bob', 1], [4, 'Daniel', 2], [7, 'Luis', 4], [8, 'John', 3],
            [9, 'Angela', 8], [77, 'Robert', 1]]
    employees = pd.DataFrame(data, columns=['employee_id', 'employee_name', 'manager_id']).astype(
        {'employee_id': 'Int64', 'employee_name': 'object', 'manager_id': 'Int64'})
    print(find_reporting_people(employees))