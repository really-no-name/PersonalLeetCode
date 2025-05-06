#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3475.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: DNA 模式识别。
"""
import pandas as pd


def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].str.contains(r'^ATG').astype(int)
    samples['has_stop'] = samples['dna_sequence'].str.contains(r'(TAA|TAG|TGA)$').astype(int)
    samples['has_atat'] = samples['dna_sequence'].str.contains(r'ATAT').astype(int)
    samples['has_ggg'] = samples['dna_sequence'].str.contains(r'G{3,}').astype(int)
    return samples


if __name__ == '__main__':
    data = [[1, 'ATGCTAGCTAGCTAA', 'Human'],
            [2, 'GGGTCAATCATC', 'Human'],
            [3, 'ATATATCGTAGCTA', 'Human'],
            [4, 'ATGGGGTCATCATAA', 'Mouse'],
            [5, 'TCAGTCAGTCAG', 'Mouse'],
            [6, 'ATATCGCGCTAG', 'Zebrafish'],
            [7, 'CGTATGCGTCGTA', 'Zebrafish']]
    samples = pd.DataFrame(data, columns=['sample_id', 'dna_sequence', 'species']).astype(
        {'sample_id': int, 'dna_sequence': str, 'species': str})
    print(analyze_dna_patterns(samples))