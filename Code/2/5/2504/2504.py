#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2504.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 把名字和职业联系起来。
"""
import pandas as pd


def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    person['profession_initial'] = person['profession'].str[0].str.upper()
    person['name'] = person['name'] + '(' + person['profession_initial'] + ')'
    result = person[['person_id', 'name']]
    result = result.sort_values(by=['person_id'], ascending=False)
    return result


if __name__ == '__main__':
    data = [[1, 'Alex', 'Singer'], [3, 'Alice', 'Actor'], [2, 'Bob', 'Player'], [4, 'Messi', 'Doctor'],
            [6, 'Tyson', 'Engineer'], [5, 'Meir', 'Lawyer']]
    person = pd.DataFrame(data, columns=['person_id', 'name', 'profession']).astype(
        {'person_id': 'Int64', 'name': 'object', 'profession': 'object'})
    print(concatenate_info(person))