//
// Created by Bolun Xu on 25-2-11.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left_index = 0, right_index = numbers.size() - 1;

        while (left_index < right_index) {
            int sum = numbers[left_index] + numbers[right_index];
            if (sum == target) {
                break;
            }
            else if (sum < target) {
                left_index++;
            }
            else {
                right_index--;
            }
        }
        left_index ++;
        right_index ++;
        return {left_index , right_index};
    }
};


int main() {
    Solution sol;
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = sol.twoSum(numbers, target);
    cout << "[" << result[0] << ',' << result[1] << "]" << endl;
    return 0;
}