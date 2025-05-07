#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2066.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 账户余额。
"""
import pandas as pd


def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.sort_values(['account_id', 'day'], ascending=[True, True])
    # 计算每笔交易的金额变化
    transactions['change'] = transactions['type'].apply(lambda x: 1 if x == 'Deposit' else -1) * transactions['amount']

    # 计算每个账户的累计余额
    transactions['balance'] = transactions.groupby('account_id')['change'].cumsum()

    result_df = transactions[['account_id', 'day', 'balance']].copy()
    return result_df


if __name__ == '__main__':
    data = [[1, '2021-11-07', 'Deposit', 2000],
            [1, '2021-11-09', 'Withdraw', 1000],
            [1, '2021-11-11', 'Deposit', 3000],
            [2, '2021-12-07', 'Deposit', 7000],
            [2, '2021-12-12', 'Withdraw', 7000]]
    transactions = pd.DataFrame(data, columns=['account_id', 'day', 'type', 'amount']).astype(
        {'account_id': 'Int64', 'day': 'datetime64[ns]', 'type': 'object', 'amount': 'Int64'})
    print(account_balance(transactions))

    data = [[7, '2021-12-07', 'Deposit', 1024],
            [7, '2021-11-17', 'Deposit', 1392],
            [7, '2021-11-04', 'Withdraw', 560],
            [7, '2021-11-25', 'Withdraw', 131],
            [7, '2021-12-19', 'Withdraw', 281],
            [7, '2021-12-28', 'Deposit', 1802],
            [7, '2021-11-01', 'Deposit', 1664]]
    transactions = pd.DataFrame(data, columns=['account_id', 'day', 'type', 'amount']).astype(
        {'account_id': 'Int64', 'day': 'datetime64[ns]', 'type': 'object', 'amount': 'Int64'})
    print('Test 1\n', account_balance(transactions))