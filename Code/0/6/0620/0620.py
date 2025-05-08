#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0620.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 有趣的电影。
"""
import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df_filt = cinema[cinema['id'] % 2 == 1]  # id 为奇数
    df_filt = df_filt[df_filt['description'] != 'boring']
    df_sort = df_filt.sort_values(by=['rating'], ascending=False)
    return df_sort


if __name__ == '__main__':
    data = [[1, 'War', 'great 3D', 8.9],
            [2, 'Science', 'fiction', 8.5],
            [3, 'irish', 'boring', 6.2],
            [4, 'Ice song', 'Fantacy', 8.6],
            [5, 'House card', 'Interesting', 9.1]]
    cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype(
        {'id': 'Int64', 'movie': 'object', 'description': 'object', 'rating': 'Float64'})
    print(not_boring_movies(cinema))