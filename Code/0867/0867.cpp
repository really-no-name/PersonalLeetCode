/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 转置矩阵。
 * 时间复杂度： O(N∗M)
 * 空间复杂度： O(N∗M)
 * 执行用时： 0 ms
 * 消耗内存： 14.59 mb
 ******************************************************************************/
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};

        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<vector<int>> transposed(cols, vector<int>(rows));

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                transposed[j][i] = matrix[i][j];
            }
        }

        return transposed;
    }
};


int main() {
  Solution s;
  vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
  vector<vector<int>> ans = s.transpose(matrix);
  // 输出转置后的矩阵
  cout << "Transposed Matrix:" << endl;
  for (const auto& row : transposed) {
    for (int val : row) {
      cout << val << " ";
    }
    cout << endl;
  }
  return 0;
}