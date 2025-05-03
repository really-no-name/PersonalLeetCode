#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2377.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 整理奥运表。
"""
import pandas as pd


def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    result = olympic.sort_values(['gold_medals', 'silver_medals', 'bronze_medals', 'country'], ascending=[False, False, False, True])
    return result


if __name__ == '__main__':
    data = [['China', 10, 10, 20], ['South Sudan', 0, 0, 1], ['USA', 10, 10, 20], ['Israel', 2, 2, 3],
            ['Egypt', 2, 2, 2]]
    olympic = pd.DataFrame(data, columns=['country', 'gold_medals', 'silver_medals', 'bronze_medals']).astype(
        {'country': 'object', 'gold_medals': 'Int64', 'silver_medals': 'Int64', 'bronze_medals': 'Int64'})
    print(sort_table(olympic))