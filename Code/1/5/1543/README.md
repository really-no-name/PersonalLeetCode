# [产品名称格式修复](https://leetcode.cn/problems/fix-product-name-format)

表：`Sales`
> ```
> +--------------+---------+
> | Column Name  | Type    |
> +--------------+---------+
> | sale_id      | int     |
> | product_name | varchar |
> | sale_date    | date    |
> +--------------+---------+
> ```
> sale_id 是该表具有唯一值的列
> 
> 该表的每一行包含了产品的名称及其销售日期 
> 
> 因为在 2000 年该表是手工填写的，product_name 可能包含前后空格，而且包含大小写。

编写一个解决方案报告每个月的销售情况：

product_name 是小写字母且不包含前后空格

sale_date 格式为 ('YYYY-MM') 

total 是产品在本月销售的次数

返回结果以 product_name 升序 排列，如果有排名相同，再以 sale_date 升序 排列。

查询结果格式如下所示。

 

示例 1：

> 输入：
> 
> Sales 表：
> ```
> +---------+--------------+------------+
> | sale_id | product_name | sale_date  |
> +---------+--------------+------------+
> | 1       | LCPHONE      | 2000-01-16 |
> | 2       | LCPhone      | 2000-01-17 |
> | 3       | LcPhOnE      | 2000-02-18 |
> | 4       | LCKeyCHAiN   | 2000-02-19 |
> | 5       | LCKeyChain   | 2000-02-28 |
> | 6       | Matryoshka   | 2000-03-31 |
> +---------+--------------+------------+
> ```
> 输出：
> ```
> +--------------+-----------+-------+
> | product_name | sale_date | total |
> +--------------+-----------+-------+
> | lckeychain   | 2000-02   | 2     |
> | lcphone      | 2000-01   | 2     |
> | lcphone      | 2000-02   | 1     |
> | matryoshka   | 2000-03   | 1     |
> +--------------+-----------+-------+
> ```
> 解释：
> - 一月份售出 2 部 LcPhones。请注意，产品名称不区分大小写，且可能包含空格。 
> - 二月份售出 2 个 LCKeychains 和 1 部 LCPhone。 
> - 三月份售出 1 个 Matryoshka。