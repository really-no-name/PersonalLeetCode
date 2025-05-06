#  [无效的推文 II]()

表：Tweets
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
```
tweet_id 是这个表的主键（有不同值的列）。

这个表包含某社交媒体 App 中所有的推文。

编写一个解决方案来找到 无效的推文。如果一条推文满足下面 任一 条件会被认为无效：

长度超过 140 个字符。

有超过 3 次提及。

有超过 3 个标签。

以 tweet_id 升序 返回结果表。

查询结果格式如下所示：

 

示例：

> 输入：
> 
> Tweets 表：
> ```
>   +----------+-----------------------------------------------------------------------------------+
>   | tweet_id | content                                                                           |
>   +----------+-----------------------------------------------------------------------------------+
>   | 1        | Traveling, exploring, and living my best life @JaneSmith @SaraJohnson @LisaTaylor |
>   |          | @MikeBrown #Foodie #Fitness #Learning                                             | 
>   | 2        | Just had the best dinner with friends! #Foodie #Friends #Fun                      |
>   | 4        | Working hard on my new project #Work #Goals #Productivity #Fun                    |
>   +----------+-----------------------------------------------------------------------------------+
>   ```
> 输出：
> ```
>   +----------+
>   | tweet_id |
>   +----------+
>   | 1        |
>   | 4        |
>   +----------+
>   ```
> 解释：
> 
> - tweet_id 1 包含 4 次提及。
> - tweet_id 4 包含 4 个标签。
> - 输出表以 tweet_id 升序排序。