#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1211.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 查询结果的质量和占比。
"""
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

def my_round(x):
    return Decimal(x).quantize(Decimal('.00'), rounding=ROUND_HALF_UP)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    grouped = queries.groupby('query_name').agg(
        quality=('quality', lambda x: my_round(x.mean())),
        poor_query_percentage=('rating', lambda x: my_round((x < 3).sum() / len(x) * 100))
    ).reset_index()

    return grouped


if __name__ == '__main__':
    data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1],
            ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
    queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype(
        {'query_name': 'object', 'result': 'object', 'position': 'Int64', 'rating': 'Int64'})
    print(queries_stats(queries))


