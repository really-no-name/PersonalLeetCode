#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1661.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 每台机器的进程平均运行时间。
"""
import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_df = activity[activity['activity_type'] == 'start']
    end_df = activity[activity['activity_type'] == 'end']

    # 合并开始和结束记录，基于machine_id和process_id
    merged_df = pd.merge(
        start_df,
        end_df,
        on=['machine_id', 'process_id'],
        suffixes=('_start', '_end')
    )

    # 计算每个进程的耗时
    merged_df['processing_time'] = merged_df['timestamp_end'] - merged_df['timestamp_start']
    print(merged_df)
    # 按机器分组计算平均耗时
    result = merged_df.groupby('machine_id')['processing_time'].mean().round(3).reset_index()
    result.columns = ['machine_id', 'processing_time']
    return result


if __name__ == '__main__':
    data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12],
            [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42],
            [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
    activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype(
        {'machine_id': 'Int64', 'process_id': 'Int64', 'activity_type': 'object', 'timestamp': 'Float64'})
    print(get_average_time(activity))