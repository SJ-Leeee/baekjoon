import sys

sys.setrecursionlimit(10000)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, node):
        if not self.root:
            self.root = node
        else:
            prev_node = None
            cur_node = self.root

            while cur_node:
                if cur_node.val > node.val:
                    prev_node = cur_node
                    cur_node = cur_node.left
                else:
                    prev_node = cur_node
                    cur_node = cur_node.right

            if prev_node.val > node.val:
                prev_node.left = node
            else:
                prev_node.right = node

    def post_order(self):
        result = []

        def post_dfs(node):
            if not node:
                return

            post_dfs(node.left)
            post_dfs(node.right)
            result.append(node.val)

        post_dfs(self.root)
        return result


tree = Tree()

while True:
    value = sys.stdin.readline().strip()

    if not value:
        break
    # 처리 로직
    value = int(value)
    node = TreeNode(value)
    tree.insert_node(node)

a = tree.post_order()
for i in a:
    print(i)
