from enum import Enum
from gamemode import GameMode

import pygame
import button
import random

from gamestate import GameState
from highscore import Highscore


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
    def __init__(self, main_gamestate):
        self.main_gamestate = main_gamestate

        screen = self.main_gamestate.getScreen()
        width, height = screen.get_size()
        self.field_length = min(width, height)
        self.box_size = self.field_length // 21

        # Actual Screen Positions and Value
        self.field = []
        for pos_x in range(20):
            self.field.append([])
            for pos_y in range(1,21):
                self.field[pos_x].append([pos_x*self.box_size + self.box_size//2, pos_y*self.box_size, Field_State.NONE])

        # Free Locations with Nothing in it
        self.white_list = set([(i,j) for i in range(0, 20) for j in range(0, 20)])
        # Used Locations
        self.black_list = set()
        self.fruit = None

    # Return tuple
    def getRandomDirection(self):
        return random.choice(list(Direction))

    # Return tuple
    def getRandomFreeLocation(self):
        return random.choice(list(self.white_list))

    def addLocation(self, pos):
        self.black_list.add(pos)
        self.white_list.remove(pos)

    def removeLocation(self, pos):
        self.white_list.add(pos)
        self.black_list.remove(pos)

    def addFruit(self):
        pos = self.getRandomFreeLocation()
        self.fruit = pos
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.FRUIT

    def draw_fruit(self, screen):
        if self.fruit is None: return
        pos_x, pos_y, _ = self.field[self.fruit[0]][self.fruit[1]]
        width, height = self.box_size, self.box_size

        rect = pygame.Rect(pos_x, pos_y, width, height)
        pygame.draw.rect(screen, pygame.Color("Red"), rect)

    def addSnake(self, pos):
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.SNAKE
        self.addLocation(pos)

    def removeSnake(self, pos):
        pos_x, pos_y = pos
        self.field[pos_x][pos_y][2] = Field_State.NONE
        self.removeLocation(pos)

class Snake:
    def __init__(self, field):
        # Queue
        self.body = []
        self.dir = Direction.DOWN
        self.score = 0
        self.tempo = 300 # Less than 60 FPS

        # Choose the First body
        self.field = field
        pos = field.getRandomFreeLocation()
        dir = field.getRandomDirection()

        #Create Default Snake
        self.body.append(pos)
        self.field.addSnake(pos)
        self.dir = dir

    def getCurrentTempo(self):
        return self.tempo

    def draw(self, screen):
        for pos in self.body:
            pos_x, pos_y, _ = self.field.field[pos[0]][pos[1]]
            width = self.field.box_size
            height = self.field.box_size

            rect = pygame.Rect(pos_x, pos_y, width, height)
            pygame.draw.rect(screen, pygame.Color("Green"), rect)

    # Return True if able to move there, False otherwise
    def move(self):
        curr_head = self.body[-1]
        curr_dir = self.dir

        next_head = (curr_head[0] + curr_dir.value[0], curr_head[1] + curr_dir.value[1])
        if next_head in self.field.white_list:
            if self.field.field[next_head[0]][next_head[1]][2] == Field_State.FRUIT:
                self.grow(next_head)
            elif self.field.field[next_head[0]][next_head[1]][2] == Field_State.NONE:
                # Add head to top
                self.body.append(next_head)
                self.field.addSnake(next_head)

                # Remove tail from bottom
                pos = self.body.pop(0)
                self.field.removeSnake(pos)
            else:
                pass
            return True
        else:
            return False

    def grow(self, pos):
        # Add head to top
        self.body.append(pos)
        self.field.addSnake(pos)
        self.field.addFruit()
        self.score += 1

class Game_State(Enum):
    GAME = 0
    PAUSE_MENU = 1
    GAME_OVER = 2
    MAIN_MENU = 3

class Game(GameMode):
    def __init__(self, gamestate):
        super().__init__(gamestate)

        screen = gamestate.getScreen()
        self.game_state = Game_State.GAME

        # Score Board
        self.font = pygame.font.SysFont("Times New Roman", 20)

        # Create PauseMenu
        self.pause_menu = pygame.Surface(screen.get_size())
        self.pause_menu.fill(pygame.Color("Black"))

        # Create PauseMenu Buttons
        button_width = 200
        button_x_center = screen.get_width() // 2 - button_width//2
        self.continue_button = button.Button(button_x_center, 100, button_width)
        self.back_to_main_menu_button = button.Button(button_x_center, 200, button_width)
        self.quit_button = button.Button(button_x_center, 300, button_width)

        # Connect Buttons to PauseMenu
        self.continue_button.draw_button(self.pause_menu, "Continue")
        self.back_to_main_menu_button.draw_button(self.pause_menu, "Back to Main Menu")
        self.quit_button.draw_button(self.pause_menu, "Quit")

        # Create GameOverMenu
        self.game_over = pygame.Surface(screen.get_size())
        self.game_over.fill(pygame.Color("Black"))

        # Create GameOver Buttons
        self.game_over_restart = button.Button(button_x_center, 100, button_width)
        self.game_over_back_to_main_menu_button = button.Button(button_x_center, 200, button_width)
        self.game_over_quit = button.Button(button_x_center, 300, button_width)

        # Connect GameOver Buttons
        self.game_over_restart.draw_button(self.game_over, "Restart")
        self.game_over_back_to_main_menu_button.draw_button(self.game_over, "Back to Main Menu")
        self.game_over_quit.draw_button(self.game_over, "Quit")

    def pause_menu_function(self):
        print("PauseMenu")
        if self.game_state == Game_State.GAME:
            self.game_state = Game_State.PAUSE_MENU
        elif self.game_state != Game_State.GAME_OVER:
            self.game_state = Game_State.GAME

    def game_over_function(self):
        print("GameOver")
        self.main_gamestate.addScore("Highscore", self.snake.score)
        self.main_gamestate.saveHighscore()
        self.game_state = Game_State.GAME_OVER

    def continue_game(self):
        print("Continue")
        self.game_state = Game_State.GAME

    def back_to_main_menu(self):
        print("Back to Main Menu")
        self.game_state = Game_State.MAIN_MENU
        main_menu = self.main_gamestate.getGameMode("MainMenu")
        self.setRunning(False)
        main_menu.setRunning(True)

    def quit_menu(self):
        print("Quit")
        self.setRunning(False)

    def start_game(self):
        self.game_state = Game_State.GAME
        self.field = Field(self.main_gamestate)
        self.snake = Snake(self.field)
        self.last_move = pygame.time.get_ticks()
        self.field.addFruit()

    def draw_game(self):
        text_img = self.font.render("Score: " + str(self.snake.score), True, "White")
        self.main_gamestate.fillScreen(pygame.Color("Black"))
        self.main_gamestate.blitScreen(text_img, (0, 0))
        self.snake.draw(self.main_gamestate.getScreen())
        self.field.draw_fruit(self.main_gamestate.getScreen())

    def gameloop(self):
        # Init Snake and Field
        self.start_game()
        self.draw_game()

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
                    elif event.key == pygame.K_r:
                        self.start_game() # Restart Game
                    if self.game_state == Game_State.GAME:
                        if event.key == pygame.K_w:
                            self.snake.dir = Direction.UP
                        elif event.key == pygame.K_s:
                            self.snake.dir = Direction.DOWN
                        elif event.key == pygame.K_a:
                            self.snake.dir = Direction.LEFT
                        elif event.key == pygame.K_d:
                            self.snake.dir = Direction.RIGHT

                # Mouse Event only in Menus
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.game_state == Game_State.PAUSE_MENU:
                            self.continue_button.click(mouse_pos, self.continue_game)
                            self.back_to_main_menu_button.click(mouse_pos, self.back_to_main_menu)
                            self.quit_button.click(mouse_pos, self.quit_menu)
                        elif self.game_state == Game_State.GAME_OVER:
                            self.game_over_restart.click(mouse_pos, self.start_game)
                            self.game_over_back_to_main_menu_button.click(mouse_pos, self.back_to_main_menu)
                            self.game_over_quit.click(mouse_pos, self.quit_menu)

            # Render Screen
            match self.game_state:
                case Game_State.GAME:
                    if pygame.time.get_ticks() - self.last_move > self.snake.getCurrentTempo():
                        if self.snake.move():
                            self.draw_game()
                        else:
                            self.game_over_function()
                        self.last_move = pygame.time.get_ticks()
                case Game_State.PAUSE_MENU:
                    self.main_gamestate.blitScreen(self.pause_menu, (0, 0))
                case Game_State.GAME_OVER:
                    self.main_gamestate.blitScreen(self.game_over, (0, 0))
                case Game_State.MAIN_MENU:
                    self.game_state = Game_State.GAME
                    break

            #Update the current surface
            pygame.display.flip()

            # Limit FPS to 60
            self.main_gamestate.tick(60)
