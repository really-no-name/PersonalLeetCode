#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1303.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 求团队人数。
"""
import pandas as pd


def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    employee_cnt = employee.groupby('team_id').nunique().reset_index()
    employee_cnt = employee_cnt.rename(columns={'employee_id': 'team_size'})
    merged_df = employee.merge(employee_cnt, on='team_id')
    return merged_df[['employee_id', 'team_size']]


if __name__ == '__main__':
    data = [[1, 8], [2, 8], [3, 8], [4, 7], [5, 9], [6, 9]]
    employee = pd.DataFrame(data, columns=['employee_id', 'team_id']).astype(
        {'employee_id': 'Int64', 'team_id': 'Int64'})
    print(team_size(employee))