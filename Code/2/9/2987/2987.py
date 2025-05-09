#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2987.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 寻找房价最贵的城市。
"""
import pandas as pd


def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    national_mean = listings['price'].mean().round(2)
    listings = listings.groupby('city')['price'].mean().round(2).reset_index()
    listings_filtered = listings[listings['price'] > national_mean]
    df_sorted = listings_filtered.sort_values(by=['city'])
    return df_sorted[['city']]


if __name__ == '__main__':
    data = [[113, 'LosAngeles', 7560386],
            [136, 'SanFrancisco', 2380268],
            [92, 'Chicago', 9833209],
            [60, 'Chicago', 5147582],
            [8, 'Chicago', 5274441],
            [79, 'SanFrancisco', 8372065],
            [37, 'Chicago', 7939595],
            [53, 'LosAngeles', 4965123],
            [178, 'SanFrancisco', 999207],
            [51, 'NewYork', 5951718],
            [121, 'NewYork', 2893760]]
    listings = pd.DataFrame(data, columns=['listing_id', 'city', 'price']).astype(
        {'listing_id': 'Int64',
         'city': 'object',
         'price': 'Int64'})
    print(find_expensive_cities(listings))