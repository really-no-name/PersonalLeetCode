#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0596.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 超过 5 名学生的课。
"""
import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df_cnt = courses.groupby('class')['student'].count().reset_index()
    df_filt = df_cnt[df_cnt['student'] >= 5]
    return df_filt[['class']]


if __name__ == '__main__':
    data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'],
            ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
    courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student': 'object', 'class': 'object'})
    print(find_classes(courses))