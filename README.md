# Turtle Racing Game

Welcome to the **Turtle Racing Game**! This Python program uses the `turtle` module to simulate a fun and interactive turtle race where multiple turtles race to the finish line. You can run multiple rounds in a tournament, and each turtle leaves a trail as they move across the screen.

## Features

- **Multiple Rounds:** Set the number of rounds for the tournament.
- **Scoring System:** After each round, the winning turtle earns points, and the final scores are displayed at the end of the tournament.
- **Random Movements:** Each turtle's movement is randomized, making the race exciting and unpredictable.
- **Path Reset:** After each round, the paths drawn by the turtles are cleared, and the turtles return to the starting position.

## Demo

<img width="300" height="350" alt="TURTLE 2" src="https://github.com/user-attachments/assets/45d73ed5-0028-4c89-bfcc-6ef8029eb380">

## Requirements

- **Python 3.x**: Make sure you have Python 3.x installed on your system.
- **Turtle Module**: The turtle module is included in Python's standard library, so you don't need to install any additional dependencies.

## How to Run

1. **Clone the repository** to your local machine:
   
   ```bash
   git clone https://github.com/yourusername/turtle-racing-game.git 

2. Navigate to the project directory:

   cd turtle-racing-game
   
3. Run the game:
   
   python3 main.py

 # 4. Follow the on-screen instructions:
   - Enter the number of racers(between 2 and 10).
   - Enter the number of rounds for the tournament.
   - Watch the turtles race and enjoy the game!

## Example Output

<img width="500" height="300" alt="OUTPUT" src="https://github.com/user-attachments/assets/441ba0bc-e097-4b26-9f0f-76e9aa14b799">


## Customization

You can customize the turtle racing game in several ways:
   - Change the colors of the turtles by modifying the COLORS list in the TurtleRace class.
   - Adjust the size of the racing screen by modifying the WIDTH and HEIGHT variables.
   - Modify the movement speed by changing the range in the random.randrange(1, 20) function inside the race() method.
