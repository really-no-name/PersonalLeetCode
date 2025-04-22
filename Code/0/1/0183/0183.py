#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0183.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 从不订购的客户。
"""
import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])]  # 判断在不在，~ 取反
    result = result.rename(columns={'name': 'Customers'})
    return result[['Customers']]


if __name__ == '__main__':
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3], [2, 1]]
    orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
    print(find_customers(customers, orders))
