from typing import List
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
    

    def insert(self, data) -> None:
        node = Node(data) 
        if self.root is None:
            self.root = node
            return
        
        temp = self.root

        while temp:
            if node.data < temp.data:
                
                if temp.left == None: 
                    temp.left = node
                    break
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = node
                    break
                temp = temp.right
    
    def _inorder_traversal(self, node: Node, result: list):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)


    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        print("In Order:", result)


    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        print(result)

    def _postorder_traversal(self, node, result):
        if node is not None:
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
            result.append(node.data)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        print(result)    
    def display(self):
        result = []
        self._inorder_traversal(self.root, result)
        print("In Order  :", result)

        result = []
        self._preorder_traversal(self.root, result)
        print("Pre Order :", result)

        result = []
        self._postorder_traversal(self.root, result)
        print("Post Order:", result)


    def search(self, key):
        path = []
        if self._search(self.root, key, path):
            path.reverse()
            print(f"Found {key}; Path:", path)
            return True
        else:
            print(f"Not found {key}")
            return False

    def _search(self, node, key, path):

        if node is not None:
            if node.data == key:
                path.append(node.data)
                return True
            elif key < node.data:
                found = self._search(node.left, key, path)
                if found: path.append(node.data)
                return found
            else:
                found = self._search(node.right, key, path)
                if found: path.append(node.data)
                return found

    def delete(self, data: int):
        pass
    




if __name__ == "__main__":
    tree = BST()

    tree.insert(55)
    tree.insert(50)
    tree.insert(40)
    tree.insert(60)
    tree.insert(52)
    tree.insert(22)
    tree.insert(67)
    tree.insert(88)
    tree.insert(50)
    tree.insert(23)
    tree.insert(68)
    tree.insert(87)
    tree.insert(49)
    tree.display()
    tree.search(22)