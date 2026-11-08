import pygame

from game import Game
from highscore import Highscore
from mainmenu import MainMenu
from gamestate import GameState


def main():
    pygame.init() # Initialize all pygame modules

    screen = pygame.display.set_mode((1280, 720)) #Return Surface to draw on
    clock = pygame.time.Clock() # Helper to create tick mainly
    highscore = Highscore()


    # Gamestate
    gamestate = GameState(screen, clock, highscore)

    # Main Menu
    main_menu = MainMenu(gamestate)
    gamestate.addGameMode("MainMenu", main_menu)

    # Game
    game = Game(gamestate)
    gamestate.addGameMode("Game", game)

    # Start with MainMenu
    main_menu.setRunning(True)
    while gamestate.getStillRunning():
        if pygame.event.peek(pygame.QUIT):
            print("Press X in GameLoop")
            break

        if main_menu.getRunning():
            main_menu.gameloop()
        elif game.getRunning():
            game.gameloop()

    pygame.quit() # Uninitialize all pygame modules

if __name__ == '__main__':
    main()