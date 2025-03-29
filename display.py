import pygame # type: ignore
import colors
from random import shuffle
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
        self.regular_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 24)
        self.img = pygame.image.load('.\\graphics\\button_2.png').convert_alpha()
        self.buttons = [
            Button(self.screen, (550, 525), 3, "Sort", colors.BLACK, self.start, self.img),
            Button(self.screen, (550, 575), 3, "Shuffle", colors.BLACK, self.reset, self.img),
            # Button(self.screen, (550, 625), 3, "New Array", colors.BLACK, self.reset_full, self.img),
            Button(self.screen, (550, 675), 3, "Big Array", colors.BLACK, self.reset_full_big, self.img),
            Button(self.screen, (550, 725), 3, "Small Array", colors.BLACK, self.reset_full_small, self.img),
            Button(self.screen, (250, 500), 3, "Bubble Sort", colors.BLACK, self.B, self.img),
            Button(self.screen, (250, 550), 3, "Insertion Sort", colors.BLACK, self.I, self.img),
            Button(self.screen, (250, 600), 3, "Selection Sort", colors.BLACK, self.S, self.img),
            Button(self.screen, (250, 650), 3, "Quick Sort", colors.BLACK, self.Q, self.img),
            Button(self.screen, (250, 700), 3, "Merge Sort", colors.BLACK, self.M, self.img)
        ]
        self.width = 0
        self.nums = self.scale_nums(nums)
        self.length = len(self.nums)
        self.algo = sorter(self.nums)
        self.height_multiplier = 380 / max(self.nums)
        self.big_arr, self.small_arr = 128, 25
        self.idxs = []
        self.sorteds = []
        self.sorted = 0
        self.done = False
        self.algo_used = None
        self.begin = False
        self.go_fast = True
        self.selected_func = "B"
        self.final_green = self.final_green_speed()
    
    def start(self): self.begin = True
    def B(self): self.selected_func = "B"
    def I(self): self.selected_func = "I"
    def S(self): self.selected_func = "S"
    def Q(self): self.selected_func = "Q"
    def M(self): self.selected_func = "M"

    def display(self):
        running = True
        reset_yet = False
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
            self.screen.fill(colors.update_brightness(colors.BLACK, 100))
            self.graph()
            if self.begin:
                if self.nums != sorted(self.nums):
                    self.nums, self.idxs = self.algo.sort_type(self.selected_func, self.go_fast)
                    if type(self.idxs[-1]) == str:
                        self.algo_used = self.idxs.pop()
                    if self.algo_used == "Q":
                        self.sorteds = self.idxs.pop()
                        pivot = self.idxs.pop()
                        self.idxs = list(set(self.idxs))
                        self.idxs.append(pivot)
                elif self.algo_used == "M" and self.idxs[-1] == self.length - 1 and not reset_yet:
                    self.done = True
                    reset_yet = True
                    self.idxs = [0]
                elif not self.idxs or self.idxs[0]!=0:
                    self.done = True
                    self.idxs = [0]
                else:
                    if len(self.idxs) < len(self.nums):
                        for i in range(self.final_green):
                            self.idxs.append(self.idxs[-1] + 1)
            for i in self.buttons:
                i.run()
            pygame.display.update()
            self.clock.tick(10)
    
    def graph(self):
        pygame.draw.rect(self.screen, colors.WHITE, [200, 100, 400, 300], 0)
        pygame.draw.rect(self.screen, colors.BLACK, [200, 100, 400, 300], 5)
        for i in range(len(self.nums)):
            if i not in self.idxs:
                pygame.draw.rect(self.screen, colors.ROYAL_BLUE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            elif not self.done and self.algo_used == "Q" and i == self.idxs[-1]:
                pygame.draw.rect(self.screen, colors.PURPLE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
                self.idxs.pop(self.idxs.index(i))
            elif not self.done and self.algo_used == "S" and i == self.idxs[-1]:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.ORANGE, -100), [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            elif not self.done:
                pygame.draw.rect(self.screen, colors.ORANGE, [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            else:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.GREEN, 100), [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)
            if not self.done and self.algo_used == "Q" and i in self.sorteds:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.ORANGE, -100), [210 + self.width * i * 1.1, 395 - self.nums[i], self.width, self.nums[i]], 0)

    def scale_nums(self, nums):
        max_num = max(nums)
        scale_factor = 270 / max_num
        self.width = 345 / len(nums)
        return [num * scale_factor for num in nums]

    def final_green_speed(self):
        final_green = self.length // 50
        if final_green == 0: self.final_green = 1
        return final_green
    
    def reset(self):
        shuffle(self.nums)
        self.idxs = []
        self.sorted = 0
        self.done = False
        self.algo_used = None
        self.begin = False
        self.algo = sorter(self.nums)
    
    def reset_full(self):
        nums = [randint(5, 105) for _ in range(self.length)]
        self.nums = self.scale_nums(nums)
        self.idxs = []
        self.sorted = 0
        self.done = False
        self.algo_used = None
        self.begin = False
        self.algo = sorter(self.nums)

    def reset_full_big(self):
        nums = [randint(5, 105) for _ in range(self.big_arr)]
        self.length = self.big_arr
        self.nums = self.scale_nums(nums)
        self.idxs = []
        self.sorted = 0
        self.go_fast = True
        self.done = False
        self.algo_used = None
        self.begin = False
        self.algo = sorter(self.nums)

    def reset_full_small(self):
        nums = [randint(5, 105) for _ in range(self.small_arr)]
        self.length = self.small_arr
        self.nums = self.scale_nums(nums)
        self.idxs = []
        self.sorted = 0
        self.go_fast = False
        self.done = False
        self.algo_used = None
        self.begin = False
        self.algo = sorter(self.nums)

nums = [randint(5, 105) for _ in range(100)]
x = Sort_Visualizer(nums)
x.display()