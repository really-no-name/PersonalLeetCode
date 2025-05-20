#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1126.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 查询活跃业务。
"""
import pandas as pd


def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    # Step 1: 计算每个 event_type 的平均 occurrences
    avg_activity = events.groupby('event_type')['occurrences'].mean().reset_index()
    avg_activity.rename(columns={'occurrences': 'avg_occurrences'}, inplace=True)

    # Step 2: 合并原表和平均活动表，标记是否满足条件
    merged = events.merge(avg_activity, on='event_type')
    merged['is_active'] = merged['occurrences'] > merged['avg_occurrences']

    # Step 3: 计算每个 business_id 满足条件的 event_type 数量
    active_counts = merged.groupby('business_id')['is_active'].sum().reset_index()

    # Step 4: 筛选出满足条件的 business_id（至少 2 个 event_type 满足）
    result = active_counts[active_counts['is_active'] >= 2][['business_id']]

    return result


if __name__ == '__main__':
    data = [[1, 'reviews', 7], [3, 'reviews', 3], [1, 'ads', 11], [2, 'ads', 7], [3, 'ads', 6], [1, 'page views', 3],
            [2, 'page views', 12]]
    events = pd.DataFrame(data, columns=['business_id', 'event_type', 'occurrences']).astype(
        {'business_id': 'Int64', 'event_type': 'object', 'occurrences': 'Int64'})
    print(active_businesses(events))
