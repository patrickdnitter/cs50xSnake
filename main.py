import pygame

def main():
    pygame.init() # Initialize all pygame modules

    screen = pygame.display.set_mode((1280, 720)) #Return Surface to draw on
    clock = pygame.time.Clock() # Helper to create tick mainly

    running = True
    while running:
        if pygame.event.peek(pygame.QUIT): # Fast Exit if there is a Event that wants to quit the game
            running = False
            continue

        # Functionality for queued events
        for event in pygame.event.get():
            pass

        screen.fill("blue") # Color the screen blue

        pygame.display.flip() # Update the current surface

        clock.tick(60) # Limit FPS to 60

    pygame.quit() # Uninitialize all pygame modules

if __name__ == '__main__':
    main()