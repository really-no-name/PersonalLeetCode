/******************************************************************************
 * 文件名: 0744
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 寻找比目标字母大的最小字母。
 * 时间复杂度：O(LogN)
 * 空间复杂度：O(1)
 * 执行用时：0 ms
 * 消耗内存：19.49 mb
 ******************************************************************************/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  char nextGreatestLetter(vector<char>& letters, char target) {
    int left = -1;
    int right = letters.size();
    while (left + 1 < right) {
      int mid = left + ( - left + right) / 2;
      if (letters[mid] <= target) {
        left = mid;
      }
      else {
        right = mid;
      }
    }
    if (right < letters.size()) {
      return letters[right];
    }
    else {
      return letters[0];
    }
  }
};

int main() {
  Solution s;

  vector<char> letters1 = {'c', 'f', 'j'};
  cout << s.nextGreatestLetter(letters1, 'a') << endl;  // 输出: c

  vector<char> letters2 = {'c', 'f', 'j'};
  cout << s.nextGreatestLetter(letters2, 'd') << endl;  // 输出: f

  vector<char> letters3 = {'x', 'x', 'y', 'y'};
  cout << s.nextGreatestLetter(letters3, 'z') << endl;  // 输出: x

  return 0;
}