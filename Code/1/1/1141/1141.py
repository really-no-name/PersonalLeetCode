#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1141.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 查询近30天活跃用户数。
"""
import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    screen = activity[(activity['activity_date'] > '2019-06-27') &
                 (activity['activity_date'] <= '2019-07-27')]
    # 按日期分组，计算每天的不同用户数
    daily_active_users = screen.groupby('activity_date')['user_id'].nunique().reset_index()
    # 重命名列以符合输出要求
    daily_active_users.columns = ['day', 'active_users']
    return daily_active_users


if __name__ == '__main__':
    data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'],
            [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'],
            [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'],
            [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'],
            [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'],
            [4, 3, '2019-06-25', 'end_session']]
    activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype(
        {'user_id': 'Int64', 'session_id': 'Int64', 'activity_date': 'datetime64[ns]', 'activity_type': 'object'})
    print(user_activity(activity))