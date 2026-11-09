import pygame

from gamestate import GameState
from highscore import Highscore

from mainmenu import MainMenu
from game import Game

def main():
    # Initialize all pygame Modules
    pygame.init()

    # Set Caption to Snake
    pygame.display.set_caption("Snake")
    # Create Surface to Draw everything on. This is the Upper-Level Surface for the game
    screen = pygame.display.set_mode((720, 720))
    # Helpers Classes to track Time and Score
    clock = pygame.time.Clock()
    highscore = Highscore()

    # Helper Class that resembles a HUB for the Information needed in all GameModes
    main_gamestate = GameState(screen, clock, highscore)

    # Main Menu
    main_menu = MainMenu(main_gamestate)
    main_gamestate.addGameMode("MainMenu", main_menu)

    # Main Game
    main_game = Game(main_gamestate)
    main_gamestate.addGameMode("MainGame", main_game)

    # Start with MainMenu
    main_menu.setRunning(True)
    while main_gamestate.getStillRunning():
        if main_menu.getRunning():
            main_menu.gameloop()
        elif main_game.getRunning():
            main_game.gameloop()

    # Uninitialize all pygame Modules
    pygame.quit()

if __name__ == '__main__':
    main()