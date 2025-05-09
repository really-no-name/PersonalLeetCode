#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1623.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 三人国家代表队。
"""
import pandas as pd


def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    df_merge = school_a.merge(school_b, how='cross')
    df_merge = df_merge.merge(school_c, how='cross')
    df_filt = df_merge[(df_merge['student_name_x'] != df_merge['student_name_y']) &
                       (df_merge['student_name_y'] != df_merge['student_name']) &
                       (df_merge['student_name_x'] != df_merge['student_name'])]
    df_filt = df_filt[(df_filt['student_id_x'] != df_filt['student_id_y']) &
                       (df_filt['student_id_y'] != df_filt['student_id']) &
                       (df_filt['student_id_x'] != df_filt['student_id'])]
    df_result = df_filt[['student_name_x', 'student_name_y', 'student_name']]
    df_result = df_result.rename(columns={'student_name_x': 'member_A', 'student_name_y': 'member_B', 'student_name':'member_C'})
    return df_result


if __name__ == '__main__':
    data = [[1, 'Alice'], [2, 'Bob']]
    school_a = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
        {'student_id': 'Int64', 'student_name': 'object'})
    data = [[3, 'Tom']]
    school_b = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
        {'student_id': 'Int64', 'student_name': 'object'})
    data = [[3, 'Tom'], [2, 'Jerry'], [10, 'Alice']]
    school_c = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
        {'student_id': 'Int64', 'student_name': 'object'})
    print(find_valid_triplets(school_a, school_b, school_c))