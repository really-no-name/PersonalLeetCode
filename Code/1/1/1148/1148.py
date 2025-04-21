#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1148.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 文章浏览 I。
"""
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # 筛选 author_id == viewer_id 的记录
    screen = views[views['author_id'] == views['viewer_id']]
    # 去重
    screen = screen.drop_duplicates(subset=['author_id'])
    # 排序
    screen = screen.sort_values(by=['author_id'])
    # 重命名列
    result = screen.rename(columns={'author_id': 'id'})[['id']]
    return result


if __name__ == '__main__':
    data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
            [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
    views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
        {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
    print(article_views(views))