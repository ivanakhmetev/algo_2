class Heap:

    def __init__(self):
        self.HeapArray = []
		
    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * self._get_size(0, depth)
        tmp = sorted(a, reverse=True)
        self.HeapArray[ : len(tmp)] = tmp

    def GetMax(self):
        if len(self.HeapArray) == 0:
	        return -1
        max_val = self.HeapArray[0]
        last_idx = self._find_last_existing()
        self._switch(0, last_idx)
        self._GetMax(0)
        return max_val
    
    def _GetMax(self, parent_idx):
        if self._is_switch_need(parent_idx):
            child_to_switch = self._max_child_idx(parent_idx)
            self._switch(parent_idx, child_to_switch)
            self._GetMax(child_to_switch)

    def Add(self, key):
        last_none = self._find_last_none()
        if last_none == -1:
	        return False
        self.HeapArray[last_none] = key
        self._Add(last_none)

    def _Add(self, child_idx):
        parent = self._get_parent_of(child_idx)
        if self._is_upward_need(child_idx):
            self._switch(child_idx, parent)
            self._Add(parent)


    def _get_size(self, size, depth):
        lvl_size = 2 ** depth + size
        if depth > 0:
            lvl_size = self._get_size(lvl_size, depth - 1)
        return lvl_size
    
    def _find_last_existing(self):
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is not None:
                return i
        return -1
    
    def _find_last_none(self):
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is None:
                return i
        return -1
    
    def _switch(self, i, j):
        tmp = self.HeapArray[i]
        self.HeapArray[i] = self.HeapArray[j]
        self.HeapArray[j] = tmp

    def _get_leftchild_of(self, idx):
        return 2 * idx + 1
    
    def _get_rightchild_of(self, idx):
        return 2 * idx + 2
    
    def _get_parent_of(self, idx):
        return (idx - 1) // 2
    
    def _max_child_idx(self, parent_idx):
        left_child = self._get_leftchild_of(parent_idx)
        right_child = self._get_rightchild_of(parent_idx)
        max_value = max(self.HeapArray[left_child], self.HeapArray[right_child])
        if max_value == self.HeapArray[left_child]:
            return left_child
        return right_child
    
    def _is_switch_need(self, parent_idx):
        left_child = self._get_leftchild_of(parent_idx)
        right_child = self._get_rightchild_of(parent_idx)
        if left_child >= len(self.HeapArray) and right_child >= len(self.HeapArray):
            return False
        max_value = max(self.HeapArray[left_child], self.HeapArray[right_child])
        if max_value < self.HeapArray[parent_idx]:
            return False
        return True
    
    def _is_upward_need(self, child_idx):
        if child_idx == 0:
            return False
        parent = self._get_parent_of(child_idx)
        if self.HeapArray[parent] > self.HeapArray[child_idx]:
            return False
        return True
         
            
    
