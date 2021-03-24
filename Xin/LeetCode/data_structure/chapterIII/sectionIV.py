'''
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

   4
 /   \
 2    7
/ \  /  \
1  3 6   9
镜像输出：

  4
 /  \
 7   2
/ \  / \
9  6 3 1



示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]


限制：

0 <= 节点个数 <= 1000

作者：Krahets
链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/59zt5i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# 递归
class Solution:
    def mirrorTree(self, root):
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

# 辅助栈
class Solution:
    def mirrorTree(self, root):
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return node
