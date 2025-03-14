/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 各位相加。
 * 时间复杂度： O(1)
 * 空间复杂度： O(1)
 ******************************************************************************/
#include <iostream>

using namespace std;

class Solution {
public:
    int addDigits(int num) {
        return (num - 1) % 9 + 1;
    }
};

int main() {
  Solution s;
  cout << s.addDigits(38) << endl;
}