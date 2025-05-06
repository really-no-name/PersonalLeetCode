#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2989.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 班级表现。
"""
import pandas as pd


def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    scores['total'] = scores['assignment1'] + scores['assignment2'] + scores['assignment3']
    max_score = scores['total'].max()
    min_score = scores['total'].min()

    diff = max_score - min_score

    result = pd.DataFrame({'difference_in_score': [diff]})
    return result


if __name__ == '__main__':
    data = [[309, 'Owen', 88, 47, 87], [321, 'Claire', 98, 95, 37], [338, 'Julian', 100, 64, 43],
            [423, 'Peyton', 60, 44, 47], [896, 'David', 32, 37, 50], [235, 'Camila', 31, 53, 69]]
    scores = pd.DataFrame(data,
                          columns=['student_id', 'student_name', 'assignment1', 'assignment2', 'assignment3']).astype(
        {'student_id': 'Int64', 'student_name': 'object', 'assignment1': 'Int64', 'assignment2': 'Int64',
         'assignment3': 'Int64'})
    print(class_performance(scores))