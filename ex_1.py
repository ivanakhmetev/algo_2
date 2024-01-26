class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        node = SimpleTreeNode(NewChild, ParentNode)
        ParentNode.Children.append(NewChild)

        # pass # ваш код добавления нового дочернего узла существующему ParentNode
  
    def DeleteNode(self, NodeToDelete):
        pass # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return []

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []
   
    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        pass  
   
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
        leaf_count = 0
        nodes = self.Root.Children
        if len(nodes) > 0:
            leaf_count = self._LeafCount(leaf_count, nodes)
        return leaf_count
    
    def _LeafCount(self, leaf_count: int, nodes: list):
        for n in nodes:
            if len(n.Children) == 0:
                leaf_count += 1
            if len(n.Children) > 0:
                leaf_count = self._LeafCount(leaf_count, n.Children)
        return leaf_count
            
            


