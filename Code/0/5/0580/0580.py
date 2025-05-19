#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0580.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 统计各专业学生人数。
"""
import pandas as pd


def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    student_grp = student.groupby('dept_id')['student_id'].nunique()
    df_merge = department.merge(student_grp, on='dept_id', how='left').fillna(0)
    df_merge = df_merge.rename(columns={'student_id': 'student_number'})
    df_sort = df_merge[['dept_name', 'student_number']].sort_values(by=['student_number', 'dept_name'], ascending=[False, True])
    return df_sort


if __name__ == '__main__':
    data = [[1, 'Jack', 'M', 1], [2, 'Jane', 'F', 1], [3, 'Mark', 'M', 2]]
    student = pd.DataFrame(data, columns=['student_id', 'student_name', 'gender', 'dept_id']).astype(
        {'student_id': 'Int64', 'student_name': 'object', 'gender': 'object', 'dept_id': 'Int64'})
    data = [[1, 'Engineering'], [2, 'Science'], [3, 'Law']]
    department = pd.DataFrame(data, columns=['dept_id', 'dept_name']).astype(
        {'dept_id': 'Int64', 'dept_name': 'object'})
    print(count_students(student, department))