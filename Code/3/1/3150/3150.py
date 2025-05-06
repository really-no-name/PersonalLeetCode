#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3150.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 无效的推文 II。
"""
import pandas as pd


def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['len'] = tweets['content'].str.len()
    tweets['mentions'] = tweets['content'].str.count(r'@\w+')
    tweets['hashtags'] = tweets['content'].str.count(r'#\w+')

    # 筛选满足任一条件的推文
    invalid = tweets[
        (tweets['len'] > 140) |
        (tweets['mentions'] > 3) |
        (tweets['hashtags'] > 3)
        ]

    # 按tweet_id升序排序并返回结果
    result = invalid[['tweet_id']].sort_values('tweet_id')

    return result


if __name__ == '__main__':
    data = [[1, 'What an amazing meal @MaxPower @AlexJones @JohnDoe #Learning #Fitness #Love'],
            [2, 'Learning something new every day @AnnaWilson #Learning #Foodie'],
            [3, "Never been happier about today's achievements @SaraJohnson @JohnDoe @AnnaWilson #Fashion"], [4,
                                                                                                              'Traveling, exploring, and living my best life @JaneSmith @JohnDoe @ChrisAnderson @AlexJones #WorkLife #Travel'],
            [5, 'Work hard, play hard, and cherish every moment @AlexJones #Fashion #Foodie'],
            [6, "Never been happier about today's achievements @ChrisAnderson #Fashion #WorkLife"], [7,
                                                                                                     "So grateful for today's experiences @AnnaWilson @LisaTaylor @ChrisAnderson @MikeBrown #Fashion #HappyDay #WorkLife #Nature"],
            [8, 'What an amazing meal @EmilyClark @AlexJones @MikeBrown #Fitness'],
            [9, 'Learning something new every day @EmilyClark @AnnaWilson @MaxPower #Travel'],
            [10, "So grateful for today's experiences @ChrisAnderson #Nature"],
            [11, "So grateful for today's experiences @AlexJones #Art #WorkLife"],
            [12, 'Learning something new every day @JaneSmith @MikeBrown #Travel'],
            [13, 'What an amazing meal @EmilyClark @JohnDoe @LisaTaylor @MaxPower #Foodie #Fitness'], [14,
                                                                                                       'Work hard, play hard, and cherish every moment @LisaTaylor @SaraJohnson @MaxPower @ChrisAnderson #TechLife #Nature #Music'],
            [15, 'What a beautiful day it is @EmilyClark @MaxPower @SaraJohnson #Fashion'],
            [16, 'What a beautiful day it is @AnnaWilson @JaneSmith #Fashion #Love #TechLife']]
    tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})
    print(find_invalid_tweets(tweets))