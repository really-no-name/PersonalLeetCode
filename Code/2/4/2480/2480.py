#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2480.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 形成化学键。
"""
import pandas as pd


def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    metal = elements[elements['type'] == 'Metal'].rename(columns={'symbol': 'metal'})
    nonmetal = elements[elements['type'] == 'Nonmetal'].rename(columns={'symbol': 'nonmetal'})
    merged_df = metal.merge(nonmetal, how='cross')
    return merged_df[['metal', 'nonmetal']]


if __name__ == '__main__':
    data = [['He', 'Noble', 0], ['Na', 'Metal', 1], ['Ca', 'Metal', 2], ['La', 'Metal', 3], ['Cl', 'Nonmetal', 1],
            ['O', 'Nonmetal', 2], ['N', 'Nonmetal', 3]]
    elements = pd.DataFrame(data, columns=['symbol', 'type', 'electrons']).astype(
        {'symbol': 'object', 'type': 'object', 'electrons': 'Int64'})
    print(form_bond(elements))