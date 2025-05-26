#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3421.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 查找进步的学生。
"""
import pandas as pd


def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # 筛选 同一科目 至少参加过两个不同日期的考试
    condition = scores.groupby(['student_id', 'subject'])['exam_date'].transform('nunique') >= 2
    df_filter = scores[condition]

    # 排序， 分别保留第一次和最后一次成绩
    df_sort = df_filter.sort_values('exam_date')
    df_first = df_sort.drop_duplicates(subset=['student_id', 'subject'], keep='first')
    df_first = df_first.rename(columns={'score': 'first_score'})
    df_last = df_sort.drop_duplicates(subset=['student_id', 'subject'], keep='last')
    df_last = df_last.rename(columns={'score': 'latest_score'})

    # 合并,并筛选进步
    df_merge = pd.merge(df_first, df_last, on=['student_id', 'subject'])

    df_result = df_merge[df_merge['first_score'] < df_merge['latest_score']][['student_id', 'subject', 'first_score', 'latest_score']]
    df_result = df_result.sort_values(['student_id', 'subject'], ascending=True)
    return df_result


if __name__ == '__main__':
    data = [[101, 'Math', 70, '2023-01-15'], [101, 'Math', 85, '2023-02-15'], [101, 'Physics', 65, '2023-01-15'],
            [101, 'Physics', 60, '2023-02-15'], [102, 'Math', 80, '2023-01-15'], [102, 'Math', 85, '2023-02-15'],
            [103, 'Math', 90, '2023-01-15'], [104, 'Physics', 75, '2023-01-15'], [104, 'Physics', 85, '2023-02-15']]
    scores = pd.DataFrame(data, columns=["student_id", "subject", "score", "exam_date"]).astype({
        'student_id': int, 'subject': str, 'score': int, 'exam_date': str
    })
    print(find_students_who_improved(scores))
