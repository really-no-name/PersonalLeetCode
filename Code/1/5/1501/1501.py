#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1501.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 可以放心投资的国家。
"""
import pandas as pd


def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    df_person = person.copy()
    df_person['country_code'] = df_person['phone_number'].str[:3]  # 获取 country_code
    df_person = df_person[['id', 'country_code']]

    # 统计每个 ID 打电话的时长 和 电话次数
    caller_df = calls.groupby('caller_id').agg({'duration': 'sum', 'callee_id': 'count'}) \
        .reset_index() \
        .rename(columns={'caller_id': 'id', 'callee_id': 'cnt'})
    callee_df = calls.groupby('callee_id').agg({'duration': 'sum', 'caller_id': 'count'}) \
        .reset_index() \
        .rename(columns={'callee_id': 'id', 'caller_id': 'cnt'})
    df_calls = pd.merge(caller_df, callee_df, on='id', how='outer').fillna(0)
    df_calls['duration'] = df_calls['duration_x'] + df_calls['duration_y']
    df_calls['cnt'] = df_calls['cnt_x'] + df_calls['cnt_y']
    df_calls = df_calls[['id', 'duration', 'cnt']]

    # 合并 并 计算 国家平均通话时长
    df_merge = df_person.merge(df_calls, on='id', how='left')
    df_merge = df_merge.groupby('country_code') \
        .agg({'duration': 'sum', 'cnt': 'sum'}) \
        .reset_index()
    df_merge['avg'] = df_merge['duration'] / df_merge['cnt']

    # 计算 全球平均通话时长
    global_call_duration_avg = calls['duration'].sum() / calls.shape[0]

    # 筛选 大于
    df_filter = df_merge[df_merge['avg'] > global_call_duration_avg][['country_code']]

    # 结果
    df_result = country[country['country_code'].isin(df_filter['country_code'])]
    df_result = df_result[['name']].rename(columns={'name': 'country'})
    return df_result


if __name__ == '__main__':
    data = [[3, 'Jonathan', '051-1234567'], [12, 'Elvis', '051-7654321'], [1, 'Moncef', '212-1234567'],
            [2, 'Maroua', '212-6523651'], [7, 'Meir', '972-1234567'], [9, 'Rachel', '972-0011100']]
    person = pd.DataFrame(data, columns=['id', 'name', 'phone_number']).astype(
        {'id': 'Int64', 'name': 'object', 'phone_number': 'object'})
    data = [['Peru', '051'], ['Israel', '972'], ['Morocco', '212'], ['Germany', '049'], ['Ethiopia', '251']]
    country = pd.DataFrame(data, columns=['name', 'country_code']).astype({'name': 'object', 'country_code': 'object'})
    data = [[1, 9, 33], [2, 9, 4], [1, 2, 59], [3, 12, 102], [3, 12, 330], [12, 3, 5], [7, 9, 13], [7, 1, 3], [9, 7, 1],
            [1, 7, 7]]
    calls = pd.DataFrame(data, columns=['caller_id', 'callee_id', 'duration']).astype(
        {'caller_id': 'Int64', 'callee_id': 'Int64', 'duration': 'Int64'})
    print(find_safe_countries(person, country, calls))