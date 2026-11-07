import pygame
from mainmenu import MainMenu
from gamestate import GameState


def main():
    pygame.init() # Initialize all pygame modules

    screen = pygame.display.set_mode((1280, 720)) #Return Surface to draw on
    clock = pygame.time.Clock() # Helper to create tick mainly

    # Gamestate
    gamestate = GameState(screen, clock)

    # Main Menu
    main_menu = MainMenu(gamestate)
    gamestate.addGameMode("MainMenu", main_menu)

    # Start with MainMenu
    main_menu.setRunning(True)
    while gamestate.getStillRunning():
        if pygame.event.peek(pygame.QUIT):
            print("Press X in GameLoop")
            break

        if main_menu.getRunning():
            main_menu.gameloop()

    pygame.quit() # Uninitialize all pygame modules

if __name__ == '__main__':
    main()