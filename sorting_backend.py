import pygame # type: ignore
import colors
from buttons import Button
from sorting_algorithms import sorter

pygame.init()

class Sort_Visualizer:
    def __init__(self, nums: int):
        self.w, self.h = 800, 600
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Simple Pygame Window")
        self.clock = pygame.time.Clock()
        self.algo = sorter(nums)
        self.nums = nums

    def display(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(colors.scrolling(10))
            pygame.display.update()
            self.clock.tick(60)


nums = [2,8,34,4,23,13]
x = Sort_Visualizer(nums)
x.display()