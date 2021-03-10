/*
 * @Author: your name
 * @Date: 2021-03-10 10:03:06
 * @LastEditTime: 2021-03-10 10:17:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionVIII.cpp
 */

#include <iostream>
using namespace std;
class Solution
{
public:
    int nthUglyNumber(int n)
    {
        int i, a = 0, b = 0, c = 0;
        int dp[n];
        dp[0] = 1;
        for (i = 1; i < n; i++)
        {
            int n2 = dp[a] * 2;
            int n3 = dp[b] * 3;
            int n5 = dp[c] * 5;
            dp[i] = min(n2, min(n3, n5));
            if (dp[i] == n2)
                a++;
            if (dp[i] == n3)
                b++;
            if (dp[i] == n5)
                c++;
        }
        return dp[n - 1];
    }
};