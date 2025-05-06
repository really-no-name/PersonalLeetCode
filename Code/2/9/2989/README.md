#  [班级表现](https://leetcode.cn/problems/class-performance)

表： Scores
```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| student_name | varchar |
| assignment1  | int     |
| assignment2  | int     |
| assignment3  | int     |
+--------------+---------+
```
student_id 是这张表具有唯一值的列。

该表包含 student_id, student_name, assignment1, assignment2,和 assignment3。

编写一个查询，计算学生获得的 最高总分 和 最低总分 之间的 差（3 次作业的总和）。

以 任意 顺序返回结果表。

结果表的格式如下示例所示。

 

示例 1:

> 输入：
> 
> Scores 表：
> ```
> +------------+--------------+-------------+-------------+-------------+
> | student_id | student_name | assignment1 | assignment2 | assignment3 |
> +------------+--------------+-------------+-------------+-------------+
> | 309        | Owen         | 88          | 47          | 87          |
> | 321        | Claire       | 98          | 95          | 37          |     
> | 338        | Julian       | 100         | 64          | 43          |  
> | 423        | Peyton       | 60          | 44          | 47          |  
> | 896        | David        | 32          | 37          | 50          | 
> | 235        | Camila       | 31          | 53          | 69          | 
> +------------+--------------+-------------+-------------+-------------+
> ```
> 输出
> ```
> +---------------------+
> | difference_in_score | 
> +---------------------+
> | 111                 | 
> +---------------------+
> ```
> 解释
> - student_id 309 的总分为 88 + 47 + 87 = 222。
> - student_id 321 的总分为 98 + 95 + 37 = 230。
> - student_id 338 的总分为 100 + 64 + 43 = 207。
> - student_id 423 的总分为 60 + 44 + 47 = 151。
> - student_id 896 的总分为 32 + 37 + 50 = 119。
> - student_id 235 的总分为 31 + 53 + 69 = 153。
> student_id 321 拥有最高分为 230，而 student_id 896 拥有最低分为 119。因此，它们之间的差异为 111。