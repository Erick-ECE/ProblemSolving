# binary tree traversal
'''tree definition'''
class ListNode(object):
    def __init__(self,v):
        self.value=v
        self.right=None
        self.left=None
    
# create a tree
root= ListNode('F')
A= ListNode('A')
B= ListNode('B')
C= ListNode('C')
D= ListNode('D')
E= ListNode('E')
F= ListNode('F')
G= ListNode('G')
H= ListNode('H')
I= ListNode('I')
#conect Nodes
root.left=B
root.right=G
B.left=A
B.right=D
D.left=C
D.right=E
G.right=I
I.left=H

#print DFS order
def dfs(tree):
    if tree:
       return dfs_print(tree,"")

def dfs_print(node,recorrido):
    if node:
        recorrido+= node.value
        recorrido= dfs_print(node.left,recorrido) 
        recorrido= dfs_print(node.right,recorrido)
    return recorrido

dfs(root)