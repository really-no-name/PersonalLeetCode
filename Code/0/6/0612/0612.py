#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0612.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 平面上的最近距离。
"""
from itertools import combinations

import numpy as np
import pandas as pd


def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    """
    报告 Point2D 表中任意两点之间的最短距离。保留 2 位小数 。
    """
    # 提取所有点的坐标
    points = point2_d[['x', 'y']].values

    # 计算所有点对之间的距离
    min_dist = np.inf
    for (x1, y1), (x2, y2) in combinations(points, 2):
        dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if dist < min_dist:
            min_dist = dist

    # 四舍五入到2位小数
    return pd.DataFrame({'shortest': [round(min_dist, 2)]})


if __name__ == '__main__':
    data = [[-1, -1], [0, 0], [-1, -2]]
    point2_d = pd.DataFrame(data, columns=['x', 'y']).astype({'x': 'Int64', 'y': 'Int64'})
    print(shortest_distance(point2_d))