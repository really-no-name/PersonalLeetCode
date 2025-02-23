/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 3 的幂。
 * 时间复杂度： O(1)
 * 空间复杂度： O(1)
 ******************************************************************************/
class Solution {
public:
    bool isPowerOfThree(int n) {
        long lim = pow(3, 19);
        if (n > 0) {
            if (lim % n == 0) {
                return true;
            }
        }
        return false;
    }
};