#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0585.py
作者: Bolun Xu
创建日期: 2025/5/18
版本: 1.0
描述: 2016年的投资。
"""
import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    #  2015 年的投保额 (tiv_2015) 至少跟一个其他投保人在 2015 年的投保额相同
    condition_1 = insurance.duplicated(subset='tiv_2015', keep=False)

    # 所在的城市必须与其他投保人都不同
    condition_2 = ~insurance.duplicated(subset=['lat', 'lon'], keep=False)

    # 求和
    df_filter = insurance[condition_1 & condition_2]
    result = round(df_filter['tiv_2016'].sum(), 2)
    return pd.DataFrame({'tiv_2016': [result]})


if __name__ == '__main__':
    data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
    insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype(
        {'pid': 'Int64', 'tiv_2015': 'Float64', 'tiv_2016': 'Float64', 'lat': 'Float64', 'lon': 'Float64'})
    print(find_investments(insurance))