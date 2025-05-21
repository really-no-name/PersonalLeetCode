#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1205.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 每月交易 II。
"""
import pandas as pd


def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    # 先根据 transactions 计算
    df_transactions = transactions.copy()
    df_transactions['month'] = df_transactions['trans_date'].dt.strftime('%Y-%m')

    # 统计 approved
    df_approved = df_transactions[df_transactions['state'] == 'approved']
    df_approved = df_approved.groupby(['month', 'country']).agg({
        'state': 'count',
        'amount': 'sum'
    }).reset_index()
    df_approved = df_approved.rename(columns={'state': 'approved_count', 'amount': 'approved_amount'})

    # 合并
    df_merge = pd.merge(transactions, chargebacks, left_on='id', right_on='trans_id', how='right')
    df_merge['month'] = df_merge['trans_date_y'].dt.strftime('%Y-%m')

    # 统计 chargeback
    df_chargeback = df_merge.groupby(['month', 'country']).agg({
        'id': 'count',
        'amount': 'sum'
    }).reset_index()
    df_chargeback = df_chargeback.rename(columns={'amount': 'chargeback_amount', 'id': 'chargeback_count'})

    # 合并结果
    df_result = pd.merge(df_approved, df_chargeback, on=['month', 'country'], how='outer').fillna(0)

    return df_result


if __name__ == '__main__':
    data = [[101, 'US', 'approved', 1000, '2019-05-18'], [102, 'US', 'declined', 2000, '2019-05-19'],
            [103, 'US', 'approved', 3000, '2019-06-10'], [104, 'US', 'declined', 4000, '2019-06-13'],
            [105, 'US', 'approved', 5000, '2019-06-15']]
    transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype(
        {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})
    data = [[102, '2019-05-29'], [101, '2019-06-30'], [105, '2019-09-18']]
    chargebacks = pd.DataFrame(data, columns=['trans_id', 'trans_date']).astype(
        {'trans_id': 'Int64', 'trans_date': 'datetime64[ns]'})
    print(monthly_transactions(transactions, chargebacks))