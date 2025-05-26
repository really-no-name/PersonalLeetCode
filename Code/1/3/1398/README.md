#  [购买了产品 A 和产品 B 却没有购买产品 C 的顾客](https://leetcode.cn/problems/customers-who-bought-products-a-and-b-but-not-c)

Customers 表：
> ```
> +---------------------+---------+
> | Column Name         | Type    |
> +---------------------+---------+
> | customer_id         | int     |
> | customer_name       | varchar |
> +---------------------+---------+
> ```
> customer_id 是这张表中具有唯一值的列。
> 
> customer_name 是顾客的名称。
 

Orders 表：
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | order_id      | int     |
> | customer_id   | int     |
> | product_name  | varchar |
> +---------------+---------+
> ```
> order_id 是这张表中具有唯一值的列。
> 
> customer_id 是购买了名为 "product_name" 产品顾客的id。
 

请你编写解决方案，报告购买了产品 "A"，"B" 但没有购买产品 "C" 的客户的 customer_id 和 customer_name，因为我们想推荐他们购买这样的产品。

返回按 customer_id 排序 的结果表。

返回结果格式如下所示。

 

示例 1：

> 输入：
> 
> Customers table:
> ```
> +-------------+---------------+
> | customer_id | customer_name |
> +-------------+---------------+
> | 1           | Daniel        |
> | 2           | Diana         |
> | 3           | Elizabeth     |
> | 4           | Jhon          |
> +-------------+---------------+
> ```
> Orders table:
> ```
> +------------+--------------+---------------+
> | order_id   | customer_id  | product_name  |
> +------------+--------------+---------------+
> | 10         |     1        |     A         |
> | 20         |     1        |     B         |
> | 30         |     1        |     D         |
> | 40         |     1        |     C         |
> | 50         |     2        |     A         |
> | 60         |     3        |     A         |
> | 70         |     3        |     B         |
> | 80         |     3        |     D         |
> | 90         |     4        |     C         |
> +------------+--------------+---------------+
> ```
> 输出：
> ```
> +-------------+---------------+
> | customer_id | customer_name |
> +-------------+---------------+
> | 3           | Elizabeth     |
> +-------------+---------------+
> ```
> 解释：
> 
> 只有 customer_id 为 3 的顾客购买了产品 A 和产品 B ，却没有购买产品 C 。