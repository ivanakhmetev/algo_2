'''algo_2 ex_1 general tree implementation'''

class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root
	
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == self.Root:
            return
        
        del NodeToDelete.Children[:]
        node_idx = NodeToDelete.Parent.Children.index(NodeToDelete)
        del NodeToDelete.Parent.Children[node_idx]
        return


    def GetAllNodes(self):
        all_nodes = [self.Root]
        nodes = self.Root.Children
        if len(nodes) > 0:
            all_nodes.extend(nodes)
            all_nodes = self._GetAllNodes(all_nodes, nodes)
        return all_nodes
    
    def _GetAllNodes(self, all_nodes: int, nodes: list):
        for n in nodes:
            num_children = len(n.Children)
            if num_children > 0:
                all_nodes.extend(n.Children)
                all_nodes = self._GetAllNodes(all_nodes, n.Children)
        return all_nodes



    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        found = []
        found = self._FindNodesByValue(found, [self.Root], val)
        return found
    
    def _FindNodesByValue(self, found, nodes, val):
        for n in nodes:
            if n.NodeValue == val:
                found.append(n)
        for n in nodes:
            if len(n.Children) != 0:
                self._FindNodesByValue(found, n.Children, val)            
        return found
   
    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        # количество всех узлов в дереве
        count = 1
        nodes = self.Root.Children
        if len(nodes) > 0:
            count += len(nodes)
            count = self._Count(count, nodes)
        return count
    
    def _Count(self, count: int, nodes: list):
        for n in nodes:
            num_children = len(n.Children)
            if num_children > 0:
                count += num_children
                count = self._Count(count, n.Children)
        return count

    def LeafCount(self):
        # количество листьев в дереве
        nodes = self.Root.Children
        if len(nodes) == 0:
            return 1
        if len(nodes) > 0:
            leaf_count = self._LeafCount(0, nodes)
        return leaf_count
    
    def _LeafCount(self, leaf_count: int, nodes: list):
        for n in nodes:
            if len(n.Children) == 0:
                leaf_count += 1
            if len(n.Children) > 0:
                leaf_count = self._LeafCount(leaf_count, n.Children)
        return leaf_count
            
            