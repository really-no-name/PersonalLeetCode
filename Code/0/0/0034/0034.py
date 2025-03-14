# 0ms, 18.74 mb

from typing import List


class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]

        start = self.lower_bound(nums, target)
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
