class sorter:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(self.nums)
    
    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def bubble_sort(self, i):
        for j in range(self.n):
            if self.nums[i] > self.nums[j]:
                self.swap(i, j)
        return self.nums

    def insertion_sort(self, i):
        pass