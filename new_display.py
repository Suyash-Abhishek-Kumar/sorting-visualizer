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
        self.tiny_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 15)
        self.small_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 20)
        self.regular_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 24)
        self.head_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 30)
        self.img = pygame.image.load('.\\graphics\\button_2.png').convert_alpha()
        self.ui_bg_color = colors.update_brightness(colors.DARK_NAVY_BLUE, 20)
        self.ui_bg_color_selected = colors.update_brightness(colors.ROYAL_BLUE, 30)
        self.button_color = (130, 150, 255)
        self.buttons = [
            Button(self.screen, (590, 35), 3, "Sort", self.start, colors.WHITE, fixed_size=(100, 20), button_color=self.button_color, hover="darken"),
            Button(self.screen, (710, 35), 3, "Shuffle", self.reset, colors.WHITE, fixed_size=(100, 20), button_color=self.button_color, hover="darken"),
            Button(self.screen, (590, 65), 3, "Big Array", self.reset_full_big, colors.WHITE, fixed_size=(100, 20), button_color=self.button_color, hover="darken"),
            Button(self.screen, (710, 65), 3, "Small Array", self.reset_full_small, colors.WHITE, fixed_size=(100, 20), button_color=self.button_color, hover="darken"),
            Button(self.screen, (480, 440), 3, "Bubble Sort", self.B, colors.WHITE, fixed_size=(100, 40), button_color=self.button_color, hover="darken"),
            Button(self.screen, (515, 490), 3, "Insertion Sort", self.I, colors.WHITE, fixed_size=(140, 40), button_color=self.button_color, hover="darken"),
            Button(self.screen, (675, 490), 3, "Selection Sort", self.S, colors.WHITE, fixed_size=(140, 40), button_color=self.button_color, hover="darken"),
            Button(self.screen, (595, 440), 3, "Quick Sort", self.Q, colors.WHITE, fixed_size=(100, 40), button_color=self.button_color, hover="darken"),
            Button(self.screen, (710, 440), 3, "Merge Sort", self.M, colors.WHITE, fixed_size=(100, 40), button_color=self.button_color, hover="darken")
        ]
        self.speed_slider = Slider(self.screen, (400, 50), 150, 10, 1, 60, 30, colors.GRAY, self.ui_bg_color_selected, "Speed")
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
        self.current_speed = 30
        self.comparisions = 0
        self.swaps = 0
        self.time = 0
        self.done = False
        self.can_tick = False
        self.algo_used = None
        self.begin = False
        self.go_fast = True
        self.selected_func = "B"
        self.final_green = self.final_green_speed()
    
    def start(self):
        self.begin = True
        self.can_tick = True
        self.time = 0
    def B(self): self.selected_func = "B"
    def I(self): self.selected_func = "I"
    def S(self): self.selected_func = "S"
    def Q(self): self.selected_func = "Q"
    def M(self): self.selected_func = "M"

    def display_new(self):
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
                self.speed_slider.handle_event(event)
            self.screen.fill(colors.DARK_NAVY_BLUE)
            self.background_boxes()
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
                    self.can_tick = False
                    self.done = True
                    reset_yet = True
                    self.idxs = [0]
                elif not self.idxs or self.idxs[0]!=0:
                    self.can_tick = False
                    self.done = True
                    self.idxs = [0]
                else:
                    if len(self.idxs) < len(self.nums):
                        for i in range(self.final_green):
                            self.idxs.append(self.idxs[-1] + 1)
                if self.can_tick: self.time += 1
            self.speed_slider.run()
            for i in self.buttons:
                i.run()
            self.current_speed = self.speed_slider.get_value()
            pygame.display.update()
            self.clock.tick(self.current_speed)
    
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
    
    def background_boxes(self):
        #draw boxes
        pygame.draw.rect(self.screen, self.ui_bg_color, [20, 20, 760, 60], 0, 6)
        pygame.draw.rect(self.screen, self.ui_bg_color, [20, 100, 760, 250], 0, 6)
        pygame.draw.rect(self.screen, self.ui_bg_color, [20, 370, 370, 160], 0, 6)
        pygame.draw.rect(self.screen, self.ui_bg_color, [410, 370, 370, 160], 0, 6)

        #draw text
        heading = self.head_font.render("Sorting Visualizer", False, colors.WHITE)
        algo = self.small_font.render("Algorithm: ", False, colors.WHITE)
        stat = self.small_font.render("Statistics: ", False, colors.WHITE)
        comparison = self.tiny_font.render("Comparisons: " + str(self.comparisions), False, colors.WHITE)
        swaps = self.tiny_font.render("Swaps: " + str(self.swaps), False, colors.WHITE)
        time = self.tiny_font.render("Time: " + str(round(self.time/self.current_speed, 2)), False, colors.WHITE)

        headbox = heading.get_rect()
        algobox = algo.get_rect()
        statbox = stat.get_rect()
        comparisonbox = comparison.get_rect()
        swapbox = swaps.get_rect()
        timebox = time.get_rect()

        headbox.midleft = (30, 50)
        algobox.midleft = (420, 390)
        statbox.midleft = (30, 390)
        comparisonbox.midleft = (30, 440)
        swapbox.midleft = (30, 460)
        timebox.midleft = (30, 480)

        self.screen.blit(algo, algobox)
        self.screen.blit(stat, statbox)
        self.screen.blit(comparison, comparisonbox)
        self.screen.blit(heading, headbox)
        self.screen.blit(swaps, swapbox)
        self.screen.blit(time, timebox)

        #draw lines
        pygame.draw.line(self.screen, colors.WHITE, (420, 410), (770, 410), 1)
        pygame.draw.line(self.screen, colors.WHITE, (30, 410), (380, 410), 1)

    def scale_nums(self, nums):
        max_num = max(nums)
        scale_factor = 230 / max_num
        self.width = 675 / len(nums)
        return [num * scale_factor for num in nums]

    def final_green_speed(self):
        final_green = self.length // 50
        if final_green == 0: final_green = 1
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
        self.final_green = self.final_green_speed()

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
        self.final_green = self.final_green_speed()

nums = [randint(5, 105) for _ in range(100)]
x = Sort_Visualizer(nums)
x.display_new()