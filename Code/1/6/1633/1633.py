#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1633.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 各赛事的用户注册率。
"""
import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # merged_df = register.merge(users, on='user_id', how='left')
    register = register.groupby('contest_id')['user_id'].nunique().reset_index(name='count')
    # total = users['user_name'].nunique()
    total = users.shape[0]
    register['percentage'] = ((register['count'] / total) * 100).round(2)
    result = register[['contest_id', 'percentage']]
    result = result.sort_values(
        by=['percentage', 'contest_id'],
        ascending=[False, True]
    )
    return result


if __name__ == '__main__':
    data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
    users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id': 'Int64', 'user_name': 'object'})
    data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2],
            [207, 2], [210, 7]]
    register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id': 'Int64', 'user_id': 'Int64'})
    print(users_percentage(users, register))