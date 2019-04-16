class binaryPriorityQ():
    '''
    The input entry is constructed by
    [priority, node, parent_node]
    '''

    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def insert(self, element):
        self.array.append(element)
        self.size += 1
        self.swim(self.size - 1)

    def exchange(self, idx1, idx2):
        temp = self.array[idx1].copy()
        self.array[idx1] = self.array[idx2]
        self.array[idx2] = temp

    def isLarge(self, idx1, idx2):
        return self.array[idx1][0] > self.array[idx2][0]

    def peek(self):
        if self.size != 0:
            return self.array[0]

    def pop(self):
        element = self.array[0]
        self.exchange(0, - 1)
        del self.array[-1]
        self.size -= 1
        self.sink(0)
        return element

    def swim(self, idx):
        while idx > 0 and self.isLarge(math.floor((idx - 1) / 2), idx):
            self.exchange(idx, math.floor((idx - 1) / 2))
            idx = math.floor((idx - 1) / 2)

    def sink(self, idx):
        while 2 * idx + 1 < self.size:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            small_child_idx = left_child_idx
            if right_child_idx < self.size and self.array[right_child_idx] < self.array[left_child_idx]:
                small_child_idx = right_child_idx
            if not self.isLarge(idx, small_child_idx): break
            self.exchange(idx, small_child_idx)
            idx = small_child_idx

    def sort(self):
        for item in self.array:
            self.sink(item)