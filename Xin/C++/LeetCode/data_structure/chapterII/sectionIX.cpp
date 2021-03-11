/*
 * @Author: your name
 * @Date: 2021-03-10 10:44:00
 * @LastEditTime: 2021-03-11 08:31:06
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionIX.cpp
 */
#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int cost = INT_MAX, profit = 0;
        for (int price : prices)
        {
            cost = min(cost, price);
            profit = max(profit, price - cost);
        }
        return profit;
    }
};