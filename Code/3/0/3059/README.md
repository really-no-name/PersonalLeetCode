#  [找到所有不同的邮件域名](https://leetcode.cn/problems/find-all-unique-email-domains)

表：Emails
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | id          | int     |
> | email       | varchar |
> +-------------+---------+
> ```
> id 是这张表的主键（有不同值的列）。
> 
> 这张表的每一行包含一个电子邮件地址。电子邮件地址不包含大写字母。

编写一个解决方案来找到所有 不同的电子邮件域名 并且计数与每个域名相关联的 记录。只考虑 以 .com 结尾 的域名。

返回结果表以 email_domains 升序 排列。

结果格式如下所示。

 

示例 1:

> 输入： 
> 
> Emails 表：
> ```
> +-----+-----------------------+
> | id  | email                 |
> +-----+-----------------------+
> | 336 | hwkiy@test.edu        |
> | 489 | adcmaf@outlook.com    |
> | 449 | vrzmwyum@yahoo.com    |
> | 95  | tof@test.edu          |
> | 320 | jxhbagkpm@example.org |
> | 411 | zxcf@outlook.com      |
> +----+------------------------+
> ```
> 输出： 
> ```
> +--------------+-------+
> | email_domain | count |
> +--------------+-------+
> | outlook.com  | 2     |
> | yahoo.com    | 1     |  
> +--------------+-------+
> ```
> 解释： 
> - 以“.com”结束的合法域名只有“outlook.com”和“yahoo.com”，数量分别为 2 和 1。
> 
> 输出表以 email_domains 升序排列。