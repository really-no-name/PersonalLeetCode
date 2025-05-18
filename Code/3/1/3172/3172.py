#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3172.py
作者: Bolun Xu
创建日期: 2025/5/18
版本: 1.0
描述: 第二天验证。
"""
import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    emails['signup_date'] = emails['signup_date'].dt.date
    texts['action_date'] = texts['action_date'].dt.date

    # 合并两个DataFrame
    merged_df = pd.merge(emails, texts, on='email_id', how='inner')

    # 筛选出验证操作为'Verified'的记录
    verified_df = merged_df[merged_df['signup_action'] == 'Verified']

    # 计算注册日期和验证日期之间的天数差异
    verified_df['days_diff'] = (verified_df['action_date'] - verified_df['signup_date']).apply(lambda x: x.days)

    # 筛选出第二天验证的用户
    next_day_verified_df = verified_df[verified_df['days_diff'] == 1]

    # 按user_id升序排序
    next_day_verified_df = next_day_verified_df.sort_values(by='user_id')

    return next_day_verified_df[['user_id']]


if __name__ == '__main__':
    data = [[125, 7771, '2022-06-14 09:30:00'], [433, 1052, '2022-07-09 08:15:00'], [234, 7005, '2022-08-20 10:00:00']]
    emails = pd.DataFrame(data, columns=['email_id', 'user_id', 'signup_date']).astype({
        'email_id': 'Int64',  # Nullable integer type
        'user_id': 'Int64',  # Nullable integer type
        'signup_date': 'datetime64[ns]'  # DateTime type for signup date
    })
    data = [[1, 125, 'Verified', '2022-06-15 08:30:00'], [2, 433, 'Not Verified', '2022-07-10 10:45:00'],
            [4, 234, 'Verified', '2022-08-21 09:30:00']]
    texts = pd.DataFrame(data, columns=['text_id', 'email_id', 'signup_action', 'action_date']).astype({
        'text_id': 'Int64',  # Nullable integer type for text_id
        'email_id': 'Int64',  # Nullable integer type for email_id
        'signup_action': 'object',  # Using 'object' to store string values for ENUM
        'action_date': 'datetime64[ns]'  # DateTime type for action_date
    })
    print(find_second_day_signups(emails, texts))