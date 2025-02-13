/******************************************************************************
 * 文件名: 1742
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 盒子中小球的最大数量 —— 暴力求解。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：3ms
 * 消耗内存：7.81 mb
 ******************************************************************************/


#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

class Solution {
private:
  int digitSum(int num) {
    int sum = 0;
    while (num > 0) {
      sum += num % 10;
      num /= 10;
    }
    return sum;
  }
public:
  int countBalls(int lowLimit, int highLimit) {
    vector<int> ans(50,0);

    for (int i = lowLimit; i <= highLimit; i++) {
      int box = digitSum(i);
      ans[box - 1] ++;
    }
    return *max_element(ans.begin(), ans.end());
  }
};

int main() {
  Solution s;
  cout << s.countBalls(1,10) << endl;
  return 0;
}