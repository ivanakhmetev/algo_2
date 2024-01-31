from ex_1 import SimpleTree, SimpleTreeNode

root = SimpleTreeNode(9, None)

l1 = SimpleTreeNode(4, root)
r1 = SimpleTreeNode(17, root)
root.Children.append(l1)
root.Children.append(r1)
l2l = SimpleTreeNode(3, l1)
l2r = SimpleTreeNode(6, l1)
l1.Children.append(l2l)
l1.Children.append(l2r)
l3l = SimpleTreeNode(5, l2r)
l3r = SimpleTreeNode(7, l2r)
l2r.Children.append(l3l)
l2r.Children.append(l3r)

r2 = SimpleTreeNode(22, r1)
r1.Children.append(r2)
r3 = SimpleTreeNode(20, r2)
r2.Children.append(r3)


my_tree = SimpleTree(root)
# print(my_tree.LeafCount())
# print(my_tree.Count())
a = my_tree.GetAllNodes()
for el in a:
    print (el.NodeValue)