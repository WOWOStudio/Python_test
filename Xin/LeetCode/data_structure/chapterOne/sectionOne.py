#可变数组
array = []
array.append(2)
array.append(3)
print(array)

#链表
class ListNode:
    def __init__(self, x):
        self.val = x  #节点值
        self.next =  None   #后继节点引用

n1 = ListNode(4)    #实例化节点，节点head
n2 = ListNode(5)
n3 = ListNode(6)

n1.next = n2    #构建引用指向
n2.next = n3
