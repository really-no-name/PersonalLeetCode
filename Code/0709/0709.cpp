/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 转换成小写字母。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 * 执行用时： 0 ms
 * 消耗内存： 8.09 mb
 ******************************************************************************/
#include <iostream>

using namespace std;

class Solution {
public:
    string toLowerCase(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        return s;
    }
};

int main() {
  Solution s;
  cout << s.toLowerCase("LOVELY") << endl;
}