#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2230.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 查找可享受优惠的用户。
"""
import pandas as pd
from datetime import datetime


def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime,
                     min_amount: int) -> pd.DataFrame:
    # Convert time_stamp to datetime if not already
    purchases['time_stamp'] = pd.to_datetime(purchases['time_stamp'])

    # Convert start and end dates to datetime (at start of day)
    start_date = pd.to_datetime(start_date).normalize()
    end_date = pd.to_datetime(end_date).normalize()

    # Filter purchases within the date range and meeting the minAmount
    eligible_purchases = purchases[
        (purchases['time_stamp'] >= start_date) &
        (purchases['time_stamp'] <= end_date) &
        (purchases['amount'] >= min_amount)
        ]

    # Get unique user_ids who made eligible purchases
    eligible_users = eligible_purchases['user_id'].unique()

    # Create result DataFrame and sort by user_id
    result = pd.DataFrame({'user_id': eligible_users}).sort_values('user_id')

    return result