from enum import Enum
from gamemode import GameMode

import pygame
import button
import random

from gamestate import GameState


# Game Classes
class Field_State(Enum):
    NONE = 0
    SNAKE = 1
    FRUIT = 2

class Direction(Enum):
    UP = (0,-1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Field:
    def __init__(self, gamestate):
        self.gamestate = gamestate

        screen = self.gamestate.getScreen()
        width, height = screen.get_size()
        self.field_length = min(width, height)
        self.box_size = self.field_length // 20

        # Actual Screen Positions and Value
        self.field = []
        for pos_x in range(20):
            self.field.append([])
            for pos_y in range(20):
                self.field[pos_x].append([pos_x*self.box_size, pos_y*self.box_size, Field_State.NONE])

        # Free Locations with Nothing in it
        self.white_list = set([(i,j) for i in range(0, 20) for j in range(0, 20)])
        # Used Locations
        self.black_list = set()

    def getRandomDirection(self):
        return random.choice(list(Direction))

    def getRandomFreeLocation(self):
        return random.choice(list(self.white_list))

    def addLocation(self, pos=(0, 0)):
        self.black_list.add(pos)
        if pos not in self.white_list: raise ValueError("Invalid Location in whitelist " + str(pos))
        self.white_list.remove(pos)

    def removeLocation(self, pos=(0, 0)):
        self.white_list.add(pos)
        self.black_list.remove(pos)

    def addFruit(self):
        pos = self.getRandomFreeLocation()
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.FRUIT
        self.addLocation(pos)

    def removeFruit(self):
        pos = self.getRandomFreeLocation()
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.NONE
        self.removeLocation(pos)

    def addSnake(self, pos):
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.SNAKE
        self.addLocation(pos)

    def removeSnake(self, pos):
        pos_x, pos_y = self.getRandomFreeLocation()
        self.field[pos_x][pos_y][2] = Field_State.NONE
        self.removeLocation(pos)

class Snake:
    def __init__(self, field):
        # Queue
        self.body = []
        self.dir = Direction.DOWN
        self.score = 0

        # Choose the First body
        self.field = field
        pos = field.getRandomFreeLocation()
        dir = field.getRandomDirection()

        #Create Default Snake
        self.body.append(pos)
        self.field.addSnake(pos)
        self.dir = dir

    def draw(self, screen):
        screen.fill(pygame.Color("Black"))

        for pos in self.body:
            pos_x, pos_y, _ = self.field.field[pos[0]][pos[1]]
            width = self.field.box_size
            height = self.field.box_size

            rect = pygame.Rect(pos_x, pos_y, width, height)
            pygame.draw.rect(screen, pygame.Color("Green"), rect)

    def move(self):
        pass

    def grow(self):
        pass

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
        elif self.game_state != Game_State.GAME_OVER:
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
        field = Field(self.gamestate)
        snake = Snake(field)

        while self.getRunning():
            #Fast Exit when pressing the X in the Right Upper Corner
            if pygame.event.get(pygame.QUIT):
                print("Press X in Game")
                self.setRunning(False)
                continue

            #Functionality for queued events
            for event in pygame.event.get():
                # Keyboard Events everywhere
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause_menu_function()
                    elif event.key == pygame.K_l:
                        self.game_over_function()
                # Mouse Event only in Menus
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
                    snake.draw(self.gamestate.getScreen())
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
