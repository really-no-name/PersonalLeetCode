#  [乘积为偶数的子数组数](https://leetcode.cn/problems/number-of-subarrays-having-even-product)

给定一个整数数组 nums，返回具有偶数乘积的 nums 子数组的数目。

 

示例 1:

> 输入: nums = [9,6,7,13]
> 
> 输出: 6
> 
> 解释: 有6个子数组的乘积是偶数:
> 
> - nums[0..1] = 9 * 6 = 54.
> - nums[0..2] = 9 * 6 * 7 = 378.
> - nums[0..3] = 9 * 6 * 7 * 13 = 4914.
> - nums[1..1] = 6.
> - nums[1..2] = 6 * 7 = 42.
> - nums[1..3] = 6 * 7 * 13 = 546.

示例 2:

> 输入: nums = [7,3,5]
> 
> 输出: 0
> 
> 解释: 没有乘积是偶数的子数组
 

提示:

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105