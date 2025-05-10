#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2669.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 统计 Spotify 排行榜上艺术家出现次数。
"""
import pandas as pd


def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    df_cnt = spotify.groupby('artist')['id'].nunique().reset_index()
    df_cnt = df_cnt.rename(columns={'id': 'occurrences'})
    df_sort = df_cnt.sort_values(by=['occurrences', 'artist'], ascending=[False, True])
    return df_sort


if __name__ == '__main__':
    data = [[303651, "Heart Won't Forget", 'Ed Sheeran'],
            [1046089, 'Shape of you', 'Sia'],
            [33445, "I'm the one", 'DJ Khalid'],
            [811266, 'Young Dumb & Broke', 'DJ Khalid'],
            [505727, 'Happier', 'Ed Sheeran']]
    spotify = pd.DataFrame(data, columns=['id', 'track_name', 'artist']).astype(
        {'id': 'Int64', 'track_name': 'object', 'artist': 'object'})
    print(count_occurrences(spotify))
