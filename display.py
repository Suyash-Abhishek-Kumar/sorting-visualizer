import pygame # type: ignore
import colors
from buttons import Button
from random import randint
from sorting_algorithms import sorter

pygame.init()

class Sort_Visualizer:
    def __init__(self, nums):
        self.w, self.h = 800, 800
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Sort Visualizer")
        self.clock = pygame.time.Clock()
        self.nums = self.scale_nums(nums)
        self.regular_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 24)
        self.buttons = [Button(self.screen, (100, 600), 3, self.regular_font.render("Sort", False, colors.BLACK), colors.BLACK, self.start)]
        self.algo = sorter(self.nums)
        self.height_multiplier = 380 / max(self.nums)
        self.width = 345 / len(self.nums)
        self.idxs = []
        self.sorted = 0
        self.done = False
        self.algo_used = None
        self.begin = False
    
    def start(self): self.begin = True

    def display(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for j in self.buttons:
                            if j.collision_check():
                                j.function()
                                continue
            self.screen.fill(colors.WHITE)
            self.graph()
            if self.begin:
                if self.nums != sorted(self.nums):
                    self.nums, self.idxs = self.algo.quick_sort()
                    if type(self.idxs[-1]) == str:
                        self.algo_used = self.idxs.pop()
                    if self.algo_used == "Q":
                        pivot = self.idxs.pop()
                        self.idxs = list(set(self.idxs))
                        self.idxs.append(pivot)
                elif self.idxs[0]!=0:
                    self.done = True
                    self.idxs = [0]
                else:
                    if len(self.idxs) < len(self.nums):
                        print(self.idxs)
                        self.idxs.append(self.idxs[-1] + 1)
            for i in self.buttons:
                i.run()
            pygame.display.update()
            self.clock.tick(10)
    
    def graph(self):
        pygame.draw.rect(self.screen, colors.BLACK, [200, 100, 400, 300], 5)
        for i in range(len(self.nums)):
            if i not in self.idxs:
                pygame.draw.rect(self.screen, colors.ROYAL_BLUE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            elif not self.done and self.algo_used == "Q" and i == self.idxs[-1]:
                pygame.draw.rect(self.screen, colors.PURPLE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
                self.idxs.pop(self.idxs.index(i))
            elif not self.done:
                pygame.draw.rect(self.screen, colors.ORANGE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            else:
                pygame.draw.rect(self.screen, colors.GREEN, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)

    def scale_nums(self, nums):
        max_num = max(nums)
        scale_factor = 270 / max_num
        return [num * scale_factor for num in nums]
    
    def input(self):
        #define input of nums and set width of each bar accordingly in the bar graph
        pass
        

nums = [randint(5, 105) for _ in range(25)]
print(nums)
x = Sort_Visualizer(nums)
x.display()