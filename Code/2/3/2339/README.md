#  [联赛的所有比赛](https://leetcode.cn/problems/all-the-matches-of-the-league)

表: Teams
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | team_name   | varchar |
> +-------------+---------+
> ```
> team_name 是该表中具有唯一值的列。
> 
> 此表的每一行都显示了团队的名称。
 

编写解决方案，获取联赛中所有比赛。每两支球队进行两场比赛，其中一支球队是主队 home_team ，另一支是客场队 away_team。

按 任意顺序 返回结果表。

返回结果格式如下例所示。

 

示例 1:

> 输入: 
> Teams 表:
> ```
> +-------------+
> | team_name   |
> +-------------+
> | Leetcode FC |
> | Ahly SC     |
> | Real Madrid |
> +-------------+
> ```
> 输出: 
> ```
> +-------------+-------------+
> | home_team   | away_team   |
> +-------------+-------------+
> | Real Madrid | Leetcode FC |
> | Real Madrid | Ahly SC     |
> | Leetcode FC | Real Madrid |
> | Leetcode FC | Ahly SC     |
> | Ahly SC     | Real Madrid |
> | Ahly SC     | Leetcode FC |
> +-------------+-------------+
> ```
> 解释: 该联赛的所有比赛都列在表格中。