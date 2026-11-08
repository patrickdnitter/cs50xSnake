from enum import Enum
from gamemode import GameMode

import pygame
import button
from gamestate import GameState


class Game_State(Enum):
    GAME = 0
    PAUSE_MENU = 1
    PAUSE_OPTIONS = 2
    GAME_OVER = 3

class Game(GameMode):

    def __init__(self, gamestate):
        super().__init__(gamestate)

        screen = gamestate.getScreen()
        self.game_state = Game_State.GAME

        # Create PauseMenu
        self.pause_menu = pygame.Surface(screen.get_size())
        self.pause_menu.fill(pygame.Color("Black"))

        # Create PauseMenu Buttons
        button_x_center = screen.get_width() // 2 - 100
        self.continue_button = button.Button(button_x_center, 100, "Continue", self.continue_game)
        self.options_button = button.Button(button_x_center, 200, "Options", self.options_menu)
        self.back_to_main_menu_button = button.Button(button_x_center, 300, "Back to Main Menu", self.back_to_main_menu)
        self.quit_button = button.Button(button_x_center, 400, "Quit", self.quit_menu)

        # Connect Buttons to PauseMenu
        self.continue_button.draw_button(self.pause_menu)
        self.options_button.draw_button(self.pause_menu)
        self.back_to_main_menu_button.draw_button(self.pause_menu)
        self.quit_button.draw_button(self.pause_menu)

        # Create OptionsMenu
        self.options_menu = pygame.Surface(screen.get_size())
        self.options_menu.fill(pygame.Color("Black"))

        # Create Options Buttons
        self.options_back = button.Button(button_x_center, 400, "Back", self.back_to_pause_menu)

        # Connect Buttons to OptionsMenu
        self.options_back.draw_button(self.options_menu)

        # Create GameOverMenu
        self.game_over = pygame.Surface(screen.get_size())
        self.game_over.fill(pygame.Color("Black"))

        # Create GameOver Buttons
        self.game_over_restart = button.Button(button_x_center, 100, "Restart Game", lambda: print("Restart Game"))
        self.game_over_back_to_main_menu_button = button.Button(button_x_center, 200, "Back to Main Menu", self.back_to_main_menu)
        self.game_over_quit = button.Button(button_x_center, 300, "Quit", self.quit_menu)

        # Connect GameOver Buttons
        self.game_over_restart.draw_button(self.game_over)
        self.game_over_back_to_main_menu_button.draw_button(self.game_over)
        self.game_over_quit.draw_button(self.game_over)


    def pause_menu_function(self):
        print("PauseMenu")
        if self.game_state == Game_State.GAME:
            self.game_state = Game_State.PAUSE_MENU
        else:
            self.game_state = Game_State.GAME

    def game_over_function(self):
        print("GameOver")
        self.game_state = Game_State.GAME_OVER


    def continue_game(self):
        print("Continue")
        self.game_state = Game_State.GAME

    def options_menu(self):
        print("OptionsMenu")
        self.game_state = Game_State.PAUSE_OPTIONS

    def back_to_main_menu(self):
        print("Back to Main Menu")
        self.game_state = Game_State.GAME
        main_menu = self.gamestate.getGameMode("MainMenu")
        if main_menu is None: raise ValueError("MainMenu not found")
        self.setRunning(False)
        main_menu.setRunning(True)

    def quit_menu(self):
        print("Quit")
        self.setRunning(False)

    def back_to_pause_menu(self):
        print("Back to Pause Menu")
        self.game_state = Game_State.PAUSE_MENU

    def gameloop(self):
        while self.getRunning():
            #Fast Exit when pressing the X in the Right Upper Corner
            if pygame.event.get(pygame.QUIT):
                print("Press X in Game")
                self.setRunning(False)
                continue

            #Functionality for queued events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause_menu_function()
                    elif event.key == pygame.K_l:
                        self.game_over_function()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.game_state == Game_State.PAUSE_MENU:
                            self.continue_button.click(mouse_pos)
                            self.options_button.click(mouse_pos)
                            self.back_to_main_menu_button.click(mouse_pos)
                            self.quit_button.click(mouse_pos)
                        elif self.game_state == Game_State.PAUSE_OPTIONS:
                            self.options_back.click(mouse_pos)
                        elif self.game_state == Game_State.GAME_OVER:
                            self.game_over_restart.click(mouse_pos)
                            self.game_over_back_to_main_menu_button.click(mouse_pos)
                            self.game_over_quit.click(mouse_pos)

            # Render Screen
            match self.game_state:
                case Game_State.GAME:
                    self.gamestate.getScreen().fill(pygame.Color("Black"))
                    # TODO GameLogic Snake
                case Game_State.PAUSE_MENU:
                    self.gamestate.getScreen().blit(self.pause_menu, (0, 0))
                case Game_State.PAUSE_OPTIONS:
                    self.gamestate.getScreen().blit(self.options_menu, (0, 0))
                case Game_State.GAME_OVER:
                    self.gamestate.getScreen().blit(self.game_over, (0, 0))

            #Update the current surface
            pygame.display.flip()

            # Limit FPS to 60
            self.gamestate.getClock().tick(60)
