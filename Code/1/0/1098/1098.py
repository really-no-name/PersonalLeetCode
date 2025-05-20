#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1098.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 小众书籍。
"""
import pandas as pd


def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 筛选过去一年
    orders_filter = orders[(orders['dispatch_date'] >= '2018-06-23') & (orders['dispatch_date'] <= '2019-06-23')]
    orders_grp = orders_filter.groupby('book_id')['quantity'].sum().reset_index()

    # 筛选不满一个月
    books_filter = books[books['available_from'] <= '2019-05-23']

    df_merge = books_filter.merge(orders_grp, on='book_id', how='left')
    df_filter = df_merge[(df_merge['quantity'] < 10) | (df_merge['quantity'].isna())][['book_id', 'name']]
    return df_filter


if __name__ == '__main__':
    data = [[1, 'Kalila And Demna', '2010-01-01'], [2, '28 Letters', '2012-05-12'], [3, 'The Hobbit', '2019-06-10'],
            [4, '13 Reasons Why', '2019-06-01'], [5, 'The Hunger Games', '2008-09-21']]
    books = pd.DataFrame(data, columns=['book_id', 'name', 'available_from']).astype(
        {'book_id': 'Int64', 'name': 'object', 'available_from': 'datetime64[ns]'})
    data = [[1, 1, 2, '2018-07-26'], [2, 1, 1, '2018-11-05'], [3, 3, 8, '2019-06-11'], [4, 4, 6, '2019-06-05'],
            [5, 4, 5, '2019-06-20'], [6, 5, 9, '2009-02-02'], [7, 5, 8, '2010-04-13']]
    orders = pd.DataFrame(data, columns=['order_id', 'book_id', 'quantity', 'dispatch_date']).astype(
        {'order_id': 'Int64', 'book_id': 'Int64', 'quantity': 'Int64', 'dispatch_date': 'datetime64[ns]'})
    print(unpopular_books(books, orders))
