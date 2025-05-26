#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1308.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 不同性别每日分数总计。
"""
import pandas as pd


def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    # 分别处理男性和女性
    df_female = scores[scores['gender'] == 'F']
    df_male = scores[scores['gender'] == 'M']

    def solve(df: pd.DataFrame) -> pd.DataFrame:
        df_sort = df.sort_values(by='day', ascending=True)
        df_sort['total'] = df_sort['score_points'].cumsum()
        return df_sort[['gender', 'day', 'total']]

    df_female = solve(df_female)
    df_male = solve(df_male)

    df_result = pd.concat([df_female, df_male], axis=0)
    return df_result


if __name__ == '__main__':
    data = [['Aron', 'F', '2020-01-01', 17], ['Alice', 'F', '2020-01-07', 23], ['Bajrang', 'M', '2020-01-07', 7],
            ['Khali', 'M', '2019-12-25', 11], ['Slaman', 'M', '2019-12-30', 13], ['Joe', 'M', '2019-12-31', 3],
            ['Jose', 'M', '2019-12-18', 2], ['Priya', 'F', '2019-12-31', 23], ['Priyanka', 'F', '2019-12-30', 17]]
    scores = pd.DataFrame(data, columns=['player_name', 'gender', 'day', 'score_points']).astype(
        {'player_name': 'object', 'gender': 'object', 'day': 'datetime64[ns]', 'score_points': 'Int64'})
    print(running_total(scores))