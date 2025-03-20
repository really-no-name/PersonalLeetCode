#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2878.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 获取 DataFrame 的大小。
"""
from typing import List
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]
