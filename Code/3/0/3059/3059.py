#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3059.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 找到所有不同的邮件域名。
"""
import pandas as pd


def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\.com$'
    df_filt = emails[emails['email'].str.contains(pattern, regex=True, na=False)]
    
    df_filt['email_domain'] = df_filt['email'].str.split('@').str[1]
    df_cnt = df_filt.groupby(['email_domain'])['email'].count().reset_index()  # 无需去重
    df_cnt = df_cnt.rename(columns={'email':'count'})
    df_sort = df_cnt.sort_values(by=['email_domain'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[336, 'hwkiy@test.edu'], [489, 'adcmaf@outlook.com'], [449, 'vrzmwyum@yahoo.com'], [95, 'tof@test.edu'],
            [320, 'jxhbagkpm@example.org'], [411, 'zxcf@outlook.com']]
    emails = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'Int64', 'email': 'object'})
    print(find_unique_email_domains(emails))