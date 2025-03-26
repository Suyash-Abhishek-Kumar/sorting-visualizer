class sorter:
    def __init__(self, nums):
        self.nums = nums
        self.partitioning, self.area = None, None
        self.i, self.j, self.pivot = 0, 0, None
        self.mi, self.mj = 0, 0
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
        self.step = 1
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
            case "M": return self.old_merge_sort()

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

    def m_insertion_sort(self, low):
        if self.j == self.i:
            self.j = self.i - 1

        if self.j >= low and self.key < self.nums[self.j]:
            self.nums[self.j + 1] = self.nums[self.j]
            self.j -= 1
            self.return_idxs = [self.j + 1, self.j, "I"]
        else:
            print(self.key, self.j+1, len(self.nums))
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

    def old_merge_sort(self):
        length = len(self.nums)

        if self.step < length:  # Check if sorting is still in progress
            if self.i < length:
                self.left_part = self.nums[self.i : self.i + self.step]
                self.right_part = self.nums[self.i + self.step : self.i + 2 * self.step]

                merged = []
                li, ri = 0, 0

                # Merge left_part and right_part
                while li < len(self.left_part) and ri < len(self.right_part):
                    if self.left_part[li] < self.right_part[ri]:
                        merged.append(self.left_part[li])
                        li += 1
                    else:
                        merged.append(self.right_part[ri])
                        ri += 1

                # Add remaining elements
                merged.extend(self.left_part[li:])
                merged.extend(self.right_part[ri:])

                # Copy back to self.nums
                self.nums[self.i:self.i + len(merged)] = merged
                self.return_idxs = [i for i in range(self.i, self.i + len(merged))]
                self.return_idxs.append("M")

                # Move to the next pair of subarrays
                self.i += 2 * self.step
            else:
                self.i = 0  # Reset for next step
                self.step *= 2  # Increase merge size
                self.return_idxs = ["M"]
        return self.nums, self.return_idxs

    def merge_sort(self):
        if self.stack and not self.area:
            self.area = self.stack.pop()
            self.i, self.j = self.area
        
        if self.area:
            low, high = self.area
            if high-low == 1:
                self.nums[high] = max(self.nums[high], self.nums[low])
                self.nums[low] = min(self.nums[high], self.nums[low])
                self.return_idxs = [high, low, "M"]
            else:
                mid = (low + high)//2
                lhf = (low, mid)
                rhf = (mid+1, high)
                if lhf not in self.stack and rhf not in self.stack:
                    self.stack.append((low, mid))
                    self.stack.append((mid+1, high))
                    self.return_idxs = ["M"]
                else:
                    print(low, high)
                    self.key =  self.nums[high]
                    self.m_insertion_sort(low)

        return self.nums, self.return_idxs
