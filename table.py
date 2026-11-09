import pygame

class Table:
    def __init__(self, pos_x= 0, pos_y= 0, width = 200, height = 100, data=None):
        if data is None:
            data = []

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.data = data

    def draw(self, screen, gamestate, count = 5):
        # Create Surface
        table = pygame.Surface(gamestate.getScreenSize())
        table.fill("White")

        font = pygame.font.SysFont("Times New Roman", 20)

        for i, d in enumerate(self.data[:count]):
            rect = pygame.Rect(self.pos_x, self.pos_y+(i*self.height), self.width, self.height)
            pygame.draw.rect(table, "Gray", rect)

            text_img = font.render(str(d["name"]) + " " + str(d["score"]), True, "Black")
            # Center Text
            text_width = self.pos_x + self.width // 2 - text_img.get_width() // 2
            text_height = self.pos_y + self.height // 2 - text_img.get_height() // 2

            table.blit(text_img, (text_width, text_height+(i*self.height)))

        screen.blit(table, (0,0))