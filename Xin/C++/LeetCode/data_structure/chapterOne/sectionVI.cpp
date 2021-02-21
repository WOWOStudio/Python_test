/*
 * @Author: your name
 * @Date: 2021-02-21 09:43:12
 * @LastEditTime: 2021-02-21 09:47:44
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterOne\sectionVI.cpp
 */

#include <iostream>
using namespace std;

// 迭代
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *cur = head, *pre = nullptr;
        while (cur != nullptr)
        {
            ListNode *tmp = cur->next; // 暂存后继节点 cur.next
            cur->next = pre;           // 修改 next 引用指向
            pre = cur;                 // pre 暂存 cur
            cur = tmp;                 // cur 访问下一节点
        }
        return pre;
    }
};

// 递归
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        return recur(head, nullptr); // 调用递归并返回
    }

private:
    ListNode *recur(ListNode *cur, ListNode *pre)
    {
        if (cur == nullptr)
            return pre;                        // 终止条件
        ListNode *res = recur(cur->next, cur); // 递归后继节点
        cur->next = pre;                       // 修改节点引用指向
        return res;                            // 返回反转链表的头节点
    }
};
