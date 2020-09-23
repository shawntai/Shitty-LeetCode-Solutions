def sol(root):

    def depth(node):
        if node:
            deepest = 0
            for child in node.children:
                child_depth = depth(child)
                if child_depth > deepest:
                    deepest = child_depth
            return deepest + 1
        else:
            return 0

    return depth(root)


