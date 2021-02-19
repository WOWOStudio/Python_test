/*
 * @Author: your name
 * @Date: 2021-02-19 10:06:09
 * @LastEditTime: 2021-02-19 10:10:43
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterOne\secctionFour.cpp
 */

#include <iostream>
#include <stack>
using namespace std;
class CQueue
{
public:
    stack<int> A, B;
    CQueue() {}
    void appendTail(int value)
    {
        A.push(value);
    }

    int deleteHead()
    {
        if (!B.empty())
        {
            int tmp = B.top();
            B.pop();
            return tmp;
        }
        if (A.empty())
            return -1;
        while (!A.empty())
        {
            int tmp = A.top();
            A.pop();
            B.push(tmp);
        }
        int tmp = B.top();
        B.pop();
        return tmp;
    }
};