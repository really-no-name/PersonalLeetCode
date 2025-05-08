#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0613.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 直线上的最近距离。
"""
import pandas as pd


def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    point = point.sort_values(by='x')
    point['diff'] = point['x'].diff()  # 相邻行最小差
    ans = point['diff'].min()
    return pd.DataFrame({'shortest': [ans]})


if __name__ == '__main__':
    data = [[-1], [0], [2]]
    point = pd.DataFrame(data, columns=['x']).astype({'x': 'Int64'})
    print(shortest_distance(point))