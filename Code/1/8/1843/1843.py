#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1843.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 可疑银行账户。
"""
import pandas as pd
from dateutil.relativedelta import relativedelta


def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    df['day'] = df['day'].dt.strftime('%Y-%m')  # 获取月份
    df = df[df['type'] == 'Creditor']  # 只保留 存款

    # 按 月份 和 ID 分组
    df_grp = df.groupby(['account_id', 'day'])['amount'].sum().reset_index()

    # 填入下一月份数据
    df_grp['next_month'] = df_grp.groupby('account_id')['day'].shift(-1)
    df_grp['next_amount'] = df_grp.groupby('account_id')['amount'].shift(-1)
    df_grp = df_grp[~df_grp['next_month'].isna()]

    # 判断是否一行内是连续两月
    def is_one_month_diff(row):
        d1 = pd.to_datetime(row['day'] + '-1')
        d2 = pd.to_datetime(row['next_month'] + '-1')
        delta = relativedelta(d2, d1)
        return (delta.years == 0 and delta.months == 1) or (delta.years == 1 and delta.months == -11)

    df_grp['is_one_month_diff'] = df_grp.apply(is_one_month_diff, axis=1)
    df_grp = df_grp[df_grp['is_one_month_diff'] == True]

    # 合并 最大收入
    df_merge = df_grp.merge(accounts, on='account_id', how='left')

    # 筛选 连续两个月 超过 最大收入
    df_filter = df_merge[(df_merge['amount'] > df_merge['max_income']) & (df_merge['next_amount'] > df_merge['max_income'])]

    # 去重
    df_drop = df_filter[['account_id']].drop_duplicates(keep='first')
    return df_drop


if __name__ == '__main__':
    data = [[3, 21000], [4, 10400]]
    accounts = pd.DataFrame(data, columns=['account_id', 'max_income']).astype(
        {'account_id': 'Int64', 'max_income': 'Int64'})
    data = [[2, 3, 'Creditor', 107100, '2021-06-02 11:38:14'], [4, 4, 'Creditor', 10400, '2021-06-20 12:39:18'],
            [11, 4, 'Debtor', 58800, '2021-07-23 12:41:55'], [1, 4, 'Creditor', 49300, '2021-05-03 16:11:04'],
            [15, 3, 'Debtor', 75500, '2021-05-23 14:40:20'], [10, 3, 'Creditor', 102100, '2021-06-15 10:37:16'],
            [14, 4, 'Creditor', 56300, '2021-07-21 12:12:25'], [19, 4, 'Debtor', 101100, '2021-05-09 15:21:49'],
            [8, 3, 'Creditor', 64900, '2021-07-26 15:09:56'], [7, 3, 'Creditor', 90900, '2021-06-14 11:23:07']]
    transactions = pd.DataFrame(data, columns=['transaction_id', 'account_id', 'type', 'amount', 'day']).astype(
        {'transaction_id': 'Int64', 'account_id': 'Int64', 'type': 'object', 'amount': 'Int64',
         'day': 'datetime64[ns]'})
    print(suspicious_bank_accounts(accounts, transactions))