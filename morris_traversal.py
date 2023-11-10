"""

Algorithm in plain english

current = root
while ( root != null):
    if current.left == null:
        visit(current)
        current = current's right
    else:
        # left of the current exists
        predecessor = current.left
        if predecessor.right is null
            predecessor.right = current
            current = current.left
        else:
            predecessor.right = null
            visit(current)
            current = current.right
visit(node):
print(node)
"""