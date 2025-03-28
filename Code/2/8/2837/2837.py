#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2837.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0
描述: 总旅行距离。
时间复杂度：
空间复杂度：
"""
import pandas as pd


def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # Merge users with rides (left join to keep all users)
    merged = pd.merge(users, rides, on='user_id', how='left')
    print(merged)

    # Group by user_id and name, sum the distance (NaN values will be treated as 0)
    result = merged.groupby(['user_id', 'name'])['distance'].sum().reset_index()
    print(result)

    # Fill NA values with 0 (for users with no rides)
    result['distance'] = result['distance'].fillna(0)
    print(result)

    # Rename the distance column
    result = result.rename(columns={'distance': 'traveled distance'})
    print(result)

    # Sort by user_id in ascending order
    result = result.sort_values('user_id')

    return result


if __name__ == '__main__':
    users = {
        'user_id': [17, 14, 4, 2, 10],
        'name': ['Addison', 'Ethan', 'Michael', 'Avery', 'Eleanor']
    }

    rides = {
        'ride_id': [72, 42, 45, 32, 15, 56],
        'user_id': [17, 14, 4, 2, 4, 2],
        'distance': [160, 161, 59, 197, 357, 196]
    }
    print(get_total_distance(pd.DataFrame(users), pd.DataFrame(rides)))