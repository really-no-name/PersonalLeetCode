#  [坚定的友谊](https://leetcode.cn/problems/strong-friendship)

表名: Friendship
> ```
> +-------------+------+
> | 列名         | 类型 |
> +-------------+------+
> | user1_id    | int  |
> | user2_id    | int  |
> +-------------+------+
> ```
> (user1_id, user2_id) 是这个表的主键（具有唯一值的列的组合）。
> 
> 这张表的每一行都表示用户 user1_id 和 user2_id 是朋友。
> 
> 请注意，user1_id < user2_id。
 

如果 x  和 y 为 朋友 且他们 至少 有三个共同的朋友 ，那么 x 和 y 之间的友谊就是 坚定的。

写一个解决方案来找到所有的 坚定的友谊。

注意，结果表不应该包含重复的行，并且 user1_id < user2_id。

以 任何顺序 返回结果表。

返回结果格式如下所示。

 

示例 1:

> 输入: 
> 
> Friendship table:
> ```
> +----------+----------+
> | user1_id | user2_id |
> +----------+----------+
> | 1        | 2        |
> | 1        | 3        |
> | 2        | 3        |
> | 1        | 4        |
> | 2        | 4        |
> | 1        | 5        |
> | 2        | 5        |
> | 1        | 7        |
> | 3        | 7        |
> | 1        | 6        |
> | 3        | 6        |
> | 2        | 6        |
> +----------+----------+
> ```
> 输出: 
> ```
> +----------+----------+---------------+
> | user1_id | user2_id | common_friend |
> +----------+----------+---------------+
> | 1        | 2        | 4             |
> | 1        | 3        | 3             |
> +----------+----------+---------------+
> ```
> 解释: 
> 
> - 用户 1 和 2 有 4 个共同的朋友（3，4，5，和 6）。
> - 用户 1 和 3 有 3 个共同的朋友（2，6，和 7）。
> - 但这里不包括用户 2 和 3 的友谊，因为他们只有两个共同的朋友（1 和 6）。