#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1468.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 计算税后工资。
"""
import pandas as pd


def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    # 计算公司最高工资
    df_max_salary = salaries.groupby('company_id')['salary'].max().reset_index(name='max_salary')

    # 合并
    df_merge = salaries.merge(df_max_salary, on='company_id', how='left')

    # 计算
    def calc_tax(row):
        if row['max_salary'] < 1000:
            return row['salary']
        elif row['max_salary'] > 10000:
            return int(row['salary'] * 0.51 + 0.5)  # 不理解但尊重
        else:
            return int(row['salary'] * 0.76 + 0.5)

    df_merge['salary'] = df_merge.apply(calc_tax, axis=1)
    return df_merge[['company_id', 'employee_id', 'employee_name', 'salary']]


if __name__ == '__main__':
    data = [[1, 1, 'Tony', 2000], [1, 2, 'Pronub', 21300], [1, 3, 'Tyrrox', 10800], [2, 1, 'Pam', 300],
            [2, 7, 'Bassem', 450], [2, 9, 'Hermione', 700], [3, 7, 'Bocaben', 100], [3, 2, 'Ognjen', 2200],
            [3, 13, 'Nyancat', 3300], [3, 15, 'Morninngcat', 7777]]
    salaries = pd.DataFrame(data, columns=['company_id', 'employee_id', 'employee_name', 'salary']).astype(
        {'company_id': 'Int64', 'employee_id': 'Int64', 'employee_name': 'object', 'salary': 'Int64'})
    print(calculate_salaries(salaries))