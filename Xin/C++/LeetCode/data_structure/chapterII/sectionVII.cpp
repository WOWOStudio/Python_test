/*
 * @Author: your name
 * @Date: 2021-03-08 09:22:15
 * @LastEditTime: 2021-03-10 10:05:22
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionVII.cpp
 */

#include <iostream>
#include <unordered_map>
using namespace std;

// 动态规划 + 哈希表
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> dic;
        int res = 0, tmp = 0, len = s.size(), i;
        for (int j = 0; j < len; j++)
        {
            if (dic.find(s[j]) == dic.end())
                i = -1;
            else
                i = dic.find(s[j])->second;
            dic[s[j]] = j;
            tmp = tmp < j - i ? tmp + 1 : j - i;
            res = max(res, tmp);
        }
        return res;
    }
};

// 动态规划 + 线性搜索
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int res = 0, tmp = 0, len = s.size();
        for (int j = 0; j < len; j++)
        {
            int i = j - 1;
            while (i >= 0 && s[i] != s[j])
                i--;                             // 线性查找 i
            tmp = tmp < j - i ? tmp + 1 : j - i; // dp[j - 1] -> dp[j]
            res = max(res, tmp);                 // max(dp[j - 1], dp[j])
        }
        return res;
    }
};

// 双指针 + 哈希表
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> dic;
        int i = -1, res = 0, len = s.size();
        for (int j = 0; j < len; j++)
        {
            if (dic.find(s[j]) != dic.end())
                i = max(i, dic.find(s[j])->second); // 更新左指针
            dic[s[j]] = j;                          // 哈希表记录
            res = max(res, j - i);                  // 更新结果
        }
        return res;
    }
};