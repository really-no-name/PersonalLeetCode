#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 使用哈希表来存储已经遍历过的数字及其索引
        unordered_map<int, int> num_map;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // 检查哈希表中是否存在与当前数字配对的数字
            if (num_map.find(complement) != num_map.end()) {
                return {num_map[complement], i};
            }
            
            // 将当前数字及其索引存入哈希表
            num_map[nums[i]] = i;
        }
        
        // 如果没有找到符合条件的数字对，返回空向量
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = solution.twoSum(nums, target);
    
    if (!result.empty()) {
        cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
    } else {
        cout << "No two sum solution found." << endl;
    }
    
    return 0;
}