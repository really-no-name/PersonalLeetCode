#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3436.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 查找合法邮箱。
"""
import pandas as pd


def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
    df_filt = users[users['email'].str.fullmatch(pattern)]
    df_sort = df_filt.sort_values(by=['user_id'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, 'alice@example.com'], [2, 'bob_at_example.com'], [3, 'charlie@example.net'], [4, 'david@domain.com'],
            [5, 'eve@invalid']]
    users = pd.DataFrame(data, columns=["user_id", "email"]).astype({"user_id": "int32", "email": "string"})
    print(find_valid_emails(users))