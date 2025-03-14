/******************************************************************************
 * 文件名: 0412
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: Fizz Buzz。
 * 时间复杂度： O(N)
 * 空间复杂度： O(N)
 * 执行用时： 4 ms
 * 消耗内存： 11.61 mb
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
        for (int i = 1; i <= n; i++) {
          if (i % 3 == 0 && i % 5 == 0) {
            ans.push_back("FizzBuzz");
          }
          else if (i % 3 == 0) {
            ans.push_back("Fizz");
          }
          else if (i % 5 == 0) {
              ans.push_back("Buzz");
          }
          else {
            ans.push_back(to_string(i));
          }
        }
        return ans;
    }
};

