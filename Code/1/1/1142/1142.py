#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1142.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 过去30天的用户活动 II。
"""
import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df_filt = activity[(activity['activity_date'] > '2019-06-27') & (activity['activity_date'] <= '2019-07-27')]
    df_filt = df_filt.drop_duplicates(subset=['user_id', 'session_id']).reset_index(drop=True)
    total = df_filt.shape[0]
    person_cnt = df_filt['user_id'].nunique()
    if person_cnt == 0:
        return pd.DataFrame({'average_sessions_per_user': [0]})
    else:
        return pd.DataFrame({'average_sessions_per_user': [round(total / person_cnt, 2)]})


if __name__ == '__main__':
    data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'],
            [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'],
            [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'],
            [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'],
            [3, 2, '2019-07-21', 'end_session'], [3, 5, '2019-07-21', 'open_session'],
            [3, 5, '2019-07-21', 'scroll_down'], [3, 5, '2019-07-21', 'end_session'],
            [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
    activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype(
        {'user_id': 'Int64', 'session_id': 'Int64', 'activity_date': 'datetime64[ns]', 'activity_type': 'object'})
    print(user_activity(activity))