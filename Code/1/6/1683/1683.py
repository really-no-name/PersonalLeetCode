#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1683.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0
描述: 无效的推文。
"""
import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['str_len'] = tweets['content'].str.len()
    return tweets[tweets['str_len'] > 15][['tweet_id']]

if __name__ == '__main__':
    data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
    tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})
    print(invalid_tweets(tweets))