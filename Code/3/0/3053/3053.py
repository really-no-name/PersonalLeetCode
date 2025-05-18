#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3053.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 根据长度分类三角形。
"""
import pandas as pd


def relation(row):
    if row['A'] + row['B'] > row['C'] and row['A'] + row['C'] > row['B'] and row['B'] + row['C'] > row['A']:
        if row['A'] == row['B'] and row['B'] == row['C']:
            return 'Equilateral'
        elif row['A'] != row['B'] and row['B'] != row['C'] and row['C'] != row['A']:
            return 'Scalene'
        else:
            return 'Isosceles'
    else:
        return 'Not A Triangle'


def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    triangles['triangle_type'] = triangles.apply(relation, axis=1)
    return triangles[['triangle_type']]


if __name__ == '__main__':
    data = [[20, 20, 23], [20, 20, 20], [20, 21, 22], [13, 14, 30]]
    triangles = pd.DataFrame(data, columns=['A', 'B', 'C']).astype({'A': 'Int64', 'B': 'Int64', 'C': 'Int64'})
    print(type_of_triangle(triangles))
