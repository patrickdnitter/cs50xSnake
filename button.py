import pygame

# General Instructions how to create a Button: https://www.youtube.com/watch?v=jyrP0dDGqgY
class Button:
    def __init__(self, pos_x = 0, pos_y = 0, text = "", method_clicked = lambda: print("Button clicked!")):
        if not pygame.get_init():
            raise ValueError("Button requires activ modules. Create Button after initialization.")

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 200
        self.height = 50

        self.text = text
        self.method_clicked = method_clicked

        # Create Font Object for Button
        self.font = pygame.font.SysFont("Times New Roman", 20)
        self.color_text = pygame.Color("Black")

        # Create Rect Object for Button
        self.button_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.color_rect = pygame.Color("Gray")

    def draw_button(self, surface):
        # Add Rect to Surface
        pygame.draw.rect(surface, self.color_rect, self.button_rect)

        # Render Text
        text_img = self.font.render(self.text, True, self.color_text)

        # Center Text
        text_width = self.pos_x + self.width//2 - text_img.get_width()//2
        text_height = self.pos_y + self.height//2 - text_img.get_height()//2

        # Add Text to Surface
        surface.blit(text_img, (text_width, text_height))

    def is_selected(self, pos_x, pos_y):
        # Returns True when the mouse is in the rect
        return self.button_rect.collidepoint(pos_x, pos_y)


    # When the Point is in the rect, the associated function is called
    def click(self, pos):
        pos_x, pos_y = pos
        if self.is_selected(pos_x, pos_y):
            self.method_clicked()