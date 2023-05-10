from queue import Queue

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue):
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        root.rightChild=insert(root.rightChild,newValue)
    return root

def bfs(node_queue):
    if not node_queue:
        return
    
    current_node = node_queue.pop(0)
    print(current_node.data)
    
    if current_node.leftChild:
        node_queue.append(current_node.leftChild)
    
    if current_node.rightChild:
        node_queue.append(current_node.rightChild)
    
    bfs(node_queue)
    
def postorder(root):
    
        if root==None:
            return
        postorder(root.leftChild)
        postorder(root.rightChild)  
        print(root.data)     
        

no_of_nodes=int(input("Enter no of nodes:"))
root_node=int(input("Enter root nodes:"))

root= insert(None,root_node)
no_of_nodes=no_of_nodes-1

while(no_of_nodes!=0):
    node_value=int(input("Node Value:"))
    insert(root,node_value)
    no_of_nodes=no_of_nodes-1

print("BFS TRAVEL")
bfs(root)
# print("Printing values of binary tree in postorder Traversal.")
# postorder(root)
