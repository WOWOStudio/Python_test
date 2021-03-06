/*
 * @Author: your name
 * @Date: 2021-03-06 08:59:21
 * @LastEditTime: 2021-03-06 09:07:57
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionV.cpp
 */
#include <iostream>
using namespace std;

// 遍历字符串
class Solution
{
public:
    int translateNum(int num)
    {
        string s = to_string(num);
        int a = 1, b = 1, len = s.size();
        for (i = 2; i <= len; i++)
        {
            string tmp = s.substr(i - 2, i);
            int c = tmp.compare("10") >= 0 && tmp.compare("25") <= 0 ? a + b : a;
            b = a;
            a = c;
        }
        return a;
    }
};

// 数字求余
class Solution
{
public:
    int translateNum(int num)
    {
        int a = 1, b = 1, x, y = num % 10;
        while (num > 9)
        {
            num /= 10;
            x = num % 10;
            int tmp = 10 * x + y;
            int c = (tmp >= 10 && tmp <= 25) ? a + b : a;
            b = a;
            a = c;
            y = x;
        }
        return a;
    }
};