#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3204.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 按位用户权限分析。

"""
from functools import reduce

import pandas as pd


def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    common_perms = reduce(lambda x, y: x & y, user_permissions['permissions'])
    any_perms = reduce(lambda x, y: x | y, user_permissions['permissions'])
    return pd.DataFrame({'common_perms': [common_perms], 'any_perms': [any_perms]})


if __name__ == '__main__':
    data = [[1, 5], [2, 12], [3, 7], [4, 3]]
    user_permissions = pd.DataFrame(data, columns=['user_id', 'permissions']).astype(
        {'user_id': 'Int64', 'permissions': 'Int64'})
    print(analyze_permissions(user_permissions))