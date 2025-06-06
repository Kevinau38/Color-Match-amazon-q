import pygame
import sys
from game import Game

def main():
    # Initialize pygame
    pygame.init()
    
    # Create game instance
    game = Game()
    
    # Run the game
    try:
        game.run()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()