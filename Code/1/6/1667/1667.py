#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1667.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 修复表中的名字。
"""
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')


if __name__ == '__main__':
    data = [[1, 'aLice'], [2, 'bOB']]
    users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})
    print(fix_names(users))