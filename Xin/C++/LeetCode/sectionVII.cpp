/*
 * @Author: your name
 * @Date: 2021-02-22 19:09:29
 * @LastEditTime: 2021-02-22 19:12:37
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\sectionVII.cpp
 */

#include <stack>
using namespace std;
class MinStack
{
public:
    stack<int> A, B;
    MinStack() {}
    void push(int x)
    {
        A.push(x);
        if (B.empty() || B.top() >= x)
            B.push(x);
    }
    void pop()
    {
        if (A.top() == B.top())
            B.pop();
        A.pop();
    }
    int top()
    {
        return A.top();
    }
    int min()
    {
        return B.top();
    }
};
