#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1783.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 大满贯数量。
"""
import pandas as pd


def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    data = [[1, 'Nadal'], [2, 'Federer'], [3, 'Novak']]
    players = pd.DataFrame(data, columns=['player_id', 'player_name']).astype(
        {'player_id': 'Int64', 'player_name': 'object'})
    data = [[2018, 1, 1, 1, 1], [2019, 1, 1, 2, 2], [2020, 2, 1, 2, 2]]
    championships = pd.DataFrame(data, columns=['year', 'Wimbledon', 'Fr_open', 'US_open', 'Au_open']).astype(
        {'year': 'Int64', 'Wimbledon': 'Int64', 'Fr_open': 'Int64', 'US_open': 'Int64', 'Au_open': 'Int64'})