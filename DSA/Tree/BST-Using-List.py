class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BST:

    def __init__(self):
        self.root=None

    
    def insertNode(self,data):
        newNode=Node(data)
        if self.root==None:
            self.root=newNode
        else:
            temp=self.root

            while True:
                if data<temp.data:
                    if temp.left==None:
                        temp.left=newNode
                        break
                    temp=temp.left

                else:
                    if temp.right is None:
                        temp.right=newNode
                        break
                    temp=temp.right

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")


bst=BST()
bst.insertNode(40)
bst.insertNode(30)
bst.insertNode(80)
print("Inorder BST : ")
bst.inorder(bst.root)
print("\nPreorder BST : ")
bst.preorder(bst.root)
print("\nPostorder BST : ")
bst.postorder(bst.root)





    