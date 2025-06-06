# Color Match Game

<div style="display: flex; align-items: center; justify-content: center">
  <img src="Picture/fcj_logo.png" alt="FCJ Logo" style="height: 200px; margin-right: 20px;">
  <img src="Picture/q_logo.png" alt="Q Logo" style="height: 200px;">
</div>

A creative color tile game where you can create patterns by selecting and coloring individual tiles.

## Short demo

![Watch Demo Video](Picture/ColorMatch_demo.gif)

## Installation

1. Make sure you have Python 3.10 or More installed
2. Install Pygame:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

## How to Play

- Click on any tile in the grid to select it
- Click on a color at the bottom of the screen to change the selected tile's color
- Try to create patterns or fill the grid with a single color
- You have 20 moves to create your masterpiece
- Press R to restart the game
- Press ESC or Q to quit

## Features

- Interactive tile selection and coloring
- Six distinct medium-brightness colors
- Real-time tracking of your most dominant color percentage
- Game results showing your best color fill percentage
- Clean, modular code structure

## Project Structure

- `main.py` - Entry point
- `constants.py` - Game constants and color definitions
- `tile.py` - Tile class implementation
- `game.py` - Game logic and rendering

---

# Building Color Match Game: A Development Journey

This project was created as a different take on the original 2048 game, transforming it into a creative color matching experience.

## 1. Building the Basic Structure

Started with a clean slate, creating a 10x10 grid for more creative possibilities. The core structure was designed to be simple yet flexible.

## 2. Implementing Tile Selection

Added the ability to select individual tiles by clicking on them, with visual feedback showing the currently selected tile.

## 3. Adding Color Selection

Created a color palette with six distinct colors and implemented the ability to change the color of selected tiles.

## 4. Tracking Game Progress

Added a move counter and percentage tracking to show how much of the board is filled with the most dominant color.

## 5. Enhancing the User Interface

Improved the layout by separating the grid area from the controls, making it easier to interact with all tiles, especially those on the bottom row.

## 6. Fine-tuning the Experience

Adjusted the colors to be more visually appealing with medium brightness, and limited the moves to create a more challenging experience.

## My Experience with Amazon Q

Throughout the development of Color Match, Amazon Q has been an invaluable coding companion. I was particularly impressed by how it helped me transform my ideas into functional code with minimal effort. The AI assistant excelled at:

- Generating efficient, clean code that matched my requirements
- Providing insightful suggestions for game mechanics and improvements
- Helping debug issues quickly with targeted solutions
- Adapting existing code to implement new features
- Offering clear explanations that enhanced my understanding

Amazon Q significantly streamlined my development workflow, allowing me to focus more on the creative aspects of game design rather than getting stuck on implementation details.