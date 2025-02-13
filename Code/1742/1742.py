#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 盒子中小球的最大数量 —— 暴力枚举。
时间复杂度：O(N*M)
空间复杂度：O(M)
执行用时：343 ms
消耗内存：17.47 mb
"""


class Solution:
    def digit_sum(self, n: int) -> int:
        # 将整数转换为字符串，以便逐个访问每个数字
        num_str = str(n)

        # 初始化总和为0
        total = 0

        # 遍历字符串中的每个字符
        for char in num_str:
            # 将字符转换回整数并加到总和中
            total += int(char)

        # 返回数位和
        return total

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = [0] * 50
        for i in range(lowLimit, highLimit + 1):
            # print("第", i, "个球，放在盒子：", self.digit_sum(i))
            ans[self.digit_sum(i) - 1] += 1

        # print(ans)
        return max(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.countBalls(lowLimit=1, highLimit=10))
