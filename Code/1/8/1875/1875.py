#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1875.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 将工资相同的雇员分组。
"""
import pandas as pd


def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    # 根据工资分组，筛选 >= 2
    can_grp = employees.groupby('salary')['employee_id'].count().reset_index(name='cnt')
    can_grp = can_grp[can_grp['cnt'] >= 2]['salary']

    # 筛选可以被分组的雇员，使用 .loc 避免警告
    df_filter = employees.loc[employees['salary'].isin(can_grp)].copy()

    # 根据工资升序排名
    df_filter.loc[:, 'team_id'] = df_filter['salary'].rank(method='dense', ascending=True)

    # 排序结果
    df_sort = df_filter.sort_values(['team_id', 'employee_id'], ascending=[True, True])
    return df_sort


if __name__ == '__main__':
    data = [[2, 'Meir', 3000], [3, 'Michael', 3000], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7400]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'salary': 'Int64'})
    print(employees_of_same_salary(employees))