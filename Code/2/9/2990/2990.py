#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2990.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 贷款类型。
"""
import pandas as pd


def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    df_pivot = loans.pivot_table(
        index="user_id",
        columns="loan_type",
        aggfunc="size",  # 统计出现次数
        fill_value=0  # 未出现的组合填充 0
    )
    df_pivot.columns.name = None  # 移除列名标签
    df_filter = df_pivot[(df_pivot['Refinance'] > 0) & (df_pivot['Mortgage'] > 0)].reset_index()
    return df_filter[['user_id']]


if __name__ == '__main__':
    data = [[683, 101, 'Mortgage'], [218, 101, 'AutoLoan'], [802, 101, 'Inschool'], [593, 102, 'Mortgage'],
            [138, 102, 'Refinance'], [294, 102, 'Inschool'], [308, 103, 'Refinance'], [389, 104, 'Mortgage']]
    loans = pd.DataFrame(data, columns=['loan_id', 'user_id', 'loan_type']).astype(
        {'loan_id': 'Int64', 'user_id': 'Int64', 'loan_type': 'object'})
    print(loan_types(loans))