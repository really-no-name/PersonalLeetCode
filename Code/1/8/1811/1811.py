#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1811.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 寻找面试候选人。
"""
import pandas as pd


def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # 在 三场及更多不同的 比赛中赢得 金牌
    df_cnt = contests.drop(labels=['contest_id', 'silver_medal', 'bronze_medal'], axis=1) \
        .stack().value_counts() \
        .reset_index()
    df_cnt.columns = ['user_id', 'cnt']
    df_cnt_filter = df_cnt[df_cnt['cnt'] >= 3]
    # 存入结果
    df_result1 = df_cnt_filter[['user_id']]

    # 在 连续三场及更多 比赛中赢得 任意 奖牌
    df_contests = contests.sort_values(by=['contest_id'], ascending=True)  # 排序
    df_contests['medal'] = df_contests[['gold_medal', 'silver_medal', 'bronze_medal']].apply(set, axis=1)  # 所有获奖者聚合为集合
    df_contests['next1'] = df_contests['medal'].shift(-1)
    df_contests['next2'] = df_contests['medal'].shift(-2)
    df_contests = df_contests[(~df_contests['next1'].isna()) & (~df_contests['next2'].isna())] \
        .drop(labels=['gold_medal', 'silver_medal', 'bronze_medal'], axis=1)
    # 求交集
    # 计算交集后使用explode展开
    df_result2 = df_contests.apply(lambda row: list(row['medal'] & row['next1'] & row['next2']), axis=1) \
        .explode() \
        .to_frame(name='user_id') \
        .reset_index(drop=True)

    # 合并结果，去重，合并获取信息
    df_result = pd.concat([df_result1, df_result2])
    df_users = users[users['user_id'].isin(df_result['user_id'])]
    return df_users[['name', 'mail']]


if __name__ == '__main__':
    data = [[190, 1, 5, 2], [191, 2, 3, 5], [192, 5, 2, 3], [193, 1, 3, 5], [194, 4, 5, 2], [195, 4, 2, 1],
            [196, 1, 5, 2]]
    contests = pd.DataFrame(data, columns=['contest_id', 'gold_medal', 'silver_medal', 'bronze_medal']).astype(
        {'contest_id': 'Int64', 'gold_medal': 'Int64', 'silver_medal': 'Int64', 'bronze_medal': 'Int64'})
    data = [[1, 'sarah@leetcode.com', 'Sarah'], [2, 'bob@leetcode.com', 'Bob'], [3, 'alice@leetcode.com', 'Alice'],
            [4, 'hercy@leetcode.com', 'Hercy'], [5, 'quarz@leetcode.com', 'Quarz']]
    users = pd.DataFrame(data, columns=['user_id', 'mail', 'name']).astype(
        {'user_id': 'Int64', 'mail': 'object', 'name': 'object'})
    print(find_interview_candidates(contests, users))