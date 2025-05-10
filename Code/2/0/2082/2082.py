#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2082.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 富有客户的数量。
"""
import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df_flitered = store[store['amount'] > 500]
    cnt = df_flitered['customer_id'].nunique()
    df_result = pd.DataFrame({'rich_count': [cnt]})
    return df_result


if __name__ == '__main__':
    data = [[6, 1, 549],
            [8, 1, 834],
            [4, 2, 394],
            [11, 3, 657],
            [13, 3, 257]]
    store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype(
        {'bill_id': 'int64', 'customer_id': 'int64', 'amount': 'int64'})
    print(count_rich_customers(store))