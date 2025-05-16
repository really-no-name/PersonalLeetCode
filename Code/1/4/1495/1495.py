#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1495.py
作者: Bolun Xu
创建日期: 2025/5/16
版本: 1.0
描述: 上月播放的儿童适宜电影。
"""
import pandas as pd


def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    df_filter = tv_program[(tv_program['program_date'] >= '2020-06-01 00:00') & (tv_program['program_date'] < '2020-07-01 00:00')]  # filter June
    content['content_id'] = content['content_id'].astype(int)  # 两表中 `content_id` 列格式不同，merge会报错
    df_merge = df_filter.merge(content, on='content_id', how='left')
    df_merge = df_merge[(df_merge['Kids_content'] == 'Y') & (df_merge['content_type'] == 'Movies')][['title']]  # 筛选电影 和 儿童适宜
    df_drop = df_merge.drop_duplicates(subset=['title'], keep='first')  # 去重
    return df_drop


if __name__ == '__main__':
    data = [['2020-06-10 08:00', 1, 'LC-Channel'],
            ['2020-05-11 12:00', 2, 'LC-Channel'],
            ['2020-05-12 12:00', 3, 'LC-Channel'],
            ['2020-05-13 14:00', 4, 'Disney Ch'],
            ['2020-06-18 14:00', 4, 'Disney Ch'],
            ['2020-07-15 16:00', 5, 'Disney Ch']]
    tv_program = pd.DataFrame(data, columns=['program_date', 'content_id', 'channel']).astype(
        {'program_date': 'datetime64[ns]', 'content_id': 'Int64', 'channel': 'object'})
    data = [[1, 'Leetcode Movie', 'N', 'Movies'],
            [2, 'Alg. for Kids', 'Y', 'Series'],
            [3, 'Database Sols', 'N', 'Series'],
            [4, 'Aladdin', 'Y', 'Movies'],
            [5, 'Cinderella', 'Y', 'Movies']]
    content = pd.DataFrame(data, columns=['content_id', 'title', 'Kids_content', 'content_type']).astype(
        {'content_id': 'object', 'title': 'object', 'Kids_content': 'object', 'content_type': 'object'})
    print(friendly_movies(tv_program, content))
