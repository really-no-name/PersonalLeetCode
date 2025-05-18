#  [贷款类型](https://leetcode.cn/problems/loan-types)

表： `Loans`
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | loan_id     | int     |
> | user_id     | int     |
> | loan_type   | varchar |
> +-------------+---------+
> ```
> loan_id 是这张表具有唯一值的列。
> 
> 该表包含 loan_id, user_id,和 loan_type。

编写一个解决方案，找出所有具有同时具有 Refinance 贷款类型和 Mortgage 贷款类型的 user_id（需去重）。

按 升序 返回结果表中的 user_id。

返回结果表格式如下例所示。

 

示例 1:

> 输入：
> 
> `Loans table`:
> ``
> +---------+---------+-----------+
> | loan_id | user_id | loan_type |
> +---------+---------+-----------+
> | 683     | 101     | Mortgage  |
> | 218     | 101     | AutoLoan  |
> | 802     | 101     | Inschool  |
> | 593     | 102     | Mortgage  |
> | 138     | 102     | Refinance |
> | 294     | 102     | Inschool  |
> | 308     | 103     | Refinance |
> | 389     | 104     | Mortgage  |
> +---------+---------+-----------+
> ``
> 输出
> ```
> +---------+
> | user_id | 
> +---------+
> | 102     | 
> +---------+
> ```
> 解释
> - User_id 101 有三种贷款类型，其中之一是 Mortgage。但是，此用户没有任何类别为 Refinance 的贷款类型，因此用户 101 不会被考虑。
> - User_id 102 拥有三种贷款类型：一种是 Mortgage，一种是 Refinance。因此，用户 102 将包括在结果中。
> - User_id 103 有一种 Refinance 贷款类型，但没有 Mortgage 贷款类型，因此用户 103 不会被考虑。
> - User_id 104 有一种 Mortgage 贷款类型，但没有 Refinance 贷款类型，因此用户 104 不会被考虑。
> 输出表以升序按 user_id 排序。