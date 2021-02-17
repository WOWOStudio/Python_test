/*
 * @Author: your name
 * @Date: 2021-02-17 11:30:15
 * @LastEditTime: 2021-02-17 18:09:35
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \C++\LeetCode\data_structure\chapterOne\sectionOne.cpp
 */

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

//!链表
struct ListNode
{
    int val;        // 节点值
    ListNode *next; // 后继节点引用
    ListNode(int x) : val(x), next(NULL) {}
};

//!树
struct TreeNode
{
    int val;         //节点值
    TreeNode *left;  //左子节点
    TreeNode *right; //右子节点
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int the_hash(int id)
{
    int index = (id - 1) % 10000;
    return index;
}

int main()
{
    //!可变数组
    vector<int> array;
    array.push_back(2);
    array.push_back(3);
    cout << array[0];

    // 实例化链表节点
    ListNode *n1 = new ListNode(4); // 节点 head
    ListNode *n2 = new ListNode(5);
    ListNode *n3 = new ListNode(1);

    // 构建引用指向
    n1->next = n2;
    n2->next = n3;

    //!栈
    stack<int> stk;
    stk.push(1);
    stk.push(2);
    stk.pop();
    stk.pop();

    //!队列
    queue<int> que;
    que.push(1);
    que.push(2);
    que.pop();

    // 初始化树节点
    TreeNode *N1 = new TreeNode(3); // 根节点 root
    TreeNode *N2 = new TreeNode(4);
    TreeNode *N3 = new TreeNode(5);
    TreeNode *N4 = new TreeNode(1);
    TreeNode *N5 = new TreeNode(2);

    // 构建引用指向
    N1->left = N2;
    N1->right = N3;
    N2->left = N4;
    N2->right = N5;

    //!图
    //邻接矩阵表示图
    int vertices[5] = {1, 2, 3, 4, 5};
    int edges[5][5] = {{0, 1, 1, 1, 1},
                       {1, 0, 0, 1, 0},
                       {1, 0, 0, 0, 1},
                       {1, 1, 0, 0, 1},
                       {1, 0, 1, 1, 0}};
    //邻接表表示图
    int vertices[5] = {1, 2, 3, 4, 5};
    vector<vector<int>> edges;

    vector<int> edge_1 = {1, 2, 3, 4};
    vector<int> edge_2 = {0, 3};
    vector<int> edge_3 = {0, 4};
    vector<int> edge_4 = {0, 1, 4};
    vector<int> edge_5 = {0, 2, 3};

    edges.push_back(edge_1);
    edges.push_back(edge_2);
    edges.push_back(edge_3);
    edges.push_back(edge_4);
    edges.push_back(edge_5);

    //! 初始化散列表
    unordered_map<string, int> dic;

    // 添加 key -> value 键值对
    dic["小力"] = 10001;
    dic["小特"] = 10002;
    dic["小扣"] = 10003;

    // 从姓名查找学号
    dic.find("小力")->second; // -> 10001
    dic.find("小特")->second; // -> 10002
    dic.find("小扣")->second; // -> 10003

    //自行设计hash函数
    string names[] = {"小力", "小特", "小扣"};
    names[int(the_hash(10001))];

    // 初始化小顶堆
    priority_queue<int, vector<int>, greater<int>> heap;

    // 元素入堆
    heap.push(1);
    heap.push(4);
    heap.push(2);
    heap.push(6);
    heap.push(8);

    // 元素出堆（从小到大）
    heap.pop(); // -> 1
    heap.pop(); // -> 2
    heap.pop(); // -> 4
    heap.pop(); // -> 6
    heap.pop(); // -> 8
}
