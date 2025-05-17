#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2205.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 有资格享受折扣的用户数量。
"""
import pandas as pd
from datetime import datetime


def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime,
                      min_amount: int) -> pd.DataFrame:
    # Convert time_stamp to datetime if not already
    # purchases['time_stamp'] = pd.to_datetime(purchases['time_stamp'])

    # Convert start and end dates to datetime (at start of day)
    start_date = pd.to_datetime(start_date).normalize()
    end_date = pd.to_datetime(end_date).normalize()

    # Filter purchases within the date range and meeting the minAmount
    eligible_purchases = purchases[
        (purchases['time_stamp'] >= start_date) &
        (purchases['time_stamp'] <= end_date) &
        (purchases['amount'] >= min_amount)
        ]

    cnt = eligible_purchases['user_id'].nunique()

    df_result = pd.DataFrame({'user_cnt': [cnt]})

    return df_result


if __name__ == '__main__':
    data = [[1, '2022-04-20 09:03:00', 4416],
            [2, '2022-03-19 19:24:02', 678],
            [3, '2022-03-18 12:03:09', 4523],
            [3, '2022-03-30 09:43:42', 626]]
    purchases = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'amount']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'amount': 'Int64'})
    print(count_valid_users(purchases, datetime(2022, 3, 8),
                            datetime(2022, 3, 20), 1000))