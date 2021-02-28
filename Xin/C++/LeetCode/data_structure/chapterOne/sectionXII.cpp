/*
 * @Author: your name
 * @Date: 2021-02-28 19:52:20
 * @LastEditTime: 2021-02-28 20:02:34
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\sectionXII.cpp
 */
#include <iostream>
#include <limits.h>
using namespace std;
class Solution
{
public:
    int strToInt(string str)
    {
        int res = 0, bndry = INT_MAX / 10;
        int i = 0, sign = 1, length = str.size();
        if (length == 0)
            return 0;
        while (str[i] == ' ')
        {
            if (++i == length)
                return 0;
        }
        if (str[i] == '-')
            sign = -1;
        if (str[i] == '-' || str[i] == '+')
            i++;
        for (int j = i; j < length; j++)
        {
            if (str[j] < '0' || str[j] > '9')
                break;
            if (res > bndry || res == bndry && str[j] > '7')
                return sign == 1 ? INT_MAX : INT_MIN;
            res = res * 10 + (str[j] - '0');
        }
        return sign * res;
    }
};