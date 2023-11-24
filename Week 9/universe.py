from planet import Planet
import random
from robot import Robot
from human import Human


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
