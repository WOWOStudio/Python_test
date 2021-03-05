/*
 * @Author: your name
 * @Date: 2021-03-05 09:59:52
 * @LastEditTime: 2021-03-05 10:03:58
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionIV.cpp
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int res = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i - 1] > 0)
                nums[i] += nums[i - 1];
            if (nums[i] > res)
                res = nums[i];
        }
        return res;
    }
};