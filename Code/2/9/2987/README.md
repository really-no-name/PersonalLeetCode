#  [寻找房价最贵的城市](https://leetcode.cn/problems/find-expensive-cities)

表： Listings
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | listing_id  | int     |
> | city        | varchar |
> | price       | int     |
> +-------------+---------+
> ```
> listing_id 是这张表具有唯一值的列。
> 
> 这张表包括 listing_id, city,和 price。

编写一个解决方案，查找 房价平均值 超过 全国 平均房价的 城市。

返回 按 city 升序 排序的结果表。

结果格式如下例所示。

 

示例 1:

> 输入：
> 
> Listings table:
> ```
> +------------+--------------+---------+
> | listing_id | city         | price   | 
> +------------+--------------+---------+
> | 113        | LosAngeles   | 7560386 | 
> | 136        | SanFrancisco | 2380268 |     
> | 92         | Chicago      | 9833209 | 
> | 60         | Chicago      | 5147582 | 
> | 8          | Chicago      | 5274441 |  
> | 79         | SanFrancisco | 8372065 | 
> | 37         | Chicago      | 7939595 | 
> | 53         | LosAngeles   | 4965123 | 
> | 178        | SanFrancisco | 999207  | 
> | 51         | NewYork      | 5951718 | 
> | 121        | NewYork      | 2893760 | 
> +------------+--------------+---------+
> ```
> 输出
> ```
> +------------+
> | city       | 
> +------------+
> | Chicago    | 
> | LosAngeles |  
> +------------+
> ```
> 解释
> 
> 全国平均房价为 $6,122,059.45。在列出的城市中：
> - Chicago 的平均价格为 $7,048,706.75
> - Los Angeles 的平均价格为 $6,277,754.5
> - San Francisco 的平均价格为 $3,900,513.33
> - New York 的平均价格为 $4,422,739
> 
> 只有 Chicago 和 Los Angeles 的平均房价超过了全国平均水平。因此，这两个城市包含在输出表中。输出表按城市名称升序排序。