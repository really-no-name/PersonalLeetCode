#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1581.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 进店却未进行过交易的顾客。
"""
import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    total = pd.merge(visits, transactions, on='visit_id', how='left')  # 合并
    print(total)
    screen = total[total['transaction_id'].isna()]  # 筛选
    print(screen)

    counts = screen['customer_id'].value_counts().reset_index()  # 数出现次数
    counts.columns = ['customer_id', 'count_no_trans']
    result = counts.sort_values(by='count_no_trans', ascending=False)  # 排序

    print(result)
    return result


if __name__ == "__main__":
    data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
    visits = pd.DataFrame(data, columns=['visit_id', 'customer_id']).astype(
        {'visit_id': 'Int64', 'customer_id': 'Int64'})
    data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
    transactions = pd.DataFrame(data, columns=['transaction_id', 'visit_id', 'amount']).astype(
        {'transaction_id': 'Int64', 'visit_id': 'Int64', 'amount': 'Int64'})
    print(find_customers(visits, transactions))