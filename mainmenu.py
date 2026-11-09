import table
import button
import pygame

from enum import Enum
from gamemode import GameMode

class MainMenuState(Enum):
    MainMenu = 0
    Highscore = 1

class MainMenu(GameMode):
    def __init__(self, main_gamestate):
        super().__init__(main_gamestate)

        # Presets
        self.main_menu_state = MainMenuState.MainMenu

        screen = self.getGameState().getScreen()
        button_width = 200
        button_x_center = screen.get_width() // 2 - button_width//2

        # Create Surface
        self.main_menu = pygame.Surface(screen.get_size())
        self.main_menu.fill("White")
        self.highscore_menu = pygame.Surface(screen.get_size())
        self.highscore_menu.fill("White")

        # Create Buttons
        self.start_game_button = button.Button(button_x_center, 100, button_width)
        self.highscore_button = button.Button(button_x_center, 200, button_width)
        self.highscore_back = button.Button(button_x_center, 400, button_width)
        self.quit_button = button.Button(button_x_center, 300, button_width)

        # Connect Buttons to Surface
        self.start_game_button.draw_button(self.main_menu, "Start Game")
        self.highscore_button.draw_button(self.main_menu, "Highscore")
        self.quit_button.draw_button(self.main_menu,"Quit")

    def start_game(self):
        print("Start Game")
        game = self.getGameState().getGameMode("MainGame")
        if game is None: raise ValueError("GameMode Game not found.")
        self.setRunning(False)
        game.setRunning(True)

    def highscore(self):
        print("Highscore")
        highscores = self.getGameState().getScores()

        screen = self.getGameState().getScreen()
        table_width = 200
        table_x_center = screen.get_width() // 2 - table_width // 2

        highscore_table = table.Table(table_x_center, 100, table_width, 50, data= highscores)
        highscore_table.draw(self.highscore_menu, self.getGameState(), 5)

        self.highscore_back.draw_button(self.highscore_menu, "Back to Main Menu")

        self.main_menu_state = MainMenuState.Highscore

    def quit(self):
        print("Quit")
        self.setRunning(False)

    def back_to_main_menu(self):
        print("Back to Main Menu")
        self.main_menu_state = MainMenuState.MainMenu

    def gameloop(self):
        while self.getRunning():
            # Fast Exit when pressing the X in the Right Upper Corner
            if pygame.event.get(pygame.QUIT):
                print("Press X in Main Menu")
                self.setRunning(False)
                continue

            # Functionality for queued events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.main_menu_state == MainMenuState.MainMenu:
                            self.start_game_button.click(mouse_pos, self.start_game)
                            self.highscore_button.click(mouse_pos, self.highscore)
                            self.quit_button.click(mouse_pos, self.quit)
                        elif self.main_menu_state == MainMenuState.Highscore:
                            self.highscore_back.click(mouse_pos, self.back_to_main_menu)

            # Render Menu
            match self.main_menu_state:
                case MainMenuState.MainMenu:
                    self.getGameState().blitScreen(self.main_menu, (0, 0))
                case MainMenuState.Highscore:
                    self.getGameState().blitScreen(self.highscore_menu, (0, 0))


            # Update the current surface
            pygame.display.flip()

            # Limit FPS to 60
            self.getGameState().tick(60)