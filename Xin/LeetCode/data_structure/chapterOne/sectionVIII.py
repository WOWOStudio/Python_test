class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 哈希表，字典


class Solution:
    def copyRandomList(self, head:'Node')->'Node':
        if not head: return
        dic={}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head

        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

# 拼接 + 拆分

class Solution:
    def copyRandomList(self, head:'Node') -> 'Node':
        if not head: return
        cur = head

        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res

