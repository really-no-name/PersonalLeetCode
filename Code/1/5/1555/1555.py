#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1555.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 银行账户概要。
"""
import pandas as pd


def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    data = [[1, 'Moustafa', 100], [2, 'Jonathan', 200], [3, 'Winston', 10000], [4, 'Luis', 800]]
    users = pd.DataFrame(data, columns=['user_id', 'user_name', 'credit']).astype(
        {'user_id': 'Int64', 'user_name': 'object', 'credit': 'Int64'})
    data = [[1, 1, 3, 400, '2020-08-01'], [2, 3, 2, 500, '2020-08-02'], [3, 2, 1, 200, '2020-08-03']]
    transactions = pd.DataFrame(data, columns=['trans_id', 'paid_by', 'paid_to', 'amount', 'transacted_on']).astype(
        {'trans_id': 'Int64', 'paid_by': 'Int64', 'paid_to': 'Int64', 'amount': 'Int64',
         'transacted_on': 'datetime64[ns]'})