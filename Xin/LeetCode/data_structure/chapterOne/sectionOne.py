# 可变数组
array = []
array.append(2)
array.append(3)
print(array)


# 链表
class ListNode:
    def __init__(self, x):
        self.val = x  # 节点值
        self.next = None  # 后继节点引用


n1 = ListNode(4)  # 实例化节点，节点head
n2 = ListNode(5)
n3 = ListNode(6)

n1.next = n2  # 构建引用指向
n2.next = n3

# 栈，python可将列表作为栈使用,「先入后出」
array.pop()
print(array)

# 双端队列,队列是一种具有 「先入先出」 特点的抽象数据结构，可使用链表实现
from collections import deque

queque = deque()
queque.append(1)
queque.append(2)
queque.popleft()


# 树
class TreeNode:
    def __init__(self, x):
        self.vel = x  # 节点值
        self.left = None  # 左子节点
        self.right = None  # 右子节点

    # 初始化节点


n1 = TreeNode(3)  # 根节点 root
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(2)

# 构建引用指向

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# 图，分为有向图和无向图
# 邻接矩阵表示图
vertices = [1, 2, 3, 4, 5]
edges = [
    [0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0]
]

# 邻接表表示矩阵
vertices = [1, 2, 3, 4, 5]
edges = [
    [1, 2, 3, 4],
    [0, 3],
    [0, 4],
    [0, 1, 4],
    [0, 2, 3]
]
# 邻接表 适合存储稀疏图（顶点较多、边较少）； 邻接矩阵 适合存储稠密图（顶点较少、边较多）

# 散列表,hash函数
dic = {}
dic['小丽'] = int('010001')
dic['张三'] = int('010002')
dic['小华'] = int('010003')

print(dic['小丽'])  # --> '010010'
# 自行设计hash函数
names = ['小丽', '张三', '小华']

def hash(id):
    index = (id-1) % 10000
    return index

print(names[hash('010001')])


# 堆
from heapq import heappush, heappop

heap = []  # 初始化小顶堆

heappush(heap, 1)  # 元素入堆
heappush(heap, 4)
heappush(heap, 2)
heappush(heap, 6)
heappush(heap, 8)

heappop(heap)  # 元素出堆（从小到大）
