/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 整数的各位积和之差。
 * 时间复杂度： O(N)
 * 空间复杂度： O(N)
 ******************************************************************************/
#include <iostream>
#include <string>

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        std::string numStr = std::to_string(n); // 将整数转换为字符串

        for (char ch : numStr) {
            int digit = ch - '0'; // 将字符转换为数字
            sum += digit;
            product *= digit;
        }

        return product - sum;
    }
};

int main() {
    Solution sol;
    std::cout << sol.subtractProductAndSum(234) << std::endl;
    return 0;
}