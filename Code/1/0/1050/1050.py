#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1050.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 合作过至少三次的演员和导演。
"""
import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped_df = actor_director.groupby(['actor_id', 'director_id']).nunique().reset_index()
    screen = grouped_df[grouped_df['timestamp'] >= 3]
    return screen[['actor_id', 'director_id']]


if __name__ == '__main__':
    data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
    actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype(
        {'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'})
    print(actors_and_directors(actor_director))
