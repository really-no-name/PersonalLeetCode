#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0177.py
作者: Bolun Xu
创建日期: 2025/5/18
版本: 1.0
描述: 第N高的薪水。
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df_drop = employee.drop_duplicates(subset=['salary'], keep='first').reset_index(drop=True)
    if df_drop.shape[0] < N or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        df_drop['rank'] = df_drop['salary'].rank(ascending=False)
        salary = df_drop[df_drop['rank'] == N]['salary'].unique()
        return pd.DataFrame({f'getNthHighestSalary({N})': salary})


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, 2))

    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, 2))

    data = [[1, 100], [2, 100]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, 1))

    data = [[1, 100], [2, 100]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, 2))

    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, -1))