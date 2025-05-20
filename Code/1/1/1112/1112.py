#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1112.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 每位学生的最高成绩。
"""
import pandas as pd


def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments['rank'] = enrollments.groupby('student_id')['grade'].rank(method='dense', ascending=False)
    df_filter = enrollments[enrollments['rank'] == 1]
    df_filter['rank2'] = df_filter.groupby('student_id')['course_id'].rank(method='dense', ascending=True)
    df_filter = df_filter[df_filter['rank2'] == 1]

    df_sort = df_filter[['student_id', 'course_id', 'grade']].sort_values(by=['student_id'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[2, 2, 95], [2, 3, 95], [1, 1, 90], [1, 2, 99], [3, 1, 80], [3, 2, 75], [3, 3, 82]]
    enrollments = pd.DataFrame(data, columns=['student_id', 'course_id', 'grade']).astype(
        {'student_id': 'Int64', 'course_id': 'Int64', 'grade': 'Int64'})
    print(highest_grade(enrollments))