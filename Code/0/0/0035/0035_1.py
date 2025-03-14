## 0 ms, 18.17 ms
# 时间复杂度 O（N）
# 空间复杂度 O（1）

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            for i in range(len(nums)):
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))