#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2889.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 数据重塑：透视。
"""
import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # result_df = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    result_df = weather.pivot_table(index = 'month', columns = 'city', values = 'temperature')
    return result_df


if __name__ == '__main__':
    data = [['Jacksonville', 'January', 13],
            ['Jacksonville', 'February', 23],
            ['Jacksonville', 'March', 38],
            ['Jacksonville', 'April', 5],
            ['Jacksonville', 'May', 34],
            ['ElPaso', 'January', 20],
            ['ElPaso', 'February', 6],
            ['ElPaso', 'March', 26],
            ['ElPaso', 'April', 2],
            ['ElPaso', 'May', 43]]
    weather = pd.DataFrame(data, columns=['city', 'month', 'temperature']).astype(
        {'city': 'object', 'month': 'object', 'temperature': 'int'}
    )
    print(pivotTable(weather))