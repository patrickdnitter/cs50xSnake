from enum import Enum
from gamemode import GameMode

import button
import pygame

from gamestate import GameState


class MainMenuState(Enum):
    MainMenu = 0
    Highscore = 1
    Options = 2

class MainMenu(GameMode):

    def __init__(self, gamestate):
        super().__init__(gamestate)

        screen = gamestate.getScreen()
        self.main_menu_state = MainMenuState.MainMenu

        # Create MainMenu
        self.main_menu = pygame.Surface(screen.get_size())
        self.main_menu.fill("White")

        # Create Main Menu Buttons
        button_x_center = screen.get_width() // 2 - 100
        self.start_game_button = button.Button(button_x_center, 100, "Start Game", self.start_game)
        self.highscore_button = button.Button(button_x_center, 200, "Highscore", self.highscore)
        self.options_button = button.Button(button_x_center, 300, "Options", self.options)
        self.quit_button = button.Button(button_x_center, 400, "Quit", self.quit)

        # Connect Buttons to MainMenu
        self.start_game_button.draw_button(self.main_menu)
        self.highscore_button.draw_button(self.main_menu)
        self.options_button.draw_button(self.main_menu)
        self.quit_button.draw_button(self.main_menu)

        # Create HighscoreMenu
        self.highscore_menu = pygame.Surface(screen.get_size())
        self.highscore_menu.fill("White")

        # Create Highscore Buttons
        self.highscore_back = button.Button(button_x_center, 400, "Back", self.back_to_main_menu)

        # Connect Buttons to HighscoreMenu
        self.highscore_back.draw_button(self.highscore_menu)

        # Create OptionsMenu
        self.options_menu = pygame.Surface(screen.get_size())
        self.options_menu.fill("White")

        # Create Options Buttons
        self.options_back = button.Button(button_x_center, 400, "Back", self.back_to_main_menu)

        # Connect Buttons to OptionsMenu
        self.options_back.draw_button(self.options_menu)


    def start_game(self):
        print("Start Game")
        self.setRunning(False)
        game = self.gamestate.getGameMode("Game")
        if game is None: raise ValueError("GameMode Game not found.")
        self.setRunning(False)
        game.setRunning(True)

    def highscore(self):
        print("Highscore")
        self.main_menu_state = MainMenuState.Highscore

    def options(self):
        print("Options")
        self.main_menu_state = MainMenuState.Options

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
                            self.start_game_button.click(mouse_pos)
                            self.highscore_button.click(mouse_pos)
                            self.options_button.click(mouse_pos)
                            self.quit_button.click(mouse_pos)
                        elif self.main_menu_state == MainMenuState.Highscore:
                            self.highscore_back.click(mouse_pos)
                        elif self.main_menu_state == MainMenuState.Options:
                            self.options_back.click(mouse_pos)

            # Render Menu
            match self.main_menu_state:
                case MainMenuState.MainMenu:
                    self.gamestate.getScreen().blit(self.main_menu, (0, 0))
                case MainMenuState.Highscore:
                    self.gamestate.getScreen().blit(self.highscore_menu, (0, 0))
                case MainMenuState.Options:
                    self.gamestate.getScreen().blit(self.options_menu, (0, 0))


            # Update the current surface
            pygame.display.flip()

            # Limit FPS to 60
            self.gamestate.getClock().tick(60)