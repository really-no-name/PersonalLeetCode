#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1280.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 学生们参加各科测试的次数。
"""
import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    group_df = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    print(group_df)

    all_subject = pd.merge(students, subjects, how='cross')

    total = pd.merge(all_subject, group_df, on=['student_id', 'subject_name'], how='left')
    print(total)

    total['attended_exams'] = total['attended_exams'].fillna(0).astype(int)

    total.sort_values(['student_id', 'subject_name'], inplace=True)
    return total[['student_id', 'student_name', 'subject_name', 'attended_exams']]



if __name__ == '__main__':
    data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
    students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
        {'student_id': 'Int64', 'student_name': 'object'})
    data = [['Math'], ['Physics'], ['Programming']]
    subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})
    data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'],
            [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
    examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
        {'student_id': 'Int64', 'subject_name': 'object'})
    print(students_and_examinations(students, subjects, examinations))