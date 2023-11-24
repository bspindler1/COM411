from planet import Planet
import random
from robot import Robot
from human import Human

import matplotlib.pyplot as plt



class Universe:

    def __init__(self):
        self.planets = []

    def generate(self):  #
        for random_num in range(random.randint(1, 10)):
            planet = Planet(f"planet {random_num}")

            for index in range(random.randint(1, 10)):
                robot = Robot(f"Robot{index}")
                planet.add_robot(robot)

            for index in range(random.randint(1, 10)):
                human = Human(f"Human{index}")
                planet.add_human(human)

            self.planets.append(planet)

    def __repr__(self):
        return f"universe(planets = {self.planets})"

    def __str__(self):
        return f"universe(planets = {self.planets}"

    def show_populations(self, selection):
        x_values = []
        y_values = []

        for planet in self.planets:
            x_values.append(planet.name)

            if selection == "human":
                y_values.append(len(planet.inhabitants['humans']))
            else:
                y_values.append(len(planet.inhabitants['robots']))


        plt.bar(x_values, y_values)
        plt.show()

if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    print(repr(universe))
    universe.show_populations("humans")
    universe.show_populations("robots")