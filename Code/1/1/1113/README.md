#  [报告的记录](https://leetcode.cn/problems/reported-posts)

动作表：Actions
> ```
> +---------------+---------+
> | Column Name   | Type    |
> +---------------+---------+
> | user_id       | int     |
> | post_id       | int     |
> | action_date   | date    | 
> | action        | enum    |
> | extra         | varchar |
> +---------------+---------+
> ```
> 此表可能会有重复的行。
> 
> action 字段是 ENUM 类型的，包含:('view', 'like', 'reaction', 'comment', 'report', 'share')
> 
> extra 包含关于 action 的可选信息，例如举报的原因或反馈的类型。
> 
> 当 action 为 'report' 时 extra 不会为 NULL。
 

编写解决方案，针对每个举报原因统计昨天的举报帖子数量。假设今天是 2019-07-05 。

返回结果表 无顺序要求 。

结果格式如下示例所示。

 

示例 1：

> 输入：
> 
> Actions table:
> ```
> +---------+---------+-------------+--------+--------+
> | user_id | post_id | action_date | action | extra  |
> +---------+---------+-------------+--------+--------+
> | 1       | 1       | 2019-07-01  | view   | null   |
> | 1       | 1       | 2019-07-01  | like   | null   |
> | 1       | 1       | 2019-07-01  | share  | null   |
> | 2       | 4       | 2019-07-04  | view   | null   |
> | 2       | 4       | 2019-07-04  | report | spam   |
> | 3       | 4       | 2019-07-04  | view   | null   |
> | 3       | 4       | 2019-07-04  | report | spam   |
> | 4       | 3       | 2019-07-02  | view   | null   |
> | 4       | 3       | 2019-07-02  | report | spam   |
> | 5       | 2       | 2019-07-04  | view   | null   |
> | 5       | 2       | 2019-07-04  | report | racism |
> | 5       | 5       | 2019-07-04  | view   | null   |
> | 5       | 5       | 2019-07-04  | report | racism |
> +---------+---------+-------------+--------+--------+
> ```
> 输出：
> ```
> +---------------+--------------+
> | report_reason | report_count |
> +---------------+--------------+
> | spam          | 1            |
> | racism        | 2            |
> +---------------+--------------+ 
> ```
> 解释：注意，我们只关心举报帖数量非零的举报原因。