#  [按性别排列表格](https://leetcode.cn/problems/arrange-table-by-gender)

表: Genders
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | user_id     | int     |
> | gender      | varchar |
> +-------------+---------+
> ```
> - user_id 是该表的主键(具有唯一值的列)。
> - gender 的值是 'female', 'male','other' 之一。
> - 该表中的每一行都包含用户的 ID 及其性别。
> - 表格中 'female', 'male','other' 数量相等。
 

编写一个解决方案以重新排列 Genders 表，使行按顺序在 'female', 'other' 和 'male' 之间交替。同时每种性别按照 user_id 升序进行排序。

按 上述顺序 返回结果表。

返回结果格式如以下示例所示。

 

示例 1:

> 输入: 
> 
> Genders 表:
> ```
> +---------+--------+
> | user_id | gender |
> +---------+--------+
> | 4       | male   |
> | 7       | female |
> | 2       | other  |
> | 5       | male   |
> | 3       | female |
> | 8       | male   |
> | 6       | other  |
> | 1       | other  |
> | 9       | female |
> +---------+--------+
> ```
> 输出: 
> ```
> +---------+--------+
> | user_id | gender |
> +---------+--------+
> | 3       | female |
> | 1       | other  |
> | 4       | male   |
> | 7       | female |
> | 2       | other  |
> | 5       | male   |
> | 9       | female |
> | 6       | other  |
> | 8       | male   |
> +---------+--------+
> ```
> 解释: 
> 
> - 女性：ID 3、7、9。
> - 其他性别：ID 1、2、6。
> - 男性：ID 4、5、8。
> - 我们在 'female', 'other','male' 之间交替排列表。
> - 注意，每种性别都是按 user_id 升序排序的。