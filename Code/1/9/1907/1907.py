#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1907.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 按分类统计薪水。
"""
import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def category(row):
        if row['income'] > 50000:
            return 'High Salary'
        elif row['income'] < 20000:
            return 'Low Salary'
        else:
            return 'Average Salary'

    df_account = accounts.copy()
    df_account['category'] = df_account.apply(category, axis=1)
    df_grp = df_account.groupby('category')['account_id'].nunique().reset_index(name='accounts_count')

    df = pd.DataFrame([['Low Salary'], ['Average Salary'], ['High Salary']], columns=['category'])

    df_merge = pd.merge(df, df_grp, on='category', how='left').fillna(0)
    return df_merge


if __name__ == '__main__':
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
    accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id': 'Int64', 'income': 'Int64'})
    print(count_salary_categories(accounts))