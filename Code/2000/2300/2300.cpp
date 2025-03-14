/******************************************************************************
 * 文件名: 2300
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：39 ms
 * 消耗内存：99.39 mb
 ******************************************************************************/
#include <iostream>
#include <vector>
#include <algorithm>  // 用于 sort 和 lower_bound

using namespace std;

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        // 对药水数组进行排序
        sort(potions.begin(), potions.end());

        vector<int> ans(spells.size(), 0);  // 初始化结果数组

        for (size_t i = 0; i < spells.size(); i++) {
            // 计算当前法术的最小药水强度阈值
            double threshold = static_cast<double>(success) / spells[i];

            // 使用二分查找找到第一个大于等于阈值的药水位置
            auto it = lower_bound(potions.begin(), potions.end(), threshold);

            // 计算满足条件的药水数量
            ans[i] = potions.end() - it;
        }

        return ans;
    }
};

int main() {
    Solution s;

    // 测试用例 1
    vector<int> spells1 = {5, 1, 3};
    vector<int> potions1 = {1, 2, 3, 4, 5};
    long long success1 = 7;
    vector<int> result1 = s.successfulPairs(spells1, potions1, success1);
    cout << "[";
    for (size_t i = 0; i < result1.size(); i++) {
        cout << result1[i];
        if (i < result1.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;  // 输出: [4, 0, 3]

    // 测试用例 2
    vector<int> spells2 = {3, 1, 2};
    vector<int> potions2 = {8, 5, 8};
    long long success2 = 16;
    vector<int> result2 = s.successfulPairs(spells2, potions2, success2);
    cout << "[";
    for (size_t i = 0; i < result2.size(); i++) {
        cout << result2[i];
        if (i < result2.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;  // 输出: [2, 0, 2]

    return 0;
}