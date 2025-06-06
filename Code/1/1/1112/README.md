#  [每位学生的最高成绩](https://leetcode.cn/problems/highest-grade-for-each-student)

表：Enrollments
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | student_id    | int     |
> | course_id     | int     |
> | grade         | int     |
> +---------------+---------+
> ```
> (student_id, course_id) 是该表的主键（具有唯一值的列的组合）。
> 
> grade 不会为 NULL。
 

编写解决方案，找出每位学生获得的最高成绩和它所对应的科目，
若科目成绩并列，取 course_id 最小的一门。查询结果需按 student_id 增序进行排序。

查询结果格式如下所示。

 

示例 1：

> 输入：
> 
> Enrollments 表：
> ```
> +------------+-------------------+
> | student_id | course_id | grade |
> +------------+-----------+-------+
> | 2          | 2         | 95    |
> | 2          | 3         | 95    |
> | 1          | 1         | 90    |
> | 1          | 2         | 99    |
> | 3          | 1         | 80    |
> | 3          | 2         | 75    |
> | 3          | 3         | 82    |
> +------------+-----------+-------+
> ```
> 输出：
> ```
> +------------+-------------------+
> | student_id | course_id | grade |
> +------------+-----------+-------+
> | 1          | 2         | 99    |
> | 2          | 2         | 95    |
> | 3          | 3         | 82    |
> +------------+-----------+-------+
> ```