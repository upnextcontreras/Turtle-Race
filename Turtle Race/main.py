from turtlerace import TurtleRace

# Main file logic
if __name__ == "__main__":
    race = TurtleRace()
    rounds = int(input("Enter the number of rounds for the tournament: "))
    race.start_tournament(rounds)
