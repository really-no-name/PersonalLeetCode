#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0175.py
作者: Bolun Xu
创建日期: 2025/4/18
版本: 1.0
描述: 组合两个表。
"""
import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 左连接(保留df1中的所有key)
    frame_a = pd.merge(person, address, on='personId', how='left')
    result = frame_a[['firstName', 'lastName', 'city', 'state']]
    return result


if __name__ == '__main__':
    data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
    person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype(
        {'personId': 'Int64', 'firstName': 'object', 'lastName': 'object'})
    data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
    address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype(
        {'addressId': 'Int64', 'personId': 'Int64', 'city': 'object', 'state': 'object'})
    print(combine_two_tables(person, address))