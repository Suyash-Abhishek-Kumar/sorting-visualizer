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

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def bubble_sort(self):
        if self.i < len(self.nums) - 1:
            if self.j < len(self.nums) - 1 - self.i:
                if self.nums[self.j] > self.nums[self.j + 1]:
                    self.swap(self.j, self.j + 1)
                    self.return_idxs = [self.j, self.j+1]
                self.j += 1  # Move to next comparison
            else:
                self.j = 0  # Reset comparison index
                self.i += 1  # Move to next pass
        self.return_idxs.append("B")
        return self.nums, self.return_idxs

    def insertion_sort(self):
        key = self.nums[self.i]
        j = self.i-1
        while j >= 0 and key < self.nums[j]:
            self.nums[j+1] = self.nums[j]
            j-=1
        self.nums[j+1] = key
        self.return_idxs = [j+1, self.i+1]
        self.return_idxs.append("I")
        self.i += 1
        return self.nums, self.return_idxs

    def merge_sort(self):
        # Step 1: Divide the array into subarrays
        if not self.merge_steps and self.stack:
            left, right = self.stack.pop()
            if left < right:
                mid = (left + right) // 2
                self.stack.append((left, mid))
                self.stack.append((mid + 1, right))
                self.merge_steps.append((left, mid, right))  # Store merge step
                return self.nums, []  # Return early to prevent instant merging

        # Step 2: Merge progressively
        if self.merge_steps:
            if not self.current_merge:  # Start new merge
                left, mid, right = self.merge_steps.pop(0)
                self.current_merge = {
                    "left_idx": 0,
                    "right_idx": 0,
                    "left": self.nums[left:mid + 1],
                    "right": self.nums[mid + 1:right + 1],
                    "merge_idx": left,
                    "end": right
                }

            merge = self.current_merge
            if merge["left_idx"] < len(merge["left"]) and (merge["right_idx"] >= len(merge["right"]) or merge["left"][merge["left_idx"]] <= merge["right"][merge["right_idx"]]):
                self.nums[merge["merge_idx"]] = merge["left"][merge["left_idx"]]
                merge["left_idx"] += 1
            elif merge["right_idx"] < len(merge["right"]):
                self.nums[merge["merge_idx"]] = merge["right"][merge["right_idx"]]
                merge["right_idx"] += 1

            # Highlight merging index
            self.return_idxs = [merge["merge_idx"]]
            merge["merge_idx"] += 1

            # Finish merge when all elements are merged
            if merge["merge_idx"] > merge["end"]:
                self.current_merge = None  # Reset for next merge

        return self.nums, self.return_idxs

    def quick_sort(self):
        if not self.partitioning and self.stack:
            low, high = self.stack.pop()
            print(f"({low}, {high}) popped")
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
                self.return_idxs.append("Q")
                return self.nums, self.return_idxs # Pause after each swap
            
            # Final swap: Move pivot to correct place
            self.swap(high, self.i+1)
            pivot_index = self.i + 1
            self.partitioning = None  # Partitioning done
            
            # Push new partitions onto stack
            self.stack.append((pivot_index + 1, high))
            self.stack.append((low, pivot_index - 1))
            print(f"({pivot_index + 1}, {high}) appended")
            print(f"({low}, {pivot_index - 1}) appended")
        
        if self.i + 1 not in self.return_idxs: self.return_idxs.append(self.i + 1)
        self.return_idxs.append("Q")
        return self.nums, self.return_idxs
