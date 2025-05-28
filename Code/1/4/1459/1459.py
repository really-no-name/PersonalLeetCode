#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1459.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 矩形面积。
"""
import pandas as pd


def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    # 获取所有点的组合
    df = pd.merge(points, points, how='cross')
    df = df[df['id_x'] < df['id_y']]
    df = df.rename(columns={'id_x': 'p1', 'id_y': 'p2', 'x_value_x': 'p1_x', 'y_value_x': 'p1_y', 'x_value_y': 'p2_x', 'y_value_y': 'p2_y'})

    # 计算面积
    def calc_area(row):
        return abs(row['p2_x'] - row['p1_x']) * abs(row['p2_y'] - row['p1_y'])

    df['area'] = df.apply(calc_area, axis=1)

    # 排除面积为0
    df_filter = df[df['area'] > 0][['p1', 'p2', 'area']]

    # 排序
    df_sort = df_filter.sort_values(by=['area', 'p1', 'p2'], ascending=[False, True, True])
    return df_sort


if __name__ == '__main__':
    data = [[1, 2, 7], [2, 4, 8], [3, 2, 10]]
    points = pd.DataFrame(data, columns=['id', 'x_value', 'y_value']).astype(
        {'id': 'Int64', 'x_value': 'Int64', 'y_value': 'Int64'})
    print(rectangles_area(points))