import pygame # type: ignore
import colors

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
        self.function = func

    def run(self):
        self.collision_check()
        pygame.draw.rect(self.screen, colors.WHITE, self.box_rect, self.width)
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
        
