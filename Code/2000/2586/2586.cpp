/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：
 * 消耗内存：
 ******************************************************************************/
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int vowelStrings(vector<string>& words, int left, int right) {
        int count = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        for (int i = left; i <= right; ++i) {
            string word = words[i];
            if (vowels.find(word[0]) != vowels.end() && vowels.find(word.back()) != vowels.end()) {
                cout << "DEBUG: " << word << endl;
                count++;
            }
        }

        return count;
    }
};

int main() {
    Solution sol;

    vector<string> words1 = {"are", "amy", "u"};
    cout << sol.vowelStrings(words1, 0, 2) << endl;

    vector<string> words2 = {"hey", "aeo", "mu", "ooo", "artro"};
    cout << sol.vowelStrings(words2, 1, 4) << endl;

    return 0;
}