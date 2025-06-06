#  [评分为 NULL 的图书](https://leetcode.cn/problems/books-with-null-ratings)

表：books
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| title          | varchar |
| author         | varchar |
| published_year | int     |
| rating         | decimal |
+----------------+---------+
```
book_id 是这张表的唯一主键。

这张表的每一行包含关于一本书的唯一 ID，题目，作者，出版年份以及评分的信息。

评分可能为 NULL，表示这本书还没有被评分。

编写一个解决方案来找到所有还没有被评分的图书。（即评分为 NULL）

返回结果表以 book_id 升序 排序。

结果格式如下所示。

 

示例：

> 输入：
> 
> books 表：
> 
> ```+---------+------------------------+------------------+----------------+--------+
> | book_id | title                  | author           | published_year | rating |
> +---------+------------------------+------------------+----------------+--------+
> | 1       | The Great Gatsby       | F. Scott         | 1925           | 4.5    |
> | 2       | To Kill a Mockingbird  | Harper Lee       | 1960           | NULL   |
> | 3       | Pride and Prejudice    | Jane Austen      | 1813           | 4.8    |
> | 4       | The Catcher in the Rye | J.D. Salinger    | 1951           | NULL   |
> | 5       | Animal Farm            | George Orwell    | 1945           | 4.2    |
> | 6       | Lord of the Flies      | William Golding  | 1954           | NULL   |
> +---------+------------------------+------------------+----------------+--------+
> ```
> 输出：
> 
> ```
> +---------+------------------------+------------------+----------------+
> | book_id | title                  | author           | published_year |
> +---------+------------------------+------------------+----------------+
> | 2       | To Kill a Mockingbird  | Harper Lee       | 1960           |
> | 4       | The Catcher in the Rye | J.D. Salinger    | 1951           |
> | 6       | Lord of the Flies      | William Golding  | 1954           |
> +---------+------------------------+------------------+----------------+
> ```
> 解释：
> 
> - book_id 为 2，4，6 的书评分为 NULL。
> - 这些书被包含在结果表中。
> - 其它书（book_id 为 1，3，5）有评分并且没有被包含。
> - 结果以 book_id 升序排序。