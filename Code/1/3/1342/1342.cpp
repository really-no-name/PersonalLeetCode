/******************************************************************************
 * 文件名: 1342
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 将数字变成 0 的操作次数。
 * 时间复杂度： O(Logn)
 * 空间复杂度： O(1)
 * 执行用时： 0 ms
 * 消耗内存： 7.81 mb
 ******************************************************************************/
#include <iostream>

using namespace std;

class Solution {
public:
    int numberOfSteps(int num) {
        int step = 0;
        while (num > 0) {
            if (num % 2 == 0) {
                num /= 2;
            }
            else {
                num -= 1;
            }
            step++;
        }
        return step;

    }
};


int main() {
    Solution solution;
    cout << solution.numberOfSteps(14) << endl;
}