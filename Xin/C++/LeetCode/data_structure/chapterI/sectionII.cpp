/*
 * @Author: your name
 * @Date: 2021-02-17 18:36:08
 * @LastEditTime: 2021-02-21 09:42:56
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterOne\sectionTwo.cpp
 */

#include <iostream>
using namespace std;

class Splution
{

public:
    string replaceSpace(string s)
    {
        int count = 0, len = s.size();
        for (char c : s) //统计空格数量
        {
            if (c == ' ')
                count++;
        }
        s.resize(len + 2 * count); //修改s长度

        //倒序遍历修改
        for (int i = len - 1, j = s.size() - 1; i < j; i--, j--)
        {
            if (s[i] != ' ')
                s[j] = s[i];
            else
            {
                s[j - 2] = '%';
                s[j - 1] = '2';
                s[j] = '0';
                j -= 2;
            }
        }
        return s;
    }
};