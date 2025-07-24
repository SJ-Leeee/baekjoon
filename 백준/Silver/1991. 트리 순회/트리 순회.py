import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 루트 -> 왼쪽 자식 -> 오른쪽 자식
def preorder_traversal(node, p_list):
    p_list.append(node.val)
    if node.left:
        preorder_traversal(node.left, p_list)
    if node.right:
        preorder_traversal(node.right, p_list)

    return p_list


# 왼쪽 자식 -> 루트 -> 오른쪽 자식
def inorder_traversal(node, p_list):
    if node.left:
        inorder_traversal(node.left, p_list)

    p_list.append(node.val)

    if node.right:
        inorder_traversal(node.right, p_list)

    return p_list


# 왼쪽 자식 -> 오른쪽 자식 -> 루트
def postorder_traversal(node, p_list):
    if node.left:
        postorder_traversal(node.left, p_list)

    if node.right:
        postorder_traversal(node.right, p_list)

    p_list.append(node.val)

    return p_list


"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""
nodes = {}


def get_node(name):
    if name in nodes:
        return nodes[name]

    node = TreeNode(name)
    nodes[name] = node
    return node


N = int(sys.stdin.readline())

result_node = None

for i in range(N):

    root, left, right = sys.stdin.readline().split()
    root_node = get_node(root)

    if i == 0:
        result_node = root_node

    if left != ".":
        left_node = get_node(left)
        root_node.left = left_node

    if right != ".":
        right_node = get_node(right)
        root_node.right = right_node

a = preorder_traversal(result_node, [])
b = inorder_traversal(result_node, [])
c = postorder_traversal(result_node, [])

print("".join(a))
print("".join(b))
print("".join(c))
