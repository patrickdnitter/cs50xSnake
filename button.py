import pygame

# General Instructions how to create a Button: https://www.youtube.com/watch?v=jyrP0dDGqgY
class Button:
    def __init__(self, pos_x = 0, pos_y = 0, width = 200, height = 50):
        if not pygame.get_init():
            raise ValueError("Button requires activ modules. Create Button after initialization.")

        # Class Variables
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.button_rect = None

    def draw_button(self, surface, text = "", text_color = "Black", rect_color = "Gray"):

        # Create Font Object for Button
        font = pygame.font.SysFont("Times New Roman", 23)

        # Render Text
        text_img = font.render(text, True, text_color)
        # Center Text
        text_width = self.pos_x + self.width // 2 - text_img.get_width() // 2
        text_height = self.pos_y + self.height // 2 - text_img.get_height() // 2

        # Create Rect Object for Button
        self.button_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        # Add Rect to Surface
        pygame.draw.rect(surface, rect_color, self.button_rect)

        # Add Text to Surface
        surface.blit(text_img, (text_width, text_height))

    # When the Point is in the rect, the associated function is called
    def click(self, pos, method_clicked):
        pos_x, pos_y = pos
        if self.button_rect and self.button_rect.collidepoint(pos_x, pos_y):
            method_clicked()