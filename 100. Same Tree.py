class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def sol(p, q):
    queue = [p, q]
    while len(queue) != 0:
        q = queue.pop()
        p = queue.pop()
        if not p and not q:
            continue
        if (not p and q) or (not q and p) or p.val != q.val:
            return False
        queue += [p.left, q.left, p.right, q.right]

    return True


n2 = TreeNode(2, None, None)
n3 = TreeNode(3, None, None)
root = TreeNode(1, n2, n3)

sol(root, root)