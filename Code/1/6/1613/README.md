#  [找到遗失的ID](https://leetcode.cn/problems/find-the-missing-ids)

表: Customers
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | customer_id   | int     |
> | customer_name | varchar |
> +---------------+---------+
> ```
> customer_id 是该表主键.
> 
> 该表第一行包含了顾客的名字和 id.
 

编写一个解决方案, 找到所有遗失的顾客 id。遗失的顾客 id 是指那些不在 Customers 表中, 值却处于 1 和表中 最大 customer_id 之间的 id.

注意: 最大的 customer_id 值不会超过 100.

返回结果按 ids 升序 排列

查询结果格式如下例所示。

 

示例 1:

> 输入：
> 
> Customers 表:
> ```
> +-------------+---------------+
> | customer_id | customer_name |
> +-------------+---------------+
> | 1           | Alice         |
> | 4           | Bob           |
> | 5           | Charlie       |
> +-------------+---------------+
> ```
> 输出：
> ```
> +-----+
> | ids |
> +-----+
> | 2   |
> | 3   |
> +-----+
> ```
> 解释：
> 
> 表中最大的 customer_id 是 5, 所以在范围 [1,5] 内, ID2 和 3 从表中遗失.