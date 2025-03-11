import pygame # type: ignore

pygame.init()


class Colors:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.PURPLE = (255, 0, 255)
        self.BLUE = (0, 0, 255)
        self.SKY_BLUE = (0, 255, 255)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.WHITE = (255, 255, 255)
        self.ROYAL_BLUE = (100, 150, 255)
        self.PINK = (255, 155, 205)
        self.color = [0, 0, 255]
        self.cur = [0, 1]
    
    def scrolling(self, speed):
        for i in range(len(self.color)):
            if i == self.cur[0]: self.color[i] = min(255, self.color[i] + speed)
            elif i == self.cur[1]: self.color[i] = max(0, self.color[i] - speed)
            else: pass
            if self.color.count(255) == 2 and self.color.count(0) == 1:
                self.cur[0] = (self.cur[0] + 1) % 3
                self.cur[1] = (self.cur[1] + 1) % 3
        print(self.color)
        return self.color


class Button:
    def __init__(self, screen, loc, width, name, func):
        self.screen = screen
        self.location = loc
        self.width = width
        self.bold_width = self.width + 3
        self.width_copy = width
        self.name = name
        self.name_rect = self.name.get_rect()
        self.box_rect = self.name.get_rect()
        self.name_size = self.name_rect.size
        self.box_rect.size = (self.name_size[0] + 10, self.name_size[1] + 7)
        self.name_rect.center = self.location
        self.box_rect.center = self.location
        self.color = Colors()
        self.function = func

    def run(self):
        self.collision_check()
        pygame.draw.rect(self.screen, self.color.WHITE, self.box_rect, self.width)
        self.screen.blit(self.name, self.name_rect)

    def collision_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if abs(mouse_pos[0] - self.location[0]) < self.box_rect.size[0] // 2 and abs(
                mouse_pos[1] - self.location[1]) < self.box_rect.size[1] // 2:
            self.width = self.bold_width
            return True
        else:
            self.width = self.width_copy
            return False
        

class sort_algorithms:
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


class Sort_Visualizer:
    def __init__(self, nums: int):
        self.w, self.h = 800, 600
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Simple Pygame Window")
        self.clock = pygame.time.Clock()
        self.algo = sort_algorithms(nums)
        self.colors = Colors()
        self.nums = nums

    def display(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.colors.scrolling(10))
            pygame.display.update()
            self.clock.tick(60)


nums = [2,8,34,4,23,13]
x = Sort_Visualizer(nums)
x.display()