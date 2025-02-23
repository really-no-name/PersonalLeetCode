/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 2 的幂。
 * 时间复杂度： O(1)
 * 空间复杂度： O(1)
 ******************************************************************************/
#include <iostream>

using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n > 0) {
          if ((n & (n - 1)) == 0) {
            return true;
          }
        }
        return false;
    }
};

int main() {
  Solution sol;
  cout << sol.isPowerOfTwo(2) << endl;
}