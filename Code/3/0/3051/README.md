#  [寻找数据科学家职位的候选人](https://leetcode.cn/problems/find-candidates-for-data-scientist-position)

表：Candidates
```
+--------------+---------+ 
| Column Name  | Type    | 
+--------------+---------+ 
| candidate_id | int     | 
| skill        | varchar |
+--------------+---------+
```
(candidate_id, skill) 是这张表的主键（有不同值的列）。

每一行包括 candidate_id 和 skill。

编写一个查询来找到最适合数据科学家职位的 候选人。应聘者必须精通 Python，Tableau 和 PostgreSQL。

返回结果表，以 candidate_id 升序 排序。

结果格式如下所示。

 

示例 1：

输入： 

Candidates 表：
```
+---------------+--------------+
| candidate_id  | skill        | 
+---------------+--------------+
| 123           | Python       |
| 234           | R            | 
| 123           | Tableau      | 
| 123           | PostgreSQL   | 
| 234           | PowerBI      | 
| 234           | SQL Server   | 
| 147           | Python       | 
| 147           | Tableau      | 
| 147           | Java         |
| 147           | PostgreSQL   |
| 256           | Tableau      |
| 102           | DataAnalysis |
+---------------+--------------+
```
输出： 
```
+--------------+
| candidate_id |  
+--------------+
| 123          |  
| 147          | 
+--------------+
```
解释： 
- 候选人 123 和 147 具备数据科学家职位必要的 Python，Tableau 和 PostgreSQL 技能。
- 候选人 234 和 102 不具备该职位所需的任何技能。
- 候选人 256 精通 Tableau 但没有掌握 Python 和 PostgreSQL。

输出表以 candidate_id 升序排序。