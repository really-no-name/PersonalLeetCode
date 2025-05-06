#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3358.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 评分为 NULL 的图书。
"""
import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    result = books[books['rating'].isna()]
    result = result.sort_values(by=['book_id'])
    return result[['book_id', 'title', 'author', 'published_year']]


if __name__ == '__main__':
    data = [[1, 'The Great Gatsby', 'F. Scott', 1925, 4.5], [2, 'To Kill a Mockingbird', 'Harper Lee', 1960, None],
            [3, 'Pride and Prejudice', 'Jane Austen', 1813, 4.8],
            [4, 'The Catcher in the Rye', 'J.D. Salinger', 1951, None], [5, 'Animal Farm', 'George Orwell', 1945, 4.2],
            [6, 'Lord of the Flies', 'William Golding', 1954, None]]
    books = pd.DataFrame(data, columns=['book_id', 'title', 'author', 'published_year', 'rating']).astype(
        {"book_id": "int", "title": "str", "author": "str", "published_year": "int", "rating": "float"})
    print(find_unrated_books(books))