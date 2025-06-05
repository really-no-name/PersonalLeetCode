#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2298.py
作者: Bolun Xu
创建日期: 2025/6/5
版本: 1.0
描述: 周末任务计数。
"""
import pandas as pd


def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    # 分类周末和工作日
    df = tasks.copy()
    df['weekend'] = df['submit_date'].dt.dayofweek >= 5

    # 分类计数
    df_grp = df.groupby('weekend')['task_id'].nunique().reset_index(name='cnt').fillna(0)

    # 获取值
    weekend_cnt = df_grp.loc[df_grp['weekend'] == True, 'cnt'].values[0]
    working_cnt = df_grp.loc[df_grp['weekend'] == False, 'cnt'].values[0]

    df_result = pd.DataFrame([[weekend_cnt, working_cnt]], columns=['weekend_cnt', 'working_cnt'])
    return df_result


if __name__ == '__main__':
    data = [[1, 1, '2022-06-13'], [2, 6, '2022-06-14'], [3, 6, '2022-06-15'], [4, 3, '2022-06-18'],
            [5, 5, '2022-06-19'], [6, 7, '2022-06-19']]
    tasks = pd.DataFrame(data, columns=['task_id', 'assignee_id', 'submit_date']).astype(
        {'task_id': 'Int64', 'assignee_id': 'Int64', 'submit_date': 'datetime64[ns]'})
    print(count_tasks(tasks))