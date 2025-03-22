class sorter:
    def __init__(self, nums):
        self.nums = nums
        self.partitioning = None
        self.i, self.j, self.pivot = 0, 0, None
        self.current_merge = None
        self.stack = [(0, len(nums) - 1)]
        self.merging = []
        self.merge_steps = []
        self.return_idxs = []
        self.left_part = []
        self.right_part = []
        self.sorteds = []
        self.min_idx = 0
        self.pivot_idx = 0
        self.key = None

    def swap(self, i, j):
        try:
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        except IndexError:
            print(len(self.nums)-1, i, j)
    
    def sort_type(self, type):
        match type:
            case "B": return self.bubble_sort()
            case "I": return self.insertion_sort()
            case "S": return self.selection_sort()
            case "Q": return self.quick_sort()

    def bubble_sort(self):
        if self.i < len(self.nums) - 1:
            if self.j < len(self.nums) - 1 - self.i:
                if self.nums[self.j] > self.nums[self.j + 1]:
                    self.swap(self.j, self.j + 1)
                    self.return_idxs = [self.j, self.j+1]
                self.j += 1
            else:
                self.j = 0
                self.i += 1
        self.return_idxs.append("B")
        return self.nums, self.return_idxs

    def insertion_sort(self):
        if self.j == self.i:
            self.key = self.nums[self.i]
            self.j = self.i - 1

        if self.j >= 0 and self.key < self.nums[self.j]:
            self.nums[self.j + 1] = self.nums[self.j]
            self.j -= 1
            self.return_idxs = [self.j + 1, self.j, "I"]
        else:
            self.nums[self.j + 1] = self.key
            self.return_idxs = [self.j + 1, self.j, "I"]
            self.i += 1
            self.j = self.i

        return self.nums, self.return_idxs

    def selection_sort(self):
        n = len(self.nums)
        if self.min_idx < n - 1:
            if self.j < n:
                if self.nums[self.j] < self.nums[self.min_idx]:
                    self.min_idx = self.j
                
                self.return_idxs = [self.j, self.min_idx, "S"]
                self.j += 1

            if self.j == n:
                self.swap(self.min_idx, self.i)
                self.i += 1
                self.j = self.i
                self.min_idx = self.i
                self.return_idxs = [self.min_idx, self.i-1, "S"]

        return self.nums, self.return_idxs

    def quick_sort(self):
        if not self.partitioning and self.stack:
            low, high = self.stack.pop()
            if low < high:
                self.partitioning = (low, high)
                self.i, self.j, self.pivot = low - 1, low, self.nums[high]

        if self.partitioning:
            low, high = self.partitioning
            if self.j < high:
                if self.nums[self.j] <= self.pivot:
                    self.i += 1
                    self.return_idxs = [i for i in range(low, high)]
                    self.swap(self.i, self.j)
                self.j += 1

                if self.nums.index(self.pivot) not in self.return_idxs: self.return_idxs.append(self.nums.index(self.pivot))
                self.return_idxs.append(self.sorteds)
                self.return_idxs.append("Q")
                return self.nums, self.return_idxs # Pause after each swap
            
            # Final swap: Move pivot to correct place
            self.swap(high, self.i+1)
            self.pivot_index = self.i + 1
            if self.pivot_index not in self.sorteds: self.sorteds.append(self.pivot_index)
            self.partitioning = None  # Partitioning done
            
            # Push new partitions onto stack
            self.stack.append((self.pivot_index + 1, high))
            self.stack.append((low, self.pivot_index - 1))
        
        if self.i + 1 not in self.return_idxs: self.return_idxs.append(self.i + 1)

        for i in range(1, 24):
            if i+1 in self.sorteds and i-1 in self.sorteds and i not in self.sorteds:
                self.sorteds.append(i)
        if 1 in self.sorteds and 0 not in self.sorteds: self.sorteds.append(0)
        if 23 in self.sorteds and 24 not in self.sorteds: self.sorteds.append(24)

        self.return_idxs.append(self.sorteds)
        self.return_idxs.append("Q")

        return self.nums, self.return_idxs
