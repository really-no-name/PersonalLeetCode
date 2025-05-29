#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1613.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 找到遗失的ID。
"""
import pandas as pd


def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    # 获取最大id 不一定是最后一行
    # max_id = customers.iloc[-1]['customer_id']
    # max_id = customers.iat[-1, customers.get_loc('customer_id')]
    max_id = customers['customer_id'].max()

    # 判断是否存在
    ans = []
    for i in range(1, max_id + 1):
        if i not in customers['customer_id'].values:
            ans.append(i)

    # 生成结果
    df_result = pd.DataFrame({'ids': ans})
    return df_result


if __name__ == '__main__':
    data = [[1, 'Alice'], [4, 'Bob'], [5, 'Charlie']]
    customers = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype(
        {'customer_id': 'Int64', 'customer_name': 'object'})
    print(find_missing_ids(customers))