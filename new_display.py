import pygame # type: ignore
import colors
from slider import Slider
from random import shuffle
from buttons import Button
from random import randint
from sorting_algorithms import sorter

pygame.init()

class Sort_Visualizer:
    def __init__(self, nums):
        self.w, self.h = 800, 550
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
        self.speed_slider = Slider(self.screen, (550, 550), 200, 10, 1, 100, 50, colors.GRAY, colors.BLUE, "Speed")
        self.width = 0
        self.nums = self.scale_nums(nums)
        self.length = len(self.nums)
        self.algo = sorter(self.nums)
        self.height_multiplier = 380 / max(self.nums)
        self.big_arr, self.small_arr = 128, 25
        self.idxs = []
        self.sorteds = []
        self.graph_start = 30
        self.sorted = 0
        self.done = False
        self.algo_used = None
        self.begin = False
        self.go_fast = True
        self.selected_func = "B"
        self.ui_bg_color = colors.update_brightness(colors.DARK_NAVY_BLUE, 20)
        self.final_green = self.final_green_speed()
    
    def start(self): self.begin = True
    def B(self): self.selected_func = "B"
    def I(self): self.selected_func = "I"
    def S(self): self.selected_func = "S"
    def Q(self): self.selected_func = "Q"
    def M(self): self.selected_func = "M"

    def display_new(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(colors.DARK_NAVY_BLUE)
            self.graph()
            pygame.display.update()
            self.clock.tick(60)
    
    def graph(self):
        pygame.draw.rect(self.screen, self.ui_bg_color, [20, 100, 760, 250], 0, 6)
        for i in range(len(self.nums)):
            if i not in self.idxs:
                pygame.draw.rect(self.screen, colors.ROYAL_BLUE, [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)
            elif not self.done and self.algo_used == "Q" and i == self.idxs[-1]:
                pygame.draw.rect(self.screen, colors.PURPLE, [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)
                self.idxs.pop(self.idxs.index(i))
            elif not self.done and self.algo_used == "S" and i == self.idxs[-1]:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.ORANGE, -100), [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)
            elif not self.done:
                pygame.draw.rect(self.screen, colors.ORANGE, [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)
            else:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.GREEN, 100), [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)
            if not self.done and self.algo_used == "Q" and i in self.sorteds:
                pygame.draw.rect(self.screen, colors.update_brightness(colors.ORANGE, -100), [self.graph_start + self.width * i * 1.1, 345 - self.nums[i], self.width, self.nums[i]], 0)

    def scale_nums(self, nums):
        max_num = max(nums)
        scale_factor = 230 / max_num
        self.width = 675 / len(nums)
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
x.display_new()