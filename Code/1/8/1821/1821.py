#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1821.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 寻找今年具有正收入的客户。
"""
import pandas as pd


def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    screen = customers[(customers['year'] == 2021) & (customers['revenue'] > 0)]
    return screen[['customer_id']]


if __name__ == '__main__':
    data = [['1', '2018', '50'],
            ['1', '2021', '30'],
            ['1', '2020', '70'],
            ['2', '2021', '-50'],
            ['3', '2018', '10'],
            ['3', '2016', '50'],
            ['4', '2021', '20']]
    customers = pd.DataFrame(data, columns=['customer_id', 'year', 'revenue']).astype(
        {'customer_id': 'Int64', 'year': 'Int64', 'revenue': 'Int64'})
    print(find_customers(customers))