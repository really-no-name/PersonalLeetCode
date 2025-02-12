## 0 ms, 17.99 ms
# 时间复杂度 O（LogN）
# 空间复杂度 O（1）

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert(nums=[1, 3, 5, 6], target=5))
