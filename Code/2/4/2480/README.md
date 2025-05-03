#  [形成化学键](https://leetcode.cn/problems/form-a-chemical-bond)

表: Elements
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| symbol      | varchar |
| type        | enum    |
| electrons   | int     |
+-------------+---------+
```
symbol 是该表的主键(具有唯一值的列)。

该表的每一行包含一个元素的信息。

type 是 ENUM 类型，它的值是 ('Metal', 'Nonmetal', 'Noble') 之一

 - 如果 type 是 Noble, electrons 是 0。
 - 如果 type 是 Metal, electrons 是这种元素的一个原子所能给出的电子数。
 - 如果 type 是 Nonmetal, electrons 这种元素的一个原子所需要的电子数。
 

如果一个元素是 'Metal'，另外一个元素是 'Nonmetal' ，那么它们可以形成键。

编写一个解决方案找出所有可以形成键的元素对。

以 任意顺序 返回结果表。

查询结果格式如下所示。

 

示例 1:

> 输入: 
> 
> Elements 表:
> ```
> +--------+----------+-----------+
> | symbol | type     | electrons |
> +--------+----------+-----------+
> | He     | Noble    | 0         |
> | Na     | Metal    | 1         |
> | Ca     | Metal    | 2         |
> | La     | Metal    | 3         |
> | Cl     | Nonmetal | 1         |
> | O      | Nonmetal | 2         |
> | N      | Nonmetal | 3         |
> +--------+----------+-----------+
> ```
> 输出: 
> ```
> +-------+----------+
> | metal | nonmetal |
> +-------+----------+
> | La    | Cl       |
> | Ca    | Cl       |
> | Na    | Cl       |
> | La    | O        |
> | Ca    | O        |
> | Na    | O        |
> | La    | N        |
> | Ca    | N        |
> | Na    | N        |
> +-------+----------+
> ```
> 解释: 
> - Metal 元素包括 La, Ca, and Na.
> - Nonmetal 元素包括 Cl, O, and N.
> - 每个 Metal 元素与输出表中的 Nonmeal 元素配对。