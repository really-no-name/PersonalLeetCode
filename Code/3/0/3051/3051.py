#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3051.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 寻找数据科学家职位的候选人。
"""
import pandas as pd


def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    # 过滤出所需的技能
    required_skills = {'Python', 'Tableau', 'PostgreSQL'}
    filtered_df = candidates[candidates['skill'].isin(required_skills)]
    print(filtered_df)

    # 统计每个候选人拥有的技能数量
    skill_counts = filtered_df.groupby('candidate_id')['skill'].nunique().reset_index()
    print(skill_counts)

    # 筛选出拥有全部三个技能的候选人
    qualified_candidates = skill_counts[skill_counts['skill'] == len(required_skills)]
    print(qualified_candidates)

    # 按 candidate_id 升序排序
    qualified_candidates = qualified_candidates.sort_values(by='candidate_id')
    print(qualified_candidates)

    # 输出结果
    result = qualified_candidates[['candidate_id']]
    return result


if __name__ == '__main__':
    data = {
        'candidate_id': [123, 234, 123, 123, 234, 234, 147, 147, 147, 147, 256, 102],
        'skill': ['Python', 'R', 'Tableau', 'PostgreSQL', 'PowerBI', 'SQL Server', 'Python', 'Tableau', 'Java',
                  'PostgreSQL', 'Tableau', 'DataAnalysis']
    }
    df = pd.DataFrame(data)
    print(find_candidates(df))