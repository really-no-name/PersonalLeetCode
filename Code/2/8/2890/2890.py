#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2890.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 重塑数据：融合。
"""
import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_melted = report.melt(
        id_vars=['product'],  # 保持不变的列（产品名称）
        var_name='quarter',  # 新列名（季度）
        value_name='sales'  # 新列名（销售额）
    )
    return report_melted
# melt() 方法用于将宽表转换为长表：
#
# id_vars=['product']：指定 product 列保持不变，作为标识列。
#
# var_name='quarter'：将原来的列名（quarter_1, quarter_2, quarter_3, quarter_4）变成新列 quarter 的值。
#
# value_name='sales'：将原来的销售数据变成新列 sales 的值。