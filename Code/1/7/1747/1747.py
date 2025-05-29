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
    # 按account_id分组
    grouped = log_info.groupby('account_id')

    banned_accounts = []

    for account_id, group in grouped:
        # 对每个账户的所有登录记录进行检查
        n = len(group)
        found = False

        # 比较所有可能的记录对
        for i in range(n):
            if found:
                break
            for j in range(i + 1, n):
                # 获取两条记录
                row1 = group.iloc[i]
                row2 = group.iloc[j]

                # 检查IP地址是否不同
                if row1['ip_address'] != row2['ip_address']:
                    # 检查时间是否有重叠
                    # 重叠条件：row1的登录时间在row2的登录和注销之间，或者相反
                    if not (row1['logout'] < row2['login'] or row2['logout'] < row1['login']):
                        banned_accounts.append(account_id)
                        found = True
                        break

    # 去重并创建结果DataFrame
    result = pd.DataFrame({'account_id': list(set(banned_accounts))})
    return result


if __name__ == '__main__':
    data = [[1, 1, '2021-02-01 09:00:00', '2021-02-01 09:30:00'], [1, 2, '2021-02-01 08:00:00', '2021-02-01 11:30:00'],
            [2, 6, '2021-02-01 20:30:00', '2021-02-01 22:00:00'], [2, 7, '2021-02-02 20:30:00', '2021-02-02 22:00:00'],
            [3, 9, '2021-02-01 16:00:00', '2021-02-01 16:59:59'], [3, 13, '2021-02-01 17:00:00', '2021-02-01 17:59:59'],
            [4, 10, '2021-02-01 16:00:00', '2021-02-01 17:00:00'],
            [4, 11, '2021-02-01 17:00:00', '2021-02-01 17:59:59']]
    log_info = pd.DataFrame(data, columns=['account_id', 'ip_address', 'login', 'logout']).astype(
        {'account_id': 'Int64', 'ip_address': 'Int64', 'login': 'datetime64[ns]', 'logout': 'datetime64[ns]'})
    print(leetflex_banned_accnts(log_info))