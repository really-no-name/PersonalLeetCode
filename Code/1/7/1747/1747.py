#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1747.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 应该被禁止的 Leetflex 账户。
"""
import pandas as pd


def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    data = [[1, 1, '2021-02-01 09:00:00', '2021-02-01 09:30:00'], [1, 2, '2021-02-01 08:00:00', '2021-02-01 11:30:00'],
            [2, 6, '2021-02-01 20:30:00', '2021-02-01 22:00:00'], [2, 7, '2021-02-02 20:30:00', '2021-02-02 22:00:00'],
            [3, 9, '2021-02-01 16:00:00', '2021-02-01 16:59:59'], [3, 13, '2021-02-01 17:00:00', '2021-02-01 17:59:59'],
            [4, 10, '2021-02-01 16:00:00', '2021-02-01 17:00:00'],
            [4, 11, '2021-02-01 17:00:00', '2021-02-01 17:59:59']]
    log_info = pd.DataFrame(data, columns=['account_id', 'ip_address', 'login', 'logout']).astype(
        {'account_id': 'Int64', 'ip_address': 'Int64', 'login': 'datetime64[ns]', 'logout': 'datetime64[ns]'})