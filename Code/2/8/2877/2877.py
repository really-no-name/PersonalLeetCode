#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2877.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 从表中创建 DataFrame。
"""
from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age']).astype({'student_id': int, 'age': int})


if __name__ == '__main__':
    print(createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]]))