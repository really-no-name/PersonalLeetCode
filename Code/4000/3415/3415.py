#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3415.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 查找具有三个连续数字的产品。
时间复杂度：
空间复杂度：
"""
import re
import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    def has_exactly_three_consecutive_digits(s):
        # 匹配恰好三个连续数字
        pattern_three = r'\d{3}'
        # 匹配四个或更多连续数字
        pattern_four_or_more = r'\d{4,}'

        # 检查是否有恰好三个连续数字
        has_three = re.search(pattern_three, s) is not None
        # 检查是否有四个或更多连续数字
        has_four_or_more = re.search(pattern_four_or_more, s) is not None

        # 返回结果：有恰好三个连续数字，且没有四个或更多连续数字
        return has_three and not has_four_or_more

    # 应用函数并筛选出符合条件的行
    filtered_df = products[products['name'].apply(has_exactly_three_consecutive_digits)]

    # 按照product_id升序排序
    result_df = filtered_df.sort_values(by='product_id')
    return result_df