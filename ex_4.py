class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = self._get_size(0, depth)
        self.Tree = [None] * tree_size # массив ключей

    def _get_size(self, size, depth):
        lvl_size = 2 ** depth + size
        if depth > 0:
            lvl_size = self._get_size(lvl_size, depth - 1)
        return lvl_size
        
	
    def FindKeyIndex(self, key):
        if len(self.Tree) == 1 and self.Tree[0] is None:
            return None
        # if len(self.Tree) == 1 and self.Tree[0] == key:
        #     return 0
        return self._FindKeyIndex(0, key)
        # ищем в массиве индекс ключа

    
    def _FindKeyIndex(self, index, key):
        if index >= len(self.Tree):
            return None
        if key == self.Tree[index]:
            return index
        if key < self.Tree[index] and not self.is_left_empty(index):
            return self._FindKeyIndex(self._get_leftchild_of(index), key)
        # if key < self.Tree[index] and self.is_next_lvl(index) and self.is_left_empty(index):
        if key < self.Tree[index] and self.is_left_empty(index):
            return -self._get_leftchild_of(index)
        if key > self.Tree[index] and not self.is_right_empty(index):
            return self._FindKeyIndex(self._get_rightchild_of(index), key)
        if key > self.Tree[index] and self.is_right_empty(index):
            return -self._get_rightchild_of(index)


        
	
    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index > 0:
            return index
        if index < 0:
            self.Tree[-index] = key
            return -index

        # индекс добавленного/существующего ключа или -1 если не удалось

    def _get_parent_of(self, idx):
        return (idx - 1) // 2
    
    def _get_leftchild_of(self, idx):
        return 2 * idx + 1
    
    def _get_rightchild_of(self, idx):
        return 2 * idx + 2
    
    def is_next_lvl(self, idx):
        return self._get_rightchild_of(idx) < len(self.Tree)
    
    def is_left_empty(self, idx):
        return self.Tree[self._get_leftchild_of(idx)] is None
    
    def is_right_empty(self, idx):
        return self.Tree[self._get_rightchild_of(idx)] is None
