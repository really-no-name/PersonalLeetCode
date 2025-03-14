#  [N 叉树的直径](https://leetcode.cn/problems/diameter-of-n-ary-tree?envType=weekly-question&envId=2025-03-02)

给定一棵 N 叉树 的根节点 root ，计算这棵树的直径长度。

N 叉树的直径指的是树中任意两个节点间路径中 最长 路径的长度。这条路径可能经过根节点，也可能不经过根节点。

（N 叉树的输入序列以层序遍历的形式给出，每组子节点用 null 分隔）

 

示例 1：



> 输入：root = [1,null,3,2,4,null,5,6]
> 
> 输出：3
> 
> 解释：直径如图中红线所示。

示例 2：



> 输入：root = [1,null,2,null,3,4,null,5,null,6]
> 
> 输出：4

示例 3：



> 输入: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
> 
> 输出: 7
 

提示：

- N 叉树的深度小于或等于 1000 。
- 节点的总个数在 [0, 10^4] 间。