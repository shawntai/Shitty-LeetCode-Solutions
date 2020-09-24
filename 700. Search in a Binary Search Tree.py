def sol(root, val):
    if root.val == val:
        return root
    sol(root.left, val)
    sol(root.right, val)
    return None