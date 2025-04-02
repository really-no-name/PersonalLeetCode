/******************************************************************************
 * 文件名: 2873
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 有序三元组中的最大值 I。
 * 时间复杂度：
 * 空间复杂度：
 ******************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long ans = 0;
        int n = nums.size();
        for (int i = 0; i < n - 2; i ++) {
            for (int j = i + 1; j < n - 1; j ++) {
                for (int k = j + 1; k < n; k ++) {
                    ans = max(ans, (long long)(nums[i] - nums[j]) * nums[k]);
                }
            }
        }
        return ans;
    }
};