import pygame # type: ignore
import colors

class Slider:
    def __init__(self, screen, loc, width, height, min_val, max_val, init_val, color, handle_color, label=None):
        self.screen = screen
        self.location = loc  # Center position of the slider
        self.width = width   # Width of the slider track
        self.height = height # Height of the slider track
        self.min_val = min_val
        self.max_val = max_val
        self.value = init_val
        self.color = color
        self.handle_color = handle_color
        self.dragging = False
        self.regular_font = pygame.font.Font(".\\basic_types\\Roboto-Medium.ttf", 14)
        
        # Calculate rectangles
        self.track_rect = pygame.Rect(0, 0, self.width, self.height)
        self.track_rect.center = self.location
        
        self.handle_size = (20, self.height + 8)
        self.handle_rect = pygame.Rect(0, 0, *self.handle_size)
        self.update_handle_position()
        
        # Optional label
        self.label = None
        self.label_rect = None
        if label:
            self.label = self.regular_font.render(label, False, color)
            self.label_rect = self.label.get_rect()
            self.label_rect.bottomleft = (self.track_rect.left, self.track_rect.top - 5)
    
    def update_handle_position(self):
        # Convert value to position
        range_normalized = (self.value - self.min_val) / (self.max_val - self.min_val)
        handle_x = self.track_rect.left + (self.track_rect.width * range_normalized)
        self.handle_rect.centerx = handle_x
        self.handle_rect.centery = self.track_rect.centery
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = max(self.min_val, min(value, self.max_val))
        self.update_handle_position()
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # Get mouse x position and convert to value
            mouse_x = max(self.track_rect.left, min(event.pos[0], self.track_rect.right))
            range_normalized = (mouse_x - self.track_rect.left) / self.track_rect.width
            self.value = self.min_val + (self.max_val - self.min_val) * range_normalized
            self.update_handle_position()
    
    def run(self):
        # Draw track
        pygame.draw.rect(self.screen, self.color, self.track_rect, 0, 3)
        
        # Draw handle
        pygame.draw.rect(self.screen, self.handle_color, self.handle_rect, 0, 5)
        pygame.draw.rect(self.screen, (255, 255, 255), self.handle_rect, 2, 5)
        
        # Draw label if exists
        if self.label:
            self.screen.blit(self.label, self.label_rect)
            
        # Optional: Draw current value
        value_text = self.regular_font.render(f"{int(self.value)}", False, self.color)
        value_rect = value_text.get_rect()
        value_rect.midright = (self.track_rect.right + 30, self.track_rect.centery)
        self.screen.blit(value_text, value_rect)