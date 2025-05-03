#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1693.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 每天的领导和合伙人。
"""
import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name'])[['lead_id', 'partner_id']].nunique().reset_index()
    result = result.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})
    return result


if __name__ == '__main__':
    data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2],
            ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2],
            ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2],
            ['2020-12-7', 'honda', 2, 1]]
    daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype(
        {'date_id': 'datetime64[ns]', 'make_name': 'object', 'lead_id': 'Int64', 'partner_id': 'Int64'})
    print(daily_leads_and_partners(daily_sales))