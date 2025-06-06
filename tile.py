from constants import TILE_SIZE, COLORS

class Tile:
    def __init__(self, color_id=0, row=0, col=0):
        self.color_id = color_id
        self.row = row
        self.col = col
        self.x = col * TILE_SIZE
        self.y = row * TILE_SIZE
        self.selected = False
        self.matched = False
        
    def draw(self, screen):
        # Get color based on color_id
        color = COLORS.get(self.color_id, (100, 100, 100))
        
        # Draw tile with border
        import pygame
        pygame.draw.rect(
            screen, 
            color, 
            (self.x + 2, self.y + 2, TILE_SIZE - 4, TILE_SIZE - 4),
            0, 3
        )
        
        # Draw highlight if selected
        if self.selected:
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (self.x + 1, self.y + 1, TILE_SIZE - 2, TILE_SIZE - 2),
                2, 3
            )