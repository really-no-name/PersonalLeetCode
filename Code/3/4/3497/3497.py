#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3497.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 分析订阅转化。
"""
import pandas as pd


def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    # 查找从免费试用转为付费订阅的用户
    free_users = user_activity[user_activity['activity_type'] == 'free_trial']['user_id'].unique()
    paid_users = user_activity[user_activity['activity_type'] == 'paid']['user_id'].unique()
    converted_users = list(set(free_users) & set(paid_users))
    df_filt = user_activity[user_activity['user_id'].isin(converted_users)]

    # 计算每位用户在 免费试用 期间的 平均每日活动时长（四舍五入至小数点后 2 位）
    free_df = df_filt[df_filt['activity_type'] == 'free_trial']
    free_avg = free_df.groupby('user_id')['activity_duration'].mean().reset_index()
    free_avg = free_avg.rename(columns={'activity_duration': 'trial_avg_duration'})
    free_avg['trial_avg_duration'] = free_avg['trial_avg_duration'].apply(lambda x: round(x + 0.000000000005, 2))  # 保留两位小数

    # 计算每位用户在 付费 订阅期间的 平均每日活动时长（四舍五入到小数点后 2 位）
    paid_df = df_filt[df_filt['activity_type'] == 'paid']
    paid_avg = paid_df.groupby('user_id')['activity_duration'].mean().reset_index()
    paid_avg = paid_avg.rename(columns={'activity_duration': 'paid_avg_duration'})
    paid_avg['paid_avg_duration'] = paid_avg['paid_avg_duration'].apply(lambda x: round(x + 0.000000000005, 2))

    result_df = pd.merge(free_avg, paid_avg, on='user_id', how='left')
    result_sort_df = result_df.sort_values(by='user_id')
    return result_sort_df


if __name__ == '__main__':
    data = [[1, '2023-01-01', 'free_trial', 45],
            [1, '2023-01-02', 'free_trial', 30],
            [1, '2023-01-05', 'free_trial', 60],
            [1, '2023-01-10', 'paid', 75],
            [1, '2023-01-12', 'paid', 90],
            [1, '2023-01-15', 'paid', 65],
            [2, '2023-02-01', 'free_trial', 55],
            [2, '2023-02-03', 'free_trial', 25],
            [2, '2023-02-07', 'free_trial', 50],
            [2, '2023-02-10', 'cancelled', 0],
            [3, '2023-03-05', 'free_trial', 70],
            [3, '2023-03-06', 'free_trial', 60],
            [3, '2023-03-08', 'free_trial', 80],
            [3, '2023-03-12', 'paid', 50],
            [3, '2023-03-15', 'paid', 55],
            [3, '2023-03-20', 'paid', 85],
            [4, '2023-04-01', 'free_trial', 40],
            [4, '2023-04-03', 'free_trial', 35],
            [4, '2023-04-05', 'paid', 45],
            [4, '2023-04-07', 'cancelled', 0]]
    user_activity = pd.DataFrame(data, columns=['user_id', 'activity_date', 'activity_type', 'activity_duration']).astype(
        {'user_id': 'Int64',
         'activity_date': 'datetime64[ns]',
         'activity_type': 'str',
         'activity_duration': 'Int64'})
    print(analyze_subscription_conversion(user_activity))