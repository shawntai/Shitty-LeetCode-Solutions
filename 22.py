'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

'''


def sol(n):

    ans = []

    class Node:
        def __init__(self, str, lp, rp):
            self.left = None
            self.right = None
            self.lp = lp
            self.rp = rp
            self.str = str
            if len(self.str) == 2 * n:
                ans.append(self.str)

    def doThings(node):
        # left
        if node.lp < n:
            node.left = Node(node.str + '(', node.lp + 1, node.rp)
            doThings(node.left)
        # right
        if node.rp < node.lp:
            node.right = Node(node.str + ')', node.lp, node.rp + 1)
            doThings(node.right)

    root = Node('', 0, 0)

    doThings(root)

    return ans


print(sol(4))
