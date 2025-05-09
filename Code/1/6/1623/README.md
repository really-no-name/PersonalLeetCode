# [三人国家代表队](https://leetcode.cn/problems/all-valid-triplets-that-can-represent-a-country)

表: SchoolA
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | student_id    | int     |
> | student_name  | varchar |
> +---------------+---------+
> ```
> student_id 是该表具有唯一值的列
> 
> 表中的每一行包含了学校 A 中每一个学生的名字和 ID
> 
> 所有 student_name 在表中都是独一无二的
 

表: SchoolB
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | student_id    | int     |
> | student_name  | varchar |
> +---------------+---------+
> ```
> student_id 是该表具有唯一值的列
> 
> 表中的每一行包含了学校 B 中每一个学生的名字和 ID
> 
> 所有 student_name 在表中都是独一无二的
 

表: SchoolC
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | student_id    | int     |
> | student_name  | varchar |
> +---------------+---------+
> ```
> student_id 是该表具有唯一值的列
> 
> 表中的每一行包含了学校 C 中每一个学生的名字和 ID

所有 student_name 在表中都是独一无二的
 

有一个国家只有三所学校，这个国家的每一个学生只会注册 一所学校。

这个国家正在参加一个竞赛，他们希望从这三所学校中各选出一个学生来组建一支三人的代表队。例如：

member_A 是从 SchoolA 中选出的

member_B 是从 SchoolB 中选出的

member_C 是从 SchoolC 中选出的

被选中的学生具有不同的名字和 ID（没有任何两个学生拥有相同的名字、没有任何两个学生拥有相同的 ID）

使用上述条件，编写一个解决方案来找到所有可能的三人国家代表队组合。

返回结果 无顺序要求。

结果格式如下示例所示。

 

示例 1:

> 输入：
> 
> SchoolA table:
> ```
> +------------+--------------+
> | student_id | student_name |
> +------------+--------------+
> | 1          | Alice        |
> | 2          | Bob          |
> +------------+--------------+
> ```
> SchoolB table:
> ```
> +------------+--------------+
> | student_id | student_name |
> +------------+--------------+
> | 3          | Tom          |
> +------------+--------------+
> ```
> SchoolC table:
> ```
> +------------+--------------+
> | student_id | student_name |
> +------------+--------------+
> | 3          | Tom          |
> | 2          | Jerry        |
> | 10         | Alice        |
> +------------+--------------+
> ```
> 输出：
> ```
> +----------+----------+----------+
> | member_A | member_B | member_C |
> +----------+----------+----------+
> | Alice    | Tom      | Jerry    |
> | Bob      | Tom      | Alice    |
> +----------+----------+----------+
> ```
> 解释：
> 
> 让我们看看有哪些可能的组合：
> - (Alice, Tom, Tom) --> 不适用，因为member_B（Tom）和member_C（Tom）有相同的名字和ID
> - (Alice, Tom, Jerry) --> 可能的组合
> - (Alice, Tom, Alice) --> 不适用，因为member_A和member_C有相同的名字
> - (Bob, Tom, Tom) --> 不适用，因为member_B和member_C有相同的名字和ID
> - (Bob, Tom, Jerry) --> 不适用，因为member_A和member_C有相同的ID
> - (Bob, Tom, Alice) --> 可能的组合.