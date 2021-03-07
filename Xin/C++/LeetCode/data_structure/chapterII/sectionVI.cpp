/*
 * @Author: your name
 * @Date: 2021-03-07 09:57:37
 * @LastEditTime: 2021-03-07 10:09:40
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterII\sectionVI.cpp
 */
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    int maxValue(vector<vector<int>> &grid)
    {
        int m = grid.size(), n = grid[0].size();
        int i = 0, j = 0;
        for (i = 1; i < m; i++)
            grid[i][0] += grid[i - 1][0];
        for (j = 1; j < n; j++)
            grid[0][j] += grid[0][j - 1];
        for (i = 1; i < m; i++)
        {
            for (j = 1; j < n; j++)
            {
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[m - 1][n - 1];
    }
};