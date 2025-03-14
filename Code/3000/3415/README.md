#  [查找具有三个连续数字的产品](https://leetcode.cn/problems/find-products-with-three-consecutive-digits)

表：Products
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| name        | varchar |
+-------------+---------+
```
product_id 是这张表的唯一主键。

这张表的每一行包含产品的 ID 和名字。

编写一个解决方案来找到所有名字中包含 三位连续数字 且无连续三位以上数字的所有 产品。

返回结果表以 product_id 升序 排序。

结果格式如下所示。

 

示例：

输入：

products 表：
```
+-------------+--------------------+
| product_id  | name               |
+-------------+--------------------+
| 1           | ABC123XYZ          |
| 2           | A12B34C            |
| 3           | Product56789       |
| 4           | NoDigitsHere       |
| 5           | 789Product         |
| 6           | Item003Description |
| 7           | Product12X34       |
+-------------+--------------------+
```
输出：
```
+-------------+--------------------+
| product_id  | name               |
+-------------+--------------------+
| 1           | ABC123XYZ          |
| 5           | 789Product         |
| 6           | Item003Description |
+-------------+--------------------+
```
解释：

产品 1：ABC123XYZ 包含数字 123。

产品 5：789Product 包含数字 789。

产品 6：Item003Description 包含数字 003，恰好是三个数字。

注意：

- 结果以 product_id 升序排序。
- 只有名称中恰好具有三个连续数字的产品才会包含在结果中。