#  [院系无效的学生](https://leetcode.cn/problems/students-with-invalid-departments)

院系表: Departments
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
```
在 SQL 中，id 是该表的主键

该表包含一所大学每个院系的 id 信息
 

学生表: Students
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| department_id | int     |
+---------------+---------+
```
在 SQL 中，id 是该表的主键

该表包含一所大学每个学生的 id 和他/她就读的院系信息
 

找出那些所在院系不存在的学生的 id 和姓名

可以以 任何顺序 返回结果。

下面是返回结果格式的例子。

 

示例 1：

> 输入：
> 
> Departments 表:
> 
> ```
> +------+--------------------------+
> | id   | name                     |
> +------+--------------------------+
> | 1    | Electrical Engineering   |
> | 7    | Computer Engineering     |
> | 13   | Bussiness Administration |
> +------+--------------------------+
> ```
> Students 表:
> ```
> +------+----------+---------------+
> | id   | name     | department_id |
> +------+----------+---------------+
> | 23   | Alice    | 1             |
> | 1    | Bob      | 7             |
> | 5    | Jennifer | 13            |
> | 2    | John     | 14            |
> | 4    | Jasmine  | 77            |
> | 3    | Steve    | 74            |
> | 6    | Luis     | 1             |
> | 8    | Jonathan | 7             |
> | 7    | Daiana   | 33            |
> | 11   | Madelynn | 1             |
> +------+----------+---------------+
> ```
> 输出：
> ```
> +------+----------+
> | id   | name     |
> +------+----------+
> | 2    | John     |
> | 7    | Daiana   |
> | 4    | Jasmine  |
> | 3    | Steve    |
> +------+----------+
> ```
> 解释：
> 
> John, Daiana, Steve 和 Jasmine 所在的院系分别是 14, 33, 74 和 77， 其中 14, 33, 74 和 77 并不存在于院系表