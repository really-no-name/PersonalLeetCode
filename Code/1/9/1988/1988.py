#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1988.py
作者: Bolun Xu
创建日期: 2025/6/2
版本: 1.0
描述: 找出每所学校的最低分数要求。
"""
import pandas as pd


def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    exam = exam.sort_values(by='score', ascending=False)
    def find_min_score(capacity):
        # 找到所有满足累计学生数 <= capacity的分数
        valid_scores = exam[exam['student_count'] <= capacity]['score']

        if len(valid_scores) > 0:
            # 返回其中最小的分数（即最后一个满足条件的）
            return valid_scores.iloc[-1]
        else:
            # 检查最低分数对应的学生数是否超过capacity
            if exam['student_count'].iloc[0] > capacity:
                return -1
            else:
                # 理论上不应该走到这里，因为如果第一个学生数<=capacity，那么至少第一个分数是有效的
                return exam['score'].iloc[-1]

    result = schools.copy()
    result['score'] = result['capacity'].apply(find_min_score)

    # 只保留需要的列并按任意顺序返回
    return result[['school_id', 'score']]


if __name__ == '__main__':
    data = [[11, 151], [5, 48], [9, 9], [10, 99]]
    schools = pd.DataFrame(data, columns=['school_id', 'capacity']).astype({'school_id': 'Int64', 'capacity': 'Int64'})
    data = [[975, 10], [966, 60], [844, 76], [749, 76], [744, 100]]
    exam = pd.DataFrame(data, columns=['score', 'student_count']).astype({'score': 'Int64', 'student_count': 'Int64'})
    print(find_cutoff_score(schools, exam))