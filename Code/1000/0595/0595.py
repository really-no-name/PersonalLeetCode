#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0595.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 大的国家。
"""
import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # 筛选条件：面积 >= 300万 或 人口 >= 2500万
    ans = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    # 返回指定的列
    return ans[['name', 'population', 'area']]
