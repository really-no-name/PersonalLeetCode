#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1341.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 电影评分。
"""
import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movierating: pd.DataFrame) -> pd.DataFrame:
    # 查找评论电影数量最多的用户名。如果出现平局，返回字典序较小的用户名。
    df1_movie_rating = movierating.groupby('user_id')['movie_id'].nunique().reset_index()
    df1_merge = df1_movie_rating.merge(users, on='user_id', how='left')
    df1_merge = df1_merge.sort_values(by=['movie_id', 'name'], ascending=[False, True])
    user_name = df1_merge.head(1)['name'].values[0]

    # 查找在 February 2020 平均评分最高 的电影名称。如果出现平局，返回字典序较小的电影名称。
    df2_filter = movierating[(movierating['created_at'] >= '2020-02-01') & (movierating['created_at'] < '2020-03-01')]
    df2_filter = df2_filter.groupby('movie_id')['rating'].mean().reset_index()  # 计算均值
    df2_merge = df2_filter.merge(movies, on='movie_id', how='left')
    df2_sort = df2_merge.sort_values(by=['rating', 'title'], ascending=[False, True])
    movie_name = df2_sort.head(1)['title'].values[0]

    # 结果
    df_result = pd.DataFrame({'results': [user_name, movie_name]})
    return df_result


if __name__ == '__main__':
    data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
    movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id': 'Int64', 'title': 'object'})
    data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
    users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})
    data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'],
            [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'],
            [3, 2, 4, '2020-02-25']]
    movierating = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype(
        {'movie_id': 'Int64', 'user_id': 'Int64', 'rating': 'Int64', 'created_at': 'datetime64[ns]'})
    print(movie_rating(movies, users, movierating))
