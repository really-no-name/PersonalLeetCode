#  [山脉数组的峰顶索引](https://leetcode.cn/problems/peak-index-in-a-mountain-array?envType=study-plan-v2&envId=primers-list)

给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。

返回峰值元素的下标。

你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。

 

示例 1：

> 输入：arr = [0,1,0]
> 
> 输出：1

示例 2：

> 输入：arr = [0,2,1,0]
> 
> 输出：1

示例 3：

> 输入：arr = [0,10,5,2]
> 
> 输出：1
 

提示：

- 3 <= arr.length <= 105
- 0 <= arr[i] <= 106
- 题目数据 保证 arr 是一个山脉数组