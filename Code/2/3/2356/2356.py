#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2356.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 每位教师所教授的科目种类的数量。
"""
import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result = result.rename(columns={'subject_id': 'cnt'})
    return result


if __name__ == '__main__':
    data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
    teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype(
        {'teacher_id': 'Int64', 'subject_id': 'Int64', 'dept_id': 'Int64'})
    print(count_unique_subjects(teacher))