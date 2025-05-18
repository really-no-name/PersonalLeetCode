#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2853.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 最高薪水差异。
"""
import pandas as pd


def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    df_marketing = salaries[salaries['department'] == 'Marketing']
    marketing_max = df_marketing['salary'].max()  # 降序排名

    df_engineering = salaries[salaries['department'] == 'Engineering']
    engineering_max = df_engineering['salary'].max()

    df_result = pd.DataFrame({'salary_difference': [abs(marketing_max - engineering_max)]})
    return df_result


if __name__ == '__main__':
    data = [['Kathy', 'Engineering', 50000], ['Roy', 'Marketing', 30000], ['Charles', 'Engineering', 45000],
            ['Jack', 'Engineering', 85000], ['Benjamin', 'Marketing', 34000], ['Anthony', 'Marketing', 42000],
            ['Edward', 'Engineering', 102000], ['Terry', 'Engineering', 44000], ['Evelyn', 'Marketing', 53000],
            ['Arthur', 'Engineering', 32000]]
    salaries = pd.DataFrame(data, columns=['emp_name', 'department', 'salary']).astype(
        {'emp_name': 'object', 'department': 'object', 'salary': 'Int64'})
    print(salaries_difference(salaries))