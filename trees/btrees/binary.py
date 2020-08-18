#!/usr/bin/env python3.8

sorted_collection = []

class Leaf:
    def __init__(self, data):
        self.left, self.right = None, None
        self.data = data
        self.sorted_contents = []

    def insert(self, data):
        # if the root node is populated
        if(self.data):
            # if the data belongs on the left side
            if(data < self.data):
                # if we reach the end of the tree on this side
                if not(self.left):
                    self.left = Leaf(data)
                # if not, we continue traversing
                else:
                    self.left.insert(data)
            # if the data belongs on the right side
            elif(data > self.data):
                # if we reach the end of the tree on this side
                if not(self.right):
                    self.right = Leaf(data)
                # continue traversing on the right side
                else:
                    self.right.insert(data)

        # if there is no root node present
        else:
            self.data = data

    def print_tree_inorder(self):
        if(self.left):
            self.left.print_tree_inorder()
        print(self.data)
        if(self.right):
            self.right.print_tree_inorder()
    def print_tree_preorder(self):
        print(self.data)
        if(self.left):
            self.left.print_tree_inorder()
        if(self.right):
            self.right.print_tree_inorder()
    def print_tree_postorder(self):
        if(self.left):
            self.left.print_tree_inorder()
        if(self.right):
            self.right.print_tree_inorder()
        print(self.data)

root = Leaf(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree_preorder()
print()
root.print_tree_inorder()
print()
root.print_tree_postorder()
