/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：
 * 消耗内存：
 ******************************************************************************/


class Solution {
public:
    int smallestEvenMultiple(int n) {
        return  (n % 2 + 1) * n;
    }
};