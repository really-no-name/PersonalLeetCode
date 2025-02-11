//
// Created by Bolun Xu on 25-2-11.
//
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int carry = 0;  // 进位
        int i = a.length() - 1;
        int j = b.length() - 1;

        // 从左到右逐位相加
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) {
                sum += a[i--] - '0';  // 将字符转换为数字
                i --;
            }
            if (j >= 0) {
                sum += b[j--] - '0';
                j--;
            }
            carry = sum / 2;
            res.push_back(sum % 2 + '0');
        }

        // 反转结果字符串
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution s;
    cout << s.addBinary("11", "1") << endl;
    cout << s.addBinary("1010", "1011") << endl;
}