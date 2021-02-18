/*
 * @Author: your name
 * @Date: 2021-02-18 09:18:52
 * @LastEditTime: 2021-02-18 09:25:09
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterOne\sectionThree.cpp
 */
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct ListNode
{
    int val;        // 节点值
    ListNode *next; // 后继节点引用
    ListNode(int x) : val(x), next(NULL) {}
};

//递归法
class Solution
{
public:
    vector<int> reversePrint(ListNode *head)
    {
        recur(head);
        return res;
    }

private:
    vector<int> res;
    void recur(ListNode *head)
    {
        if (head == nullptr)
            return;
        recur(head->next);
        res.push_back(head->val);
    }
};

//辅助栈法
class Solution
{
public:
    vector<int> reversePrint(ListNode *head)
    {
        stack<int> stk;
        while (head != nullptr)
        {
            stk.push(head->val);
            head = head->next;
        }
        vector<int> res;
        while (!stk.empty())
        {
            res.push_back(stk.top());
            stk.pop();
        }
        return res;
    }
};