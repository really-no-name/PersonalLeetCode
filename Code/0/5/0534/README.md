#  [游戏玩法分析 III](https://leetcode.cn/problems/game-play-analysis-iii)

表：Activity
> ```
> +--------------+---------+
> | Column Name  | Type    |
> +--------------+---------+
> | player_id    | int     |
> | device_id    | int     |
> | event_date   | date    |
> | games_played | int     |
> +--------------+---------+
> ```
> （player_id，event_date）是此表的主键（具有唯一值的列）。
> 
> 这张表显示了某些游戏的玩家的活动情况。
> 
> 每一行是一个玩家的记录，他在某一天使用某个设备注销之前登录并玩了很多游戏（可能是 0 ）。
 

编写一个解决方案，同时报告每组玩家和日期，以及玩家到 目前为止 玩了多少游戏。也就是说，玩家在该日期之前所玩的游戏总数。详细情况请查看示例。

以 任意顺序 返回结果表。

结果格式如下所示。

 

示例 1：

> 输入：
> 
> Activity table:
> ```
> +-----------+-----------+------------+--------------+
> | player_id | device_id | event_date | games_played |
> +-----------+-----------+------------+--------------+
> | 1         | 2         | 2016-03-01 | 5            |
> | 1         | 2         | 2016-05-02 | 6            |
> | 1         | 3         | 2017-06-25 | 1            |
> | 3         | 1         | 2016-03-02 | 0            |
> | 3         | 4         | 2018-07-03 | 5            |
> +-----------+-----------+------------+--------------+
> ```
> 输出：
> ```
> +-----------+------------+---------------------+
> | player_id | event_date | games_played_so_far |
> +-----------+------------+---------------------+
> | 1         | 2016-03-01 | 5                   |
> | 1         | 2016-05-02 | 11                  |
> | 1         | 2017-06-25 | 12                  |
> | 3         | 2016-03-02 | 0                   |
> | 3         | 2018-07-03 | 5                   |
> +-----------+------------+---------------------+
> ```
> 解释：
> - 对于 ID 为 1 的玩家，2016-05-02 共玩了 5+6=11 个游戏，2017-06-25 共玩了 5+6+1=12 个游戏。
> - 对于 ID 为 3 的玩家，2018-07-03 共玩了 0+5=5 个游戏。
> - 请注意，对于每个玩家，我们只关心玩家的登录日期。