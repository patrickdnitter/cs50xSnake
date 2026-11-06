import pygame
import button

def main():
    pygame.init() # Initialize all pygame modules

    screen = pygame.display.set_mode((1280, 720)) #Return Surface to draw on
    clock = pygame.time.Clock() # Helper to create tick mainly

    # Main Menu
    main_menu = pygame.Surface(screen.get_size())
    button_x_center = screen.get_width() // 2 - 100
    start_game_button = button.Button(button_x_center, 100, "Start Game", lambda: print("Start Game"))
    highscore_button = button.Button(button_x_center, 200, "Highscore", lambda: print("Highscore"))
    options_button = button.Button(button_x_center, 300, "Options", lambda: print("Options"))
    quit_button = button.Button(button_x_center, 400, "Quit", lambda: print("Quit"))

    running = True
    while running:
        if pygame.event.peek(pygame.QUIT): # Fast Exit if there is a Event that wants to quit the game
            running = False
            continue

        # Functionality for queued events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: # Left Mouse Click
                    start_game_button.click(pygame.mouse.get_pos())
                    highscore_button.click(pygame.mouse.get_pos())
                    options_button.click(pygame.mouse.get_pos())
                    if quit_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                        running = False

        screen.fill("White") # Color the screen blue

        start_game_button.draw_button(screen)
        highscore_button.draw_button(screen)
        options_button.draw_button(screen)
        quit_button.draw_button(screen)

        pygame.display.flip() # Update the current surface

        clock.tick(60) # Limit FPS to 60

    pygame.quit() # Uninitialize all pygame modules

if __name__ == '__main__':
    main()