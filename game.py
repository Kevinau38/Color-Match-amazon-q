import pygame
import random
import sys
from constants import *
from tile import Tile

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Color Match - Kevin Tran FCJ")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 18, bold=True)
        self.reset_game()

    def reset_game(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.moves_left = MAX_MOVES
        self.game_over = False
        self.won = False
        self.selected_color = 0
        self.selected_tile = (0, 0)  # Track currently selected tile position
        
        # Initialize grid with random colors
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color_id = random.randint(0, len(COLORS) - 1)
                self.grid[row][col] = Tile(color_id, row, col)
        
        # Set the starting position
        self.grid[0][0].selected = True

    def calculate_color_percentages(self):
        """Calculate percentage of each color on the board"""
        color_counts = {}
        total = GRID_SIZE * GRID_SIZE
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color_id = self.grid[row][col].color_id
                if color_id not in color_counts:
                    color_counts[color_id] = 0
                color_counts[color_id] += 1
        
        # Convert counts to percentages
        color_percentages = {color_id: (count / total) * 100 
                            for color_id, count in color_counts.items()}
        
        return color_percentages
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        # Draw grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                tile = self.grid[row][col]
                if tile:
                    tile.draw(self.screen)

        # Draw color selection buttons
        button_width = WIDTH // len(COLORS)
        button_y = GRID_AREA_HEIGHT + 10  # Position buttons below the grid area
        for color_id, color in COLORS.items():
            button_rect = pygame.Rect(color_id * button_width, button_y, button_width, 30)
            
            # Highlight selected color
            if color_id == self.selected_color:
                pygame.draw.rect(self.screen, BUTTON_HOVER_COLOR, button_rect)
            else:
                pygame.draw.rect(self.screen, BUTTON_COLOR, button_rect)
                
            pygame.draw.rect(self.screen, color, 
                             (button_rect.x + 5, button_rect.y + 5, 
                              button_rect.width - 10, button_rect.height - 10))

        # Draw moves left
        moves_text = self.font.render(f"Moves: {self.moves_left}", True, TEXT_COLOR)
        self.screen.blit(moves_text, (10, 10))
        
        # Calculate and display most common color percentage
        percentages = self.calculate_color_percentages()
        if percentages:
            max_color_id = max(percentages, key=percentages.get)
            max_percentage = percentages[max_color_id]
            percentage_text = self.font.render(f"Best Fill: {max_percentage:.1f}%", True, TEXT_COLOR)
            self.screen.blit(percentage_text, (WIDTH - percentage_text.get_width() - 10, 10))
        
        # Draw instructions
        instructions = self.small_font.render("Click on grid to select tile, then choose a color", True, TEXT_COLOR)
        self.screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, 40))
        
        # Draw game over or win message
        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            self.screen.blit(overlay, (0, 0))
            
            # Calculate final results
            percentages = self.calculate_color_percentages()
            max_color_id = max(percentages, key=percentages.get)
            max_percentage = percentages[max_color_id]
            
            # Show game results
            game_over_text = self.font.render("Game Over!", True, TEXT_COLOR)
            
            # Get color name based on color_id
            color_names = {
                0: "Red", 1: "Green", 2: "Blue", 
                3: "Yellow", 4: "Magenta", 5: "Cyan"
            }
            color_name = color_names.get(max_color_id, f"Color {max_color_id}")
            
            # Show results
            result_text = self.font.render(f"Best color: {color_name} ({max_percentage:.1f}%)", True, TEXT_COLOR)
            restart_text = self.small_font.render("Press R to restart", True, TEXT_COLOR)
            
            # Display all text
            y_pos = HEIGHT // 2 - 60
            self.screen.blit(
                game_over_text,
                (WIDTH // 2 - game_over_text.get_width() // 2, y_pos)
            )
            y_pos += 40
            self.screen.blit(
                result_text,
                (WIDTH // 2 - result_text.get_width() // 2, y_pos)
            )
            y_pos += 40
            self.screen.blit(
                restart_text,
                (WIDTH // 2 - restart_text.get_width() // 2, y_pos)
            )

        pygame.display.flip()

    def select_tile(self, row, col):
        """Select a tile at the given position"""
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            return False
            
        # Clear previous selection
        prev_row, prev_col = self.selected_tile
        if 0 <= prev_row < GRID_SIZE and 0 <= prev_col < GRID_SIZE:
            self.grid[prev_row][prev_col].selected = False
            
        # Set new selection
        self.grid[row][col].selected = True
        self.selected_tile = (row, col)
        return True
        
    def change_color(self, new_color):
        """Change the color of the selected tile"""
        row, col = self.selected_tile
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            return False
            
        # Don't count as a move if selecting the same color
        if self.grid[row][col].color_id == new_color:
            return False
            
        # Change the color of the selected tile
        self.grid[row][col].color_id = new_color
        
        # Decrement moves
        self.moves_left -= 1
        if self.moves_left <= 0:
            self.game_over = True
            
        return True

    def handle_click(self, pos):
        """Handle mouse click on the screen"""
        x, y = pos
        
        # Check if click is on color buttons
        button_y = GRID_AREA_HEIGHT + 10
        if button_y <= y <= button_y + 30:
            button_width = WIDTH // len(COLORS)
            color_id = x // button_width
            if 0 <= color_id < len(COLORS):
                self.selected_color = color_id
                self.change_color(color_id)
        # Check if click is on grid
        elif y < GRID_AREA_HEIGHT:
            col = x // TILE_SIZE
            row = y // TILE_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                self.select_tile(row, col)

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_r:
                        self.reset_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and not self.won:
                        self.handle_click(pygame.mouse.get_pos())
            
            # Draw everything
            self.draw()
            
            # Cap the frame rate
            self.clock.tick(FPS)