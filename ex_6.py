class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key 
        self.Parent = parent 
        self.LeftChild = None 
        self.RightChild = None 
        self.Level = 0
        
class BalancedBST:
		
    def __init__(self):
        self.Root = None 

    def GenerateTree(self, a):
        tmp = sorted(a)
        self.Root = self._GenerateTree(None, tmp, 0, len(a), 0)

    def _GenerateTree(self, parent, array, start, end, lvl):
        if start >= end:
            return
        center = start + (end - start) // 2
        center_node = BSTNode(array[center], parent)
        center_node.Level = lvl
        center_node.LeftChild = self._GenerateTree(center_node, array, start, center, lvl+1)
        center_node.RightChild = self._GenerateTree(center_node, array, center+1, end, lvl+1)
        return center_node
    
    def IsCorect(self, root):
        left_correct = True
        right_correct = True
        if root.LeftChild is not None and root.LeftChild.NodeKey < root.NodeKey:
            left_correct = self.IsCorect(root.LeftChild)
        if root.RightChild is not None and root.RightChild.NodeKey >= root.NodeKey:
            right_correct = self.IsCorect(root.RightChild)
        if root.LeftChild is not None and root.LeftChild.NodeKey > root.NodeKey:
            return False
        if root.RightChild is not None and root.RightChild.NodeKey < root.NodeKey:
            return False
        return left_correct and right_correct
    
    def IsTreeCorrect(self):
        return self.IsCorect(self.Root)
        

    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        left_h = self.Height(root_node.LeftChild)
        right_h = self.Height(root_node.RightChild)
        if abs(left_h - right_h) <= 1 and self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild):
            return True
        return False
    
    def Height(self, node):
        if node is None:
            return 0
        return max(self.Height(node.LeftChild), self.Height(node.RightChild)) + 1

