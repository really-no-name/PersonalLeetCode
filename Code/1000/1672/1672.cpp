/******************************************************************************
 * 文件名: 1672
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 1672。
 * 时间复杂度： O(N)
 * 空间复杂度： O(N)
 * 执行用时： 3 ms
 * 消耗内存： 11.3 mb
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
    public:
    int maximumWealth(vector<vector<int>>& accounts) {
        std::vector<int> account_sum;
        for (const auto& account : accounts) {
            int sum = std::accumulate(account.begin(), account.end(), 0);
            account_sum.push_back(sum);
        }
        return *std::max_element(account_sum.begin(), account_sum.end());
    }
};

int main() {
    Solution sol;
    std::vector<std::vector<int>> accounts = {{1, 2, 3}, {3, 2, 1}};
    std::cout << sol.maximumWealth(accounts) << std::endl;
    return 0;
}