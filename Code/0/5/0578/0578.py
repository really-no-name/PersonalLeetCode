#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0578.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 查询回答率最高的问题。
"""
import pandas as pd


def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    # 重组数据
    df_pivot = survey_log.pivot_table(
        index='question_id',
        columns='action',
        aggfunc="size",  # 统计出现次数
        fill_value=0  # 未出现的组合填充 0
    ).reset_index()
    df_pivot.columns.name = None

    def rate(row):
        if row['answer'] == 0 or row['show'] == 0:
            return 0
        else:
            return row['answer'] / row['show']
    df_pivot['rate'] = df_pivot.apply(rate, axis=1)

    df_sort = df_pivot.sort_values(by=['rate', 'question_id'], ascending=[False, True])

    df_result = df_sort.head(1).rename(columns={'question_id': 'survey_log'})
    return df_result[['survey_log']]


if __name__ == '__main__':
    data = [[5, 'show', 285, None, 1, 123], [5, 'answer', 285, 124124, 1, 124], [5, 'show', 369, None, 2, 125],
            [5, 'skip', 369, None, 2, 126]]
    survey_log = pd.DataFrame(data, columns=['id', 'action', 'question_id', 'answer_id', 'q_num', 'timestamp']).astype(
        {'id': 'Int64', 'action': 'object', 'question_id': 'Int64', 'answer_id': 'Int64', 'q_num': 'Int64',
         'timestamp': 'Int64'})
    print(get_the_question(survey_log))