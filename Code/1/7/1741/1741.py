#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1741.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 查找每个员工花费的总时间。
"""
import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    grouped_df = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    grouped_df = grouped_df.rename(columns={'event_day': 'day'})
    return  grouped_df[['day', 'emp_id', 'total_time']]


if __name__ == '__main__':
    data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'],
            ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
    employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype(
        {'emp_id': 'Int64', 'event_day': 'datetime64[ns]', 'in_time': 'Int64', 'out_time': 'Int64'})
    print(total_time(employees))