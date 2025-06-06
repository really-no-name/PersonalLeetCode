#  [每日新用户统计](https://leetcode.cn/problems/new-users-daily-count)

Traffic 表：
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | user_id       | int     |
> | activity      | enum    |
> | activity_date | date    |
> +---------------+---------+
> ```
> 该表可能有重复的行。
> 
> activity 列是 ENUM 类型，可能取 ('login', 'logout', 'jobs', 'groups', 'homepage') 几个值之一。

 

编写解决方案，找出从今天起最多 90 天内，每个日期该日期首次登录的用户数。假设今天是 2019-06-30 。

以 任意顺序 返回结果表。

结果格式如下所示。

 

 

示例 1：

> 输入：
> 
> Traffic 表：
> ```
> +---------+----------+---------------+
> | user_id | activity | activity_date |
> +---------+----------+---------------+
> | 1       | login    | 2019-05-01    |
> | 1       | homepage | 2019-05-01    |
> | 1       | logout   | 2019-05-01    |
> | 2       | login    | 2019-06-21    |
> | 2       | logout   | 2019-06-21    |
> | 3       | login    | 2019-01-01    |
> | 3       | jobs     | 2019-01-01    |
> | 3       | logout   | 2019-01-01    |
> | 4       | login    | 2019-06-21    |
> | 4       | groups   | 2019-06-21    |
> | 4       | logout   | 2019-06-21    |
> | 5       | login    | 2019-03-01    |
> | 5       | logout   | 2019-03-01    |
> | 5       | login    | 2019-06-21    |
> | 5       | logout   | 2019-06-21    |
> +---------+----------+---------------+
> ```
> 输出：
> ```
> +------------+-------------+
> | login_date | user_count  |
> +------------+-------------+
> | 2019-05-01 | 1           |
> | 2019-06-21 | 2           |
> +------------+-------------+
> ```
> 解释：
> - 请注意，我们只关心用户数非零的日期.
> - ID 为 5 的用户第一次登陆于 2019-03-01，因此他不算在 2019-06-21 的的统计内。