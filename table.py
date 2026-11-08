import pygame

class Table:
    def __init__(self, pos_x= 0, pos_y= 0, width = 200, height = 100, count = 0, data=None):
        if data is None:
            data = []

        self.width = width
        self.height = height

        self.table = pygame.Surface((width, height*min(count, len(data))))
        self.table.fill("Black")
        font = pygame.font.SysFont("Times New Roman", 20)

        for i, d in enumerate(data[:count]):
            rect = pygame.Rect(pos_x, pos_y+(i*height), width, height)
            pygame.draw.rect(self.table, "Gray", rect)
            text_img = font.render(str(d["name"]) + " " + str(d["score"]), True, "Black")
            self.table.blit(text_img, (pos_x, pos_y+(i*height)))

    def draw(self, screen):
        screen.blit(self.table, (0,0))