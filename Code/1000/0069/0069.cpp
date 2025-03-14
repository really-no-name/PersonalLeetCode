//0 ms, 8.38 mb
// Created by Bolun Xu on 25-2-11.
// float：是单精度浮点类型，通常占用32位（4字节）的存储空间。它提供大约6到7位的有效数字，这意味着它可以精确表示小数点后大约6到7位的数值。
// double：是双精度浮点类型，通常占用64位（8字节）的存储空间。 它提供大约15到16位的有效数字，因此比float类型提供更高的精度。

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
	int mySqrt(int x) {
		if (x == 0) return 0;
        double x_0 = 0.5 * x;
        while (true) {
        	double x_n = (x_0 + x / x_0) / 2;
            if (abs(x_n - x_0) < 1e-7) break;
            x_0 = x_n;
        }
		// printf(x_0)
        return int(x_0);
	}
};

int main() {
	Solution s;
    printf("%d\n", s.mySqrt(10));
	printf("%d\n", s.mySqrt(2147395599));
	return 0;
}

