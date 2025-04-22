#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1517.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 查找拥有有效邮箱的用户。
"""
import re

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'  # 正则
    # ^[a-zA-Z]开头需要 + ^
    # 之后包含[a-zA-Z0-9_.-]* 需要 + *
    # 以@leetcode\.com（注意点 . 需要转义 \.）结尾 + $
    return users[users['mail'].str.fullmatch(pattern)]


if __name__ == '__main__':
    data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'],
            [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'],
            [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'],
            [7, 'Shapiro', '.shapo@leetcode.com']]
    users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype(
        {'user_id': 'int64', 'name': 'object', 'mail': 'object'})
    print(valid_emails(users))