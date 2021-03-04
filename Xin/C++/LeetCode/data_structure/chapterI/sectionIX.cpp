/*
 * @Author: your name
 * @Date: 2021-02-24 11:11:23
 * @LastEditTime: 2021-02-24 11:19:08
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\sectionIX.cpp
 */
#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
    string reverseLefWords(string s, int n)
    {
        reverseString(s, 0, n - 1);
        reverseString(s, n, s.size() - 1);
        reverseString(s, 0, s.size() - 1);
        return s;
    }

private:
    void reverseString(string &s, int i, int j)
    {
        while (i < j)
        {
            swap(s[i++], s[j--]);
        }
    }
};

class Solution
{
public:
    string reverseLeftWords(string s, int n)
    {
        reverse(s.begin(), s.begin() + n);
        reverse(s.begin() + n, s.end());
        reverse(s.begin(), s.end());
        return s;
    }
};
