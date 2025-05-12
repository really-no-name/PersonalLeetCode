#  [查找每个州的城市]()

表：cities
> ```
> +-------------+---------+
> | Column Name | Type    | 
> +-------------+---------+
> | state       | varchar |
> | city        | varchar |
> +-------------+---------+
> ```
> (state, city) 是这张表的主键（有不同值的列的组合）。
> 
> 这张表的每一行包含州名和其中的城市名。

编写一个解决方案来 查找每个州的所有城市，并将它们组合成 一个逗号分隔 的字符串。

返回结果表以 state 升序 排序。

结果格式如下所示。

 

示例：

> 输入：
> 
> cities 表：
> ```
> +-------------+---------------+
> | state       | city          |
> +-------------+---------------+
> | California  | Los Angeles   |
> | California  | San Francisco |
> | California  | San Diego     |
> | Texas       | Houston       |
> | Texas       | Austin        |
> | Texas       | Dallas        |
> | New York    | New York City |
> | New York    | Buffalo       |
> | New York    | Rochester     |
> +-------------+---------------+
> ```
> 输出：
> ```
> +-------------+---------------------------------------+
> | state       | cities                                |
> +-------------+---------------------------------------+
> | California  | Los Angeles, San Diego, San Francisco |
> | New York    | Buffalo, New York City, Rochester     |
> | Texas       | Austin, Dallas, Houston               |
> +-------------+---------------------------------------+
> ```
> 解释：
> 
> - California：所有城市 ("Los Angeles", "San Diego", "San Francisco") 以逗号分隔的字符串列出。
> - New York：所有城市 ("Buffalo", "New York City", "Rochester") 以逗号分隔的字符串列出。
> - Texas：所有城市 ("Austin", "Dallas", "Houston") 以逗号分隔的字符串列出。
> - 注意：输出表以州名升序排序。