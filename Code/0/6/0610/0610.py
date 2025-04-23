#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0610.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 判断三角形。
"""
import numpy as np
import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = np.where(
        (triangle['x'] + triangle['y'] > triangle['z']) &
        (triangle['x'] + triangle['z'] > triangle['y']) &
        (triangle['y'] + triangle['z'] > triangle['x']),
        'Yes',
        'No'
    )
    return triangle


if __name__ == '__main__':
    data = [[13, 15, 30], [10, 20, 15]]
    triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
    print(triangle_judgement(triangle))