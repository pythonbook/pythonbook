import tree_node

tree = tree_node.Node(10)
n7 = tree_node.Node(7)
n8 = tree_node.Node(8)
n9 = tree_node.Node(9)
n11 = tree_node.Node(11)
n12 = tree_node.Node(12)

tree.add_lchild(n8)
n8.add_lchild(n7)
n8.add_rchild(n9)
tree.add_rchild(n12)
n12.add_lchild(n11)

print('Pre-Order')
tree.pre_order()

print('In-Order')
tree.in_order()

print('Post-Order')
tree.post_order()

print('Breadth-First')
tree.breadth_first()
