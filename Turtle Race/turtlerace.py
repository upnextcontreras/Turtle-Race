import turtle
import random
import time

class TurtleRace:
    WIDTH = 500
    HEIGHT = 500
    COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'cyan', 'gold', 'silver', 'brown']
    
    def __init__(self):
        self.racers = self.get_num_of_racers()  # Ask for number of racers first
        random.shuffle(self.COLORS)
        self.colors = self.COLORS[:self.racers]
        self.turtles = []

    def get_num_of_racers(self):
        while True:
            racers = input('Enter number of racers you would like (2 - 10): ')
            if racers.isdigit():
                racers = int(racers)
            else:
                print('Input is not numeric ... Add Valid Option!')
                continue
            if 2 <= racers <= 10:
                return racers
            else:
                print('Number is not in range. Enter a number in the correct range!')

    def init_screen(self):
        self.screen = turtle.Screen()
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.title('TURTLE RACING')

    def create_turtles(self):
        self.turtles = []  # Reset turtles for each race
        spacingx = self.WIDTH // (len(self.colors) + 1)
        for i, color in enumerate(self.colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-self.WIDTH // 2 + (i + 1) * spacingx, -self.HEIGHT // 2 + 20)
            racer.pendown()
            self.turtles.append(racer)
    
    def reset_turtles(self):
        """Resets the turtles to the starting position and clears their paths."""
        spacingx = self.WIDTH // (len(self.colors) + 1)
        for i, racer in enumerate(self.turtles):
            racer.penup()  # Lift the pen so no line is drawn while resetting position
            racer.clear()  # Clear the path drawn by the turtle
            racer.setpos(-self.WIDTH // 2 + (i + 1) * spacingx, -self.HEIGHT // 2 + 20)
            racer.pendown()  # Put the pen down for drawing in the next round

    def race(self):
        self.create_turtles()  # Ensure turtles are recreated for each race
        while True:
            for racer in self.turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                _, y = racer.pos()
                if y >= self.HEIGHT // 2 - 10:
                    return self.colors[self.turtles.index(racer)]

    def start_race(self):
        self.init_screen()  # Initialize the screen only after racers are selected
        winner = self.race()
        print("WINNER:", winner)
        time.sleep(10)

    def start_tournament(self, num_rounds):
        # Initialize the screen before starting the tournament
        self.init_screen()

        scores = {color: 0 for color in self.colors}
        for round_num in range(num_rounds):
            if round_num > 0:
                self.reset_turtles()  # Clear the lines and reset positions before each round

            winner = self.race()  # Race and get the winner
            scores[winner] += 10  # Award points to the winner
            print(f"Winner of round {round_num + 1}: {winner}")
            time.sleep(2)  # Pause between rounds

        print("\nFinal Scores:")
        for color, score in scores.items():
            print(f"{color.capitalize()}: {score} points")

        return scores


