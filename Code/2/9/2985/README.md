#  [计算订单平均商品数量](https://leetcode.cn/problems/calculate-compressed-mean)

表： Orders
```
+-------------------+------+
| Column Name       | Type |
+-------------------+------+
| order_id          | int  |
| item_count        | int  |
| order_occurrences | int  |
+-------------------+------+
```
order_id 是这张表具有唯一值的列。

这张表包括 order_id, item_count,和 order_occurrences。

编写一个计算每个订单的 平均 商品数量的解决方案，保留 2 位小数。

以 任意 顺序返回结果表。

结果格式如下例所示。

 

示例 1:

输入：
Orders table:
```
+----------+------------+-------------------+
| order_id | item_count | order_occurrences | 
+----------+------------+-------------------+
| 10       | 1          | 500               | 
| 11       | 2          | 1000              |     
| 12       | 3          | 800               |  
| 13       | 4          | 1000              | 
+----------+------------+-------------------+
```
输出
```
+-------------------------+
| average_items_per_order | 
+-------------------------+
| 2.70                    |
+-------------------------+
```
解释

计算如下：
 - 总商品数：(1 * 500) + (2 * 1000) + (3 * 800) + (4 * 1000) = 8900 
 - 总订单数：500 + 1000 + 800 + 1000 = 3300 
 - 因此，每个订单的平均商品数量为 8900 / 3300 = 2.70