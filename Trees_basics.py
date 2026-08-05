"""class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    # Find minimum value node
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            # Case 1 & 2: Node has 0 or 1 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has 2 children
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# Example usage
if __name__ == "__main__":
    tree = BST()
    root = None
    root = tree.insert(root, 50)
    tree.insert(root, 30)
    tree.insert(root, 20)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Inorder traversal:")
    tree.inorder(root)

    print("\nDelete 20")
    root = tree.delete(root, 20)
    tree.inorder(root)

    print("\nDelete 30")
    root = tree.delete(root, 30)
    tree.inorder(root)

    print("\nDelete 50")
    root = tree.delete(root, 50)
    tree.inorder(root)
"""







class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class bst:
    def __init__(self):
        self.root  = None
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data <root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)
        return root
    def minValueNode(self,Node):
        current = Node
        while current.left:
            current = current.left
        return current
    def delete(self,root,data):
        if root is None:
            return None
        if data < root.data :
            root.left = self.delete(root.left,data)
        elif data >root.data :
            root.right = self.delete(root.right,data)
            #no child
        else:
            if root.left is None and root.right is None:
                return None
            # 1 child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 2 childs
            else:
                temp = self.minValueNode(root.right)
                root.data = temp.data
                root.right = self.delete(root.right,temp.data)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end = " ")
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")      
            self.preorder(root.left)       
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)     
            self.postorder(root.right)  
            print(root.data, end=" ")
if __name__ == "__main__":
    tree = bst()
    root = None
    root = tree.insert(root, 50)
    tree.insert(root, 30)
    tree.insert(root, 20)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)
    tree.insert(root, 50)
    print("\n Inorder traversal:")
    tree.inorder(root)
    print("\npreorder traversal:")
    tree.preorder(root)
    print("\npostorder traversal:")
    tree.postorder(root)
    

    print("\nDelete 20")
    root = tree.delete(root, 20)
    tree.inorder(root)

    print("\nDelete 30")
    root = tree.delete(root, 30)
    tree.inorder(root)

    print("\nDelete 50")
    root = tree.delete(root, 50)
    tree.inorder(root)
    






            
