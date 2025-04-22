#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0182.py
作者: Bolun Xu
创建日期: 2025/4/22
版本: 1.0
描述: 查找重复的电子邮箱。
"""
import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person['email'].value_counts()
    res = res[res > 1].index
    return pd.DataFrame(res)


if __name__ == '__main__':
    data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
    person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'Int64', 'email': 'object'})
    print(duplicate_emails(person))
