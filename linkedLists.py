# my own class list

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

nodo1 = ListNode(1)
nodo2 = ListNode(2)
nodo3 = ListNode(3)
nodo4 = ListNode(4)
nodo5 = ListNode(5)
nodo6 = ListNode(6)
nodo7 = ListNode(7)
nodo8 = ListNode(8)
nodo9 = ListNode(9)
nodo10 = ListNode(10)
nodo1.next=nodo2
nodo2.next=nodo3
nodo3.next=nodo4
nodo4.next=nodo5
nodo5.next=nodo6
nodo6.next=nodo7
nodo7.next=nodo8
nodo8.next=nodo9
nodo9.next=nodo10


#reverse
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    ls = []
    while l:
        ls.append(l.value)
        l=l.next
    return ls == ls[::-1]

def reverse(l):
    head=l.value
    prev=None
    current=l
    while current:
        next= current.next
        current.next=prev
        prev=current
        current = next
        head = current

reverse(nodo1)

def printList(l):
    while l:
        print(l.value)
        l = l.next

printList(nodo10)

print(isListPalindrome(nodo1))