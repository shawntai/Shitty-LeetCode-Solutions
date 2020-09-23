def sol(root):
    #maxDepth = 0

    def do_things(node, depth):
        #global maxDepth
        if node:
            return max(do_things(node.left, depth + 1), do_things(node.right, depth + 1))
        else:
            return depth

    return do_things(root, 0)


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


n15 = Node(None, None)
n7 = Node(None, None)
n20 = Node(n15, n7)
n9 = Node(None, None)
root_n3 = Node(n9, n20)

print(sol(root_n3))