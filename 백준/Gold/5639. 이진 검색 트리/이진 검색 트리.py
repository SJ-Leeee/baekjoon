class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def set_node(self, node):
        if self.root == None:
            self.root = node
        else:
            prev_node = None
            cur_node = self.root
            while cur_node != None:
                if cur_node.val < node.val:
                    prev_node = cur_node
                    cur_node = cur_node.right
                else:
                    prev_node = cur_node
                    cur_node = cur_node.left
            if prev_node.val < node.val:
                prev_node.right = node
            else:
                prev_node.left = node

    def post_order(self, node):
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)

        print(node.val)
        return

    def get_root(self):
        return self.root


import sys

sys.setrecursionlimit(10000)
tree = Tree()

while True:
    value = sys.stdin.readline().strip()

    if not value:
        break
    # 처리 로직
    value = int(value)
    node = TreeNode(value)
    tree.set_node(node)

root_node = tree.get_root()
tree.post_order(root_node)
