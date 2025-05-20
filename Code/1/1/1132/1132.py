#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1132.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 报告的记录 II。
"""
import pandas as pd


def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    # 求出每日垃圾广告
    df_spam = actions[actions['extra'] == 'spam']
    daily_spam_df = df_spam.groupby('action_date')['post_id'].nunique().reset_index(name='spam_count')

    # 求出每日移除的垃圾广告
    daily_remove_df = pd.merge(actions, removals, left_on='post_id', right_on='post_id', how='right')
    daily_remove_df = daily_remove_df[daily_remove_df['extra'] == 'spam'].groupby('action_date')['post_id'].nunique().reset_index(name='removal_count')

    # 合并数据，填充null值
    result_df = pd.merge(daily_spam_df, daily_remove_df, left_on='action_date', right_on='action_date', how='left')
    result_df['removal_count'] = result_df['removal_count'].fillna(0).astype(int)

    # 计算每日移除率
    result_df['daily_percent'] = (result_df['removal_count'] / result_df['spam_count'] * 100).round(2)

    # 计算平均每日移除率
    average_daily_percent = result_df['daily_percent'].mean().round(2)

    # 返回结果
    return pd.DataFrame({'average_daily_percent': [average_daily_percent]})


if __name__ == '__main__':
    data = [[1, 1, '2019-07-01', 'view', None], [1, 1, '2019-07-01', 'like', None], [1, 1, '2019-07-01', 'share', None],
            [2, 2, '2019-07-04', 'view', None], [2, 2, '2019-07-04', 'report', 'spam'],
            [3, 4, '2019-07-04', 'view', None], [3, 4, '2019-07-04', 'report', 'spam'],
            [4, 3, '2019-07-02', 'view', None], [4, 3, '2019-07-02', 'report', 'spam'],
            [5, 2, '2019-07-03', 'view', None], [5, 2, '2019-07-03', 'report', 'racism'],
            [5, 5, '2019-07-03', 'view', None], [5, 5, '2019-07-03', 'report', 'racism']]
    actions = pd.DataFrame(data, columns=['user_id', 'post_id', 'action_date', 'action', 'extra']).astype(
        {'user_id': 'Int64', 'post_id': 'Int64', 'action_date': 'datetime64[ns]', 'action': 'object',
         'extra': 'object'})
    data = [[2, '2019-07-20'], [3, '2019-07-18']]
    removals = pd.DataFrame(data, columns=['post_id', 'remove_date']).astype(
        {'post_id': 'Int64', 'remove_date': 'datetime64[ns]'})
    print(reported_posts(actions, removals))