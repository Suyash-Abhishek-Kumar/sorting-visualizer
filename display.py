import pygame # type: ignore
import colors
from buttons import Button
from sorting_algorithms import sorter

pygame.init()

class Sort_Visualizer:
    def __init__(self, nums: int):
        self.w, self.h = 800, 800
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Sort Visualizer")
        self.clock = pygame.time.Clock()
        self.nums = self.scale_nums(nums)
        print("nums: ", self.nums)
        self.algo = sorter(self.nums)
        self.height_multiplier = 360 / max(self.nums)
        self.width = 350 / len(self.nums)

    def display(self):
        i, j = 0, 0
        print(self.nums)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(colors.SKY_BLUE)
            self.graph()
            if i < len(self.nums):
                self.nums = self.algo.bubble_sort(i)
                print(self.nums)
            j += 1
            if j%10 == 0:
                i += 1
            pygame.display.update()
            self.clock.tick(60)
    
    def graph(self):
        pygame.draw.rect(self.screen, colors.BLACK, [200, 100, 400, 300], 5)
        for i in range(len(self.nums)):
            pygame.draw.rect(self.screen, colors.ROYAL_BLUE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)

    def scale_nums(self, nums):
        max_num = max(nums)
        scale_factor = 270 // max_num
        return [num * scale_factor for num in nums]
    
    def input(self):
        #define input of nums and set width of each bar accordingly in the bar graph
        pass
        

nums = [2,8,34,4,23,13,46,6,12,40]
x = Sort_Visualizer(nums)
x.display()