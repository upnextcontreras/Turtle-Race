Turtle Racing Game 🐢
Description
The Turtle Racing Game is a fun and interactive game built using Python's turtle graphics library. Players can set the number of racing turtles, and the game will simulate multiple rounds where the turtles race to the finish line. The winner is displayed after each round, and scores are tracked across multiple rounds in a tournament format. The lines drawn by the turtles are cleared after each round to ensure a fresh race.

Features
🐢 Turtle Racing: Race turtles in an interactive environment with randomized speeds.
🎨 Customizable Racers: Choose between 2 to 10 racers, each with a unique color.
🏆 Tournament Mode: Run multiple rounds of races, and keep track of scores to crown the overall winner.
✨ Clean Tracks: The paths drawn by the turtles are cleared after each race, ensuring a fresh start for every round.
Demo


How to Install
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/turtle-racing-game.git
Navigate to the project directory:

bash
Copy code
cd turtle-racing-game
Make sure you have Python 3.x installed on your machine. You can download Python from here.

Install any necessary dependencies. The game uses the built-in turtle module, which comes with Python, so no external libraries are required.

How to Play
Run the game:

bash
Copy code
python main.py
You will be prompted to enter the number of turtles (racers) you'd like, between 2 and 10.

The race will start, and after each round, the winner will be announced. The tracks will clear automatically for the next round.

The game will run for the number of rounds you specify, and at the end, the total scores will be displayed.

Example:
bash
Copy code
Enter number of racers you would like (2 - 10): 5
Enter the number of rounds for the tournament: 3
Winner of round 1: green
Winner of round 2: blue
Winner of round 3: red

Final Scores:
Green: 10 points
Blue: 10 points
Red: 10 points
Customization
You can customize the game by tweaking a few aspects:

Turtle Colors: The turtle colors are pre-set in the COLORS list but can be changed or expanded.
Race Mechanics: The turtles' movement speed is randomized, but you can adjust the speed range in the race() method.
Future Enhancements
Add power-ups or obstacles to make the races more dynamic.
Allow users to customize turtle names or assign abilities.
Implement a multiplayer mode where players control different turtles with keyboard inputs.
