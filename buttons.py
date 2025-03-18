import pygame # type: ignore
import colors

class Button:
    def __init__(self, screen, loc, width, name, color, func, button_img = None):
        self.screen = screen
        self.location = loc
        self.width = width
        self.bold_width = self.width + 3
        self.width_copy = width
        self.name = name
        self.color = color
        self.name_rect = self.name.get_rect()
        self.box_rect = self.name.get_rect()
        self.name_size = self.name_rect.size
        self.box_rect.size = (self.name_size[0] + 10, self.name_size[1] + 7)
        self.name_rect.center = self.location
        self.box_rect.center = self.name_rect.center
        self.function = func
        if button_img:
            self.img = button_img
            self.box_rect.size = (self.box_rect.size[0] + 17, self.box_rect.size[1] + 2)
            self.box_rect.center = self.name_rect.center
            self.img = pygame.transform.smoothscale(self.img, self.box_rect.size)

    def run(self):
        self.collision_check()
        if self.img:
            self.screen.blit(self.img, self.box_rect)
            self.screen.blit(self.name, self.name_rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.box_rect, self.width)
            self.screen.blit(self.name, self.name_rect)

    def collision_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if abs(mouse_pos[0] - self.location[0]) < self.box_rect.size[0] // 2 and abs(
                mouse_pos[1] - self.location[1]) < self.box_rect.size[1] // 2:
            if self.img:
                pygame.draw.rect(self.screen, pygame.Color(200, 200, 200, a = 255), self.box_rect, 0, 10)
            else:
                self.width = self.bold_width
            return True
        else:
            if self.img:
                pass
            else:
                self.width = self.width_copy
            return False
        
