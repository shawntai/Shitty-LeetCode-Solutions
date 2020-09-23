def sol(root):
    if root:
        deepest = 0
        for child in root.children:
            child_depth = sol(child)
            if child_depth > deepest:
                deepest = child_depth
        return deepest + 1
    else:
        return 0


