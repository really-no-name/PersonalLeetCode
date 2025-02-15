/******************************************************************************
 * 文件名: 1706
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 球会落何处。
 * 时间复杂度：O(M*N)
 * 空间复杂度：O(N)
 * 执行用时：0 ms
 * 消耗内存：16.91 mb
 ******************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int ball_nums = grid[0].size();  // 球的数量，即网格的列数
        vector<int> ans(ball_nums, -1);  // 初始化结果数组，默认值为-1

        for (int i = 0; i < ball_nums; i++) {  // 遍历每个球
            int cur_col = i;  // 当前球的初始列位置

            for (size_t row_idx = 0; row_idx < grid.size(); row_idx++) {  // 逐层处理网格
                int direction = grid[row_idx][cur_col];  // 当前格子的方向（-1 或 1）
                int next_col = cur_col + direction;  // 计算下一个列位置

                // 检查是否出界或形成V形
                if (next_col < 0 || next_col >= ball_nums || grid[row_idx][next_col] != direction) {
                    cur_col = -1;  // 标记为卡住
                    break;
                }

                cur_col = next_col;  // 移动到下一个列
            }

            // 如果所有层处理完毕且未被卡住，则更新结果
            if (cur_col != -1) {
                ans[i] = cur_col;
            }
        }

        return ans;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> grid = {
        {1, 1, 1, -1, -1},
        {1, 1, 1, -1, -1},
        {-1, -1, -1, 1, 1},
        {1, 1, 1, 1, -1},
        {-1, -1, -1, -1, -1}
    };

    vector<int> result = solution.findBall(grid);

    // 输出结果
    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    return 0;
}